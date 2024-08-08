from collections import defaultdict
import functools
import dis
import logging
from threading import Condition
import time
import multiprocessing
import sys
import os
import json
import threading
import pty
import collections
import subprocess
import signal
from typing import (
    DefaultDict,
    Optional,
    Tuple,
    Dict,
    Callable,
    Union,
    List,
    Any,
)
from logging.handlers import DatagramHandler
from websocket_server import WebsocketServer  # type: ignore
from py2cfg.builder import CFGBuilder
from py2cfg._source_db import CFG_Database


# --- Forward type declarations --- #
# Stores pid of debugger/this process
_pid: int

# Stores pid of fork
_child_pid: int

LineCache = DefaultDict[
    Tuple[str, str, int],  # filename, funcname, stacklevel
    List[int],  # list of executed lines
]

logger = logging.getLogger(__name__)

LOCAL_SL = "__py2cfg_stacklevel"

# Cheat sheet on stack frame objects.
# https://docs.python.org/3/library/inspect.html


# --- Server handlers --- #

_cond = threading.Condition()


def new_client(client, server):
    cfg = CFGBuilder().build_from_src("", "")
    _path = cfg.build_visual(
        "key",
        format="svg",
        show=False,
        calls=True,
        cleanup=True,
        directory=os.path.join(os.environ["PY2CFG_SERVE_AT"], "cfg"),
        build_keys=True,
    )
    logger.debug(f"Build key at {_path}")
    server.send_message(
        client,
        json.dumps(
            {"type": "key", "filepath": os.path.join("cfg", "key.svg"),}
        ),
    )

    with _cond:
        _cond.notify_all()


def client_left(client, server):
    # How to gracefully shutdown pudb when browser tab is closed?
    pass


def message_received(client, server, message):
    """Called when SVG link is clicked ?"""


server = WebsocketServer(int(os.environ["PY2CFG_SOCKET_PORT"]))
server.set_fn_new_client(new_client)
server.set_fn_client_left(client_left)
server.set_fn_message_received(message_received)

_entry_frame = None


def _set_entry_frame(frame, name):
    global _entry_frame
    if frame.f_code.co_filename == name and _entry_frame is None:
        _entry_frame = frame
        frame.f_locals[LOCAL_SL] = 0
        with _cond:
            # Wait so a browser can service the request
            _cond.wait_for(lambda: server.clients)
        return 0
    return -1


def _get_stack_level(current_frame):
    assert _entry_frame is not None
    last_visited_frame = None
    frame = current_frame
    delta_sl = 0
    while frame:
        if LOCAL_SL in frame.f_locals:
            last_visited_frame = frame
            break

        frame = frame.f_back
        delta_sl += 1

    frame_sl = delta_sl + last_visited_frame.f_locals[LOCAL_SL]
    frame = current_frame
    while frame and frame_sl:
        if LOCAL_SL not in frame.f_locals:
            frame.f_locals[LOCAL_SL] = frame_sl
        else:
            break
        frame_sl -= 1

    return current_frame.f_locals[LOCAL_SL]


# --- Databases --- #
cfg_db = CFG_Database()


def wrap_user_call(func, entry):
    def user_call(dbg, _frame, argument_list):
        if _pid == os.getpid():
            _set_entry_frame(_frame, entry)

        return func(dbg, _frame, argument_list)

    return user_call


_child_pid = None  # type: ignore


def get_future_id():
    return _child_pid


class ExecData(tuple):
    @property
    def filename(self):
        return self[0]

    @property
    def funcname(self):
        return self[1]

    @property
    def lineno(self):
        return self[2]

    @property
    def event(self):
        return self[3]

    @property
    def stack_level(self):
        return self[4]

    @classmethod
    def create(
        cls,
        filename: str,
        funcname: str,
        lineno: int,
        event: str,
        stacklevel: int,
    ):
        return cls((filename, funcname, lineno, event, stacklevel))

    @classmethod
    def from_frame(cls, frame, event):
        return cls(
            (
                frame.f_code.co_filename,
                frame.f_code.co_name,
                frame.f_lineno,
                event,
                _get_stack_level(frame),
            )
        )


