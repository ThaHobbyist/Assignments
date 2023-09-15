# Since the VM's at MST uses a distributed file system, multiple paths may refer
# to the same directory. For example
# /usr/local/.../<SSO>/home
# /mnt/dfs/.../<SSO>/linuxhome
# Both refer to the same directory. For reasons quite literally beyond the scope
# of just py2cfg, we need the /usr/local version
import os
from typing import Callable


def _is_dfs() -> bool:
    # on dfs, os.getcwd() will always return the /mnt/dfs directory
    curdir = os.getcwd()
    homedir = os.environ[
        "HOME"
    ]  # but the environment variable will still refer
    # to /usr/local

    # Even if we explicitly chdir to homedir...
    os.chdir(homedir)
    testdir = os.getcwd()  # Still returns /mnt directory.
    result = not testdir == homedir
    os.chdir(curdir)
    return result


def _normal_path() -> Callable[[str], str]:
    curdir = os.getcwd()
    os.chdir(os.environ["HOME"])
    dfs_home = os.getcwd()
    os.chdir(curdir)

    def normalizer(path):
        return path.replace(dfs_home, os.environ["HOME"])

    return normalizer


# Don't change the path if we're not on MST's VM.
normalizer = _normal_path() if _is_dfs() else lambda path: path
getcwd = lambda: normalizer(os.getcwd())
