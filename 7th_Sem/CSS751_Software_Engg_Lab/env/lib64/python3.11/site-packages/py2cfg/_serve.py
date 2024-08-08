import logging
import os
import contextlib
import http.server
import shutil


logger = logging.getLogger(__name__)
logger.setLevel(1)

SUBDIR = ".py2cfg"
PROTODIR = "_proto_"


@contextlib.contextmanager
def serve_dir(serve_dir):
    # Need a place to host generated control flow graphs/metadata/whatever.

    serve_path = os.path.join(serve_dir, SUBDIR)
    proto = os.path.join(os.path.dirname(__file__), PROTODIR)
    logger.debug(f"Copying prototype at {proto} to {serve_path}")

    if os.path.exists(serve_path):
        shutil.rmtree(serve_path)

    try:
        shutil.copytree(proto, serve_path)
    except OSError:
        logger.exception(f"Failed to copy tree")
        return -1
    try:
        yield serve_path
    finally:
        shutil.rmtree(serve_path)


_pid = None


def set_pid(pid):
    global _pid
    _pid = pid


def get_pid():
    return _pid


def serve(port=None, directory=None, pipe=None) -> None:
    """Serve control flow graph files"""
    rootlog = logging.getLogger()
    rootlog.addHandler((fh := logging.FileHandler("log.txt")))
    fh.setFormatter(logging.Formatter("%(name)s - %(levelname)s - %(message)s"))

    port = 8000 if port is None else port
    directory = os.getenv("HOME") if directory is None else directory

    with serve_dir(directory) as target:

        class Py2CFG_Handler(http.server.SimpleHTTPRequestHandler):
            def __init__(self, *args, **kwargs):
                super().__init__(*args, directory=target, **kwargs)

            # Only works for some browsers. Mangling filename still required
            def end_headers(self):
                # https://gist.github.com/dustingetz/5348582
                self.send_header(
                    "Cache-Control", "no-cache, no-store, must-revalidate",
                )
                self.send_header("Pragma", "no-cache")
                self.send_header("Expires", "0")
                super().end_headers()

        with http.server.HTTPServer(("", port), Py2CFG_Handler) as httpd:
            httpd.serve_forever()