def trace_create(f_id, queue_object):
    def trace(frame, event, args):
        queue_object.put(ExecData.from_frame(frame, event))
        return trace

    return trace


class FrameWrapper:
    def __init__(self, frame, rel=_entry_frame):
        assert _entry_frame is not None
        self._frame = frame
        _get_stack_level(frame)

    @property
    def name(self):
        return self._frame.f_code.co_name

    @property
    def frame(self):
        return self._frame

    @property
    def stack_level(self):
        return self._frame.f_locals[LOCAL_SL]

    @property
    def filename(self):
        return self._frame.f_code.co_filename

    @property
    def lineno(self):
        return self._frame.f_lineno

    def settrace(self, tracefn, stop=None):
        sys.settrace(tracefn)
        frame = self._frame
        while frame is not None:
            frame.f_trace = tracefn
            if frame == stop:
                break
            frame = frame.f_back
        return frame

    _calls_at_line: Dict[
        Tuple[str, int], Optional[bool],
    ] = collections.defaultdict(lambda: None)

    def calls_function(self):
        if (res := self._calls_at_line[self]) is not None:
            return res
        generator = iter(dis.Bytecode(self.frame.f_code))
        instruction = next(generator)
        try:
            while True:
                instruction = next(generator)
                if instruction.starts_line == self.frame.f_lineno:
                    if "CALL" in instruction.opname:
                        self._calls_at_line[self] = True
                        return True
                    while (instruction := next(generator)).starts_line is None:
                        if "CALL" in instruction.opname:
                            self._calls_at_line[self] = True
                            return True
        except StopIteration:
            self._calls_at_line[self] = False
            return False

    def __str__(self):
        frame = self._frame
        string = super().__str__() + "\n"
        while frame is not None:
            string += f"\t{frame.f_code.co_filename}:{frame.f_lineno}\n"
            frame = frame.f_back
        return string

    def __hash__(self):
        return hash((self.frame.f_code.co_filename, self.frame.f_lineno))


class QueueMGR:
    def __init__(self, mp_queue, factory, line_cache: LineCache) -> None:
        self._lock = threading.Lock()
        self._line_cache = line_cache
        self._rx = mp_queue
        self._running = True
        self.thread = threading.Thread(target=self._start_fn, daemon=True)
        self.thread.start()
        self._thread_ident = -1
        self._f_id = factory

        self._requests: Dict[
            Tuple[str, str, int], Union[Tuple[Condition, List[int]], list]
        ] = {}

    def set_thread_ident(self, ident):
        with self._lock:
            self._thread_ident = ident

    def clear_thread_ident(self):
        with self._lock:
            self._thread_ident = -1

    def post(self, key: Tuple[str, str, int]):
        self._requests[key] = [threading.Condition(), None]

    def wait(self, key, timeout=None) -> list:
        assert key in self._requests
        cond = self._requests[key][0]
        with cond:
            cond.wait_for(lambda: self._requests[key][1] is not None, timeout)
            lines = self._requests[key][1]
            del self._requests[key]
        return lines

    def _start_fn(self):
        while self._running:
            try:
                data: ExecData = self._rx.get(timeout=0.1)
            except:
                time.sleep(0.01)
                continue
            else:
                key = data.filename, data.funcname, data.stack_level
                if key in self._requests:
                    cond = self._requests[key][0]
                    with cond:
                        self._requests[key][1] = self._line_cache[key]
                        cond.notify_all()

                if data.event == "call":
                    logger.debug(f"call: {data.funcname}")
                elif data.event == "return":
                    logger.debug(f"return: {data.funcname}")
                    self._line_cache[key] = []

                self._line_cache[key].append(data.lineno)

    def close(self) -> None:
        self._rx.close()
        self._running = False


