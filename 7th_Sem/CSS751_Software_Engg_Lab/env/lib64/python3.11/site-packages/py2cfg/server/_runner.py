import pickle
from .filewatcher import create_managed_database
from .db import query_filename_lineno, connect
from .util import getcwd
from flask import Flask, abort, request
import logging
import os
import base64

logger = logging.getLogger(__name__)
server = Flask(__name__)
create_managed_database()

REMOTE_CALLS = {}


def remote(func):
    REMOTE_CALLS[func.__name__] = func
    return func


def validate_data(data):
    def resolve(result):
        return {
            "jsonrpc": data["jsonrpc"],
            "id": data["id"],
            "result": result,
        }

    def failure(reason):
        return {
            "jsonrpc": data["jsonrpc"],
            "id": data["id"],
            "error": {"code": 1, "message": reason},
        }

    if data is None:
        return None, None
    if not all(s in data for s in ("jsonrpc", "method", "params", "id")):
        return None, None
    return resolve, failure


def strip_svg_doctype(svgdata: str) -> str:
    lines = svgdata.splitlines(keepends=True)

    def iter_lines():
        found = False
        for line in lines:
            if found:
                yield line
            else:
                if line.startswith("<svg"):
                    found = True
                    yield line

    return "".join(iter_lines())


@server.route("/")
def index():
    return "py2cfg"


@server.route("/build")
def build(method=["GET"]):
    data = request.get_json()
    resolve, failure = validate_data(data)
    if resolve is None:
        abort(400)

    logger.info(f"method: {data['method']}, params: {data['params']}")
    method = data["method"]
    params = data["params"]

    if method not in REMOTE_CALLS:
        abort(400)

    func = REMOTE_CALLS[method]
    return resolve(func(**params))


@remote
def build_graph(
    filename, lineno, build_own=True, build_keys=False, interactive=False
):
    with connect() as cursor:
        cfg, own_blocks = query_filename_lineno(filename, lineno, cursor)
        if interactive:
            cfg.outline_block(lineno, own_blocks)
            cfg.highlight_blocks([lineno], own_blocks)

        path = cfg.build_visual(
            "_tmp_file",
            "svg",
            show=False,
            directory=os.path.join(getcwd(), ".py2cfg"),
            build_own=build_own,
            build_keys=build_keys,
            interactive=interactive,
        )
        with open(path, "r") as fp:
            svg_data = fp.read()

        os.remove(path)
        return strip_svg_doctype(svg_data)


@remote
def build_cfg(filename, lineno):
    with connect() as cursor:
        cfg, _ = query_filename_lineno(filename, lineno, cursor)
        return str(base64.b64encode(pickle.dumps(cfg)), encoding="utf-8")
