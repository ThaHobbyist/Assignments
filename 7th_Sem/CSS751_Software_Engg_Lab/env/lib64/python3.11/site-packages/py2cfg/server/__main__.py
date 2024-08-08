#! /usr/bin/python3.8
import logging, logging.handlers, logging.config
import os
import subprocess
import argparse
from .util import getcwd

parser = argparse.ArgumentParser()
runner_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "_runner.py"
)
parser.add_argument("host", nargs="?", type=str, default="localhost")
parser.add_argument("port", nargs="?", type=str, default="5000")

parser.add_argument("--directory", type=str, default=".")
parser.add_argument(
    "--logconf-port", type=int, default=8123,
)
args = parser.parse_args()
if not os.path.exists(args.directory):
    raise OSError(f"directory {args.directory} does not exist")
else:
    print(f"Running at {os.path.abspath(args.directory)}")
    os.chdir(args.directory)

if not os.path.exists(tmpdir := os.path.join(getcwd(), ".py2cfg")):
    os.mkdir(tmpdir)

logging.config.listen(args.logconf_port).start()
os.environ["FLASK_APP"] = runner_path
subprocess.call(["flask", "run", "-h", args.host, "-p", args.port])