class ProcessFactory:
    def __new__(
        cls,
        frame: FrameWrapper,
        func: Callable,
        stop: Any,
        continue_fn: Callable = None,
    ):
        ipc = multiprocessing.Queue()  # type: ignore
        cond = multiprocessing.Condition()

        # First fork saves the context of 'frame' before we enter a function
        # at the debugger.
        # TODO Don't fork if there isn't a function call at current line.
        if (factory := os.fork()) == 0:
            pid = os.getpid()
            logger.info(f"Factory {pid} created at level: {frame.stack_level}")
            last_child = -1
            while True:
                # Wait for parent to signal this process.
                os.kill(pid, signal.SIGSTOP)
                time.sleep(0.01)
                child, _ = pty.fork()  # Don't inherit stdin/stdout descriptors
                if child == 0:
                    # Second fork starts execution from saved context. A child
                    # is created on every step. The last child created is killed
                    time.sleep(0.01)
                    # Install trace handlers
                    if continue_fn is not None:
                        continue_fn()

                    trace = trace_create(pid, ipc)
                    return func(frame.settrace(trace, stop))
                else:
                    if last_child != -1:
                        os.kill(last_child, signal.SIGTERM)
                        _, status = os.waitpid(last_child, 0)
                    else:
                        status = -1
                    logger.info(
                        f"\n\tFactory ({pid}) stack level {frame.stack_level}: "
                        f"{frame.filename}:{frame.lineno}"
                        f"\n\t-> Fork: {child}"
                        f"\n\t Kill: {last_child} status: {status}\n"
                    )
                    last_child = child
                    continue
        else:
            cache = defaultdict(list)  # type: ignore
            obj = super().__new__(cls)
            # __init__()
            obj._frame = frame
            obj._pid = factory
            obj._queue = QueueMGR(ipc, factory, cache)
            obj._stack_level = frame.stack_level
            obj._line_cache = cache
            return obj

    def draw_graph(self, frame: FrameWrapper, create_child=True) -> None:
        key = frame.filename, frame.name, frame.stack_level
        if self.line_cache[key]:
            return threading.Thread(
                target=self._draw_graph,
                args=(frame.frame, self.line_cache[key]),
                daemon=True,
            ).start()

        if create_child:
            threading.Thread(
                target=self._draw_graph,
                args=(frame.frame, self.line_cache[key]),
                daemon=True,
            ).start()

            self.queue.post(key)
            os.kill(self.pid, signal.SIGCONT)

            def _start_fn():
                time.sleep(1)
                self.line_cache[key] = lines = self.queue.wait(key)
                last_size = 0
                while (size := len(lines)) != last_size:
                    if threading.current_thread().ident != self.thrd_ident:
                        logger.warn("Thread ident changed. Cancelling build")
                        break
                    last_size = size
                    self._draw_graph(frame.frame, lines)
                    time.sleep(1)

            thrd = threading.Thread(target=_start_fn, daemon=True,)
            thrd.start()
            self.thrd_ident = thrd.ident

    def terminate(self) -> int:
        os.kill(self.pid, signal.SIGTERM)
        os.kill(self.pid, signal.SIGCONT)
        _, status = os.waitpid(self.pid, 0)
        self.queue.close()
        logger.info(
            f"\n\tKill {self.pid}"
            f"\n\tlevel {self.stack_level}"
            f"\n\tstatus {status}"
            f"\n"
        )
        return status

    @property
    def frame(self) -> FrameWrapper:
        return self._frame  # type: ignore

    @property
    def stack_level(self) -> int:
        return self._stack_level  # type: ignore

    @property
    def pid(self) -> int:
        return self._pid  # type: ignore

    @property
    def queue(self) -> QueueMGR:
        return self._queue  # type: ignore

    @property
    def line_cache(self) -> LineCache:
        return self._line_cache  # type: ignore

    nbuild = 0

    def _draw_graph(self, frame, lst):
        name = frame.f_globals["__name__"]
        if frame.f_code.co_name != "<module>":
            name = f"{name}.{frame.f_code.co_name}"

        key = frame.f_code.co_filename, frame.f_code.co_name
        cfg, context_blocks = cfg_db.at_function[key]

        if cfg.outline_block(frame.f_lineno, context_blocks) < 0:
            logger.error(f"Unable to find block at line {frame.f_lineno}")

        cfg.highlight_blocks(lst, context_blocks)
        dispatch_cfg(cfg, f"{name}{self.nbuild}", True)
        self.nbuild += 1


