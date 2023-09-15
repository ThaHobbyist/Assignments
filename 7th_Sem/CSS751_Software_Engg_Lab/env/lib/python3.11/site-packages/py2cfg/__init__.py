#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Just the init!
"""
from . import server
from .builder import CFG, CFGBuilder
import requests
import base64
import os
import pickle
import functools


@functools.singledispatch  # Overload +0
def request_cfg(
    relpath: str, lineno: int, hostname="localhost", port=5000
) -> CFG:
    """
    Request a CFG object from server.
        Overload +0:
            Args:
                relpath (str): Path to python source file relative to server's directory
                lineno: (int): Line number of the desired CFG
            Returns:
                CFG near lineno
        Overload +1:
            Args:
                cfgptr (list): Non-zero length list that stores the CFG
            Returns: A decorator for the desired CFG object
    """
    body = {
        "jsonrpc": "2.0",
        "method": "build_cfg",
        "params": {
            "filename": os.path.join(os.getcwd(), relpath),
            "lineno": lineno,
        },
        "id": 0,
    }

    req = requests.get(f"http://{hostname}:{port}/build", json=body)
    if req.status_code != 200:
        raise Exception(f"Received {req.status_code}")

    res: dict = req.json()["result"]
    if res["error"]:
        raise Exception(f"{res['data']}")
    return pickle.loads(base64.b64decode(res["data"].encode()))


@request_cfg.register  # Overload +1
def _(cfgptr: list, hostname="localhost", port=5000):
    def f(func):
        code = func.__code__
        cfgptr[0] = request_cfg(
            code.co_filename, code.co_firstlineno + 1, hostname, port
        )

        @functools.wraps(func)
        def g(*args, **kwargs):
            return func(*args, **kwargs)

        return g

    return f


__all__ = [
    "server",
    "CFG",
    "CFGBuilder",
    "request_cfg",
]
