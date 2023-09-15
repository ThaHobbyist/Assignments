#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This is the wrapper that provides/is the py2cfg shell script.
"""

import os
import sys
import argparse
import pty

# Relative and absolute version of the same thing for interpreter tolerance
sys.path.append("..")
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# can be either pip or local relative dir
from py2cfg.builder import CFGBuilder  # type: ignore


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate the control flow graph of a Python program"
    )
    parser.add_argument(
        "input_file",
        help="Path to a file containing a Python program for which the CFG must be generated",
    )
    parser.add_argument(
        "--short",
        action="store_true",
        help="Shorten all strings above 20 characters",
    )
    parser.add_argument(
        "--format",
        type=str,
        default="svg",
        help="File format of the generated cfg",
    )
    parser.add_argument(
        "--calls", nargs=1, type=bool, default=True, help="Toggle call graph"
    )
    parser.add_argument(
        "--show",
        nargs=1,
        type=bool,
        default=False,
        help="Open CFG after generation",
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        default=False,
        help="Generate graphs at run time",
    )
    parser.add_argument(
        "--port", type=int, help="Serve at localhost:port", default=8000,
    )
    parser.add_argument(
        "--wsport", type=int, help="Socket port",
    )
    parser.add_argument(
        "--serve-at",
        type=str,
        help="Host language server here",
        default=os.path.join(os.environ["HOME"]),
    )
    parser.add_argument(
        "--cleanup", action="store_true", help="Remove DOT file"
    )
    parser.add_argument(
        "--pack", type=bool, default=True, help="Generate compact graph"
    )
    parser.add_argument(
        "--level",
        type=str,
        default="WARN",
        choices=["DEBUG", "INFO", "WARN", "CRITICAL", "ERROR",],
    )
    parser.add_argument(
        "--diffable", type=str, help="generate diffable ast traversal"
    )
    args = parser.parse_args()
    os.environ["PY2CFG_SERVER_PORT"] = str(
        8000 if args.port is None else args.port
    )

    os.environ["PY2CFG_SOCKET_PORT"] = str(
        args.port + 1 if args.wsport is None else args.wsport
    )
    os.environ["PY2CFG_PACK"] = str(args.pack)
    os.environ["PY2CFG_SERVE_AT"] = args.serve_at
    os.environ["PY2CFG_CLEANUP"] = str(args.cleanup)
    os.environ["PY2CFG_LOGLEVEL"] = args.level
    cfg_name = args.input_file.split("/")[-1]

    # Run py2cfg interactively along side a debugger.
    if args.debug:
        try:
            from pudb.debugger import Debugger  # type: ignore
            from pudb.run import main as pudb_main  # type: ignore
        except:
            # Once we have a working implementation creating a Spyder plugin should be ez-pz.
            print("pudb not found :(")
            exit(1)

        if not os.path.exists(args.input_file):
            raise OSError("File not found")
        os.environ["PY2CFG_SERVE_AT"] = os.path.join(args.serve_at, ".py2cfg")
        if not os.path.exists(args.serve_at):
            raise OSError("Server directory does not exist")

        if (child := pty.fork()[0]) == 0:
            # Create an http server that serves control flow graph files. Whenever
            # the program is paused, generate a new py2cfg file and notify the
            # browser script.
            from py2cfg._serve import serve

            serve(args.port)
        else:
            from py2cfg._debug_hooks import debug_init
            from py2cfg._serve import set_pid

            set_pid(child)  # child is deleted from global namespace later
            debug_init(Debugger, args.input_file, args.port)
            # What to do about command line args? Use a positional argument as
            # as a toggle?

            # Just create a graph for examples/fib.py
            # $ py2cfg graph [FILE] [--show {True, False}]...

            # Run in debug mode
            # $ py2cfg debug examples/fib.py [--arg [FOO]]
            pudb_main()
            # pudb wipes global variables so we have to import everything
            # without upsetting the parser.
            from os import kill
            from os import getpid
            from signal import SIGINT, SIGTERM
            from py2cfg._serve import get_pid
            from py2cfg._debug_hooks import get_future_id

            if get_future_id() is not None:
                kill(get_future_id(), SIGTERM)
            kill(get_pid(), SIGINT)
            return

    cfg = CFGBuilder(args.short).build_from_file(cfg_name, args.input_file)

    # Some options for wrapping:
    # cfg.build_visual(cfg_name[:-3] + '_cfg', format='pdf', calls=True)
    # cfg.build_visual(cfg_name[:-3] + "_cfg", format="svg", calls=True, show=False)
    # cfg.build_visual(cfg_name[:-3] + "_cfg", format="png", calls=True, show=False)
    # cfg.build_visual('controlflowgraph', format='png', calls=True, show=False)
    cfg.build_visual(
        cfg_name[:-3] + "_cfg",
        format=args.format,
        calls=args.calls,
        show=args.show,
        diffable=args.diffable,
    )


if __name__ == "__main__":
    main()