class ProcessStack(collections.deque):
    curr_stack_level: int = 0
    base_factory: ProcessFactory = None  # type: ignore


_process_stack = ProcessStack()


def dispatch_cfg(cfg, name=None, interactive=False):
    name = cfg.name if name is None else name
    try:
        src = cfg.build_visual(
            name,
            format="svg",
            show=False,
            calls=True,
            cleanup=True,
            directory=os.path.join(os.environ["PY2CFG_SERVE_AT"], "cfg"),
            interactive=interactive,
            build_keys=False,
        )
    except:
        logger.warn("Failed to build cfg from source")
    else:
        server.send_message_to_all(
            json.dumps(
                {
                    "type": "cfg",
                    "filepath": os.path.join("cfg", f"{name}.svg"),
                    "layer": 0,
                }
            )
        )
        logger.debug(f"Created at {src}")


def wrap_user_line(func, entry):
    name = os.path.basename(os.path.splitext(entry)[0])

    def user_line(dbg, _frame):
        # Only fork if this is the main debugger process...
        if _pid == os.getpid() and _entry_frame is not None:
            frame = FrameWrapper(_frame)
            if frame.stack_level >= _process_stack.curr_stack_level:
                if (
                    factory := ProcessFactory(
                        frame, functools.partial(func, dbg), dbg.botframe,
                    )
                ) is None:
                    # Continue program execution from caller's stack frame.
                    return

                if frame.stack_level > _process_stack.curr_stack_level:
                    # Entered a function call on step. The factory is forked
                    # if next step enters a higher stack level
                    _process_stack.appendleft(factory)

                elif (
                    _process_stack.curr_stack_level == frame.stack_level
                    and _process_stack[0] is None
                ):
                    _process_stack[0] = factory
                    _process_stack.base_factory = ProcessFactory(
                        frame, functools.partial(func, dbg), dbg.botframe,
                    )
                    if _process_stack.base_factory is None:
                        # Continue program execution from first line of program
                        return

                    cfg = CFGBuilder(short=True).build_from_file(name, entry)
                    cfg_db.index(entry, cfg)

                    try:
                        src = cfg.build_visual(
                            name,
                            format="svg",
                            show=False,
                            calls=True,
                            cleanup=True,
                            directory=os.path.join(
                                os.environ["PY2CFG_SERVE_AT"], "cfg"
                            ),
                            build_keys=False,
                        )
                    except:
                        logger.warn("Failed to build cfg from source")
                    else:
                        server.send_message_to_all(
                            json.dumps(
                                {
                                    "type": "cfg",
                                    "filepath": os.path.join(
                                        "cfg", f"{name}.svg"
                                    ),
                                    "layer": 0,
                                }
                            )
                        )
                        logger.debug(f"Created at {src}")
                    return func(dbg, _frame)

                elif _process_stack.curr_stack_level == frame.stack_level:
                    assert _process_stack[0].pid > 0
                    _process_stack[0].terminate()
                    _process_stack[0] = factory

            elif frame.stack_level < _process_stack.curr_stack_level:
                # Since we can jump back any number of stack frames, clean up
                # all factories at stack levels higher than this one.
                while True:
                    if _process_stack[0].stack_level <= frame.stack_level:
                        break
                    assert _process_stack[0].pid > 0
                    _process_stack[0].terminate()
                    del _process_stack[0]

            if (k := (frame.filename, frame.lineno)) in cfg_db.at_lineno:
                # When stopped at a functionDef statement, generate a
                # cfg with normal styling
                subcfg, _ = cfg_db.at_lineno[k]
                logger.warn(f"{str(subcfg)} @ {frame.filename}:{frame.lineno}")
                threading.Thread(
                    target=dispatch_cfg, args=(subcfg,), daemon=True,
                ).start()

            elif (size := len(_process_stack)) > 1:
                # Fork previous stack frame's factory
                for i in range(1, size):
                    caller = _process_stack[i]
                    if caller.stack_level < frame.stack_level:
                        caller.draw_graph(
                            frame,
                            frame.stack_level > _process_stack.curr_stack_level,
                        )
                        break

            elif _process_stack.curr_stack_level == 0:
                assert _process_stack.base_factory is not None
                _process_stack.base_factory.draw_graph(frame, False)

            _process_stack.curr_stack_level = frame.stack_level
        return func(dbg, _frame)

    return user_line


def wrap_user_return(func, entry):
    def user_return(dbg, frame, return_value):
        if _pid == os.getpid():
            _set_entry_frame(frame, entry)
            if _entry_frame is not None:
                subcfg, blocks = cfg_db.at_function[
                    frame.f_code.co_filename, frame.f_code.co_name
                ]
                if subcfg.outline_block(frame.f_lineno, blocks) < 0:
                    logger.warn(
                        f"Failed to highlight block at {frame.f_lineno}"
                    )
                threading.Thread(
                    target=dispatch_cfg,
                    args=(subcfg, subcfg.name, True),
                    daemon=True,
                ).start()

            logger.debug(f"return: {frame.f_code.co_name}")
        return func(dbg, frame, return_value)

    return user_return


def wrap_user_exception(func, entry):
    def user_exception(dbg, frame, exc_tuple):
        if _pid == os.getpid():
            logger.info(
                f"exception: {frame.f_code.co_filename}:{frame.f_lineno}"
            )
        return func(dbg, frame, exc_tuple)

    return user_exception


class Handler(logging.Handler):
    def __init__(self, server):
        super().__init__()
        self.server = server

    def emit(self, record):
        self.server.send_message_to_all(
            json.dumps(
                {
                    "type": "log",
                    "data": self.format(record),
                    "levelname": record.levelname,
                }
            )
        )


def debug_init(debug_class, entryfile, port=None) -> None:
    global _pid
    port = 8000 if port is None else port
    _pid = os.getpid()
    _process_stack.appendleft(None)

    rootlog = logging.getLogger()

    handler = Handler(server)
    rootlog.addHandler(handler)
    handler.setFormatter(logging.Formatter("%(asctime)s - %(message)s"))
    logger.error("\033[H\033[J")
    logger.setLevel(getattr(logging, os.environ["PY2CFG_LOGLEVEL"], 0))

    # TOP SNEAKY: Swap whatever debugger functions that [DEBUG PROG] uses with
    # our own user_ functions.
    debug_class.user_call = wrap_user_call(debug_class.user_call, entryfile)
    debug_class.user_line = wrap_user_line(debug_class.user_line, entryfile)
    debug_class.user_return = wrap_user_return(
        debug_class.user_return, entryfile
    )
    debug_class.user_exception = wrap_user_exception(
        debug_class.user_exception, entryfile
    )
    threading.Thread(target=server.run_forever, daemon=True,).start()

    try:
        subprocess.Popen(["xdg-open", f"http://localhost:{port}"])
    except OSError:
        print(
            f"Could not start browser. Program will hang unless browser attaches to localhost:{port}"
        )
        return


__all__ = ["debug_init", "module_context", "get_future_id"]
