from py2cfg.model import Block
import sqlite3
import threading
import os
from typing import List, Tuple
from py2cfg.builder import CFG
import pickle
import logging
import contextlib
import time
from .util import getcwd

logger = logging.getLogger(__name__)


TMPDIR = os.path.join(getcwd(), ".py2cfg")
DB_FILE = os.path.join(getcwd(), ".py2cfg", "cfg.db")
UPDATE_LOCK = threading.Condition()


def _sql_init():
    if not os.path.exists(DB_FILE):
        # Server initiated in new directory so define schema (?)
        cursor = sqlite3.connect(os.path.join(TMPDIR, "cfg.db")).cursor()
        cursor.execute(
            r"""
            CREATE TABLE Files (
                qualname TEXT,
                filepath TEXT,
                lineno INT,
                end_lineno INT,
                PRIMARY KEY (qualname),
                FOREIGN KEY (filepath) REFERENCES Data(filepath)  
            )
            """,
        )
        cursor.execute(
            r"""
                CREATE TABLE Data (
                    filepath TEXT NOT NULL,  
                    data BLOB,
                    PRIMARY KEY (filepath)
                )
            """,
        )

    return sqlite3.connect(
        os.path.join(TMPDIR, "cfg.db"),
        isolation_level="IMMEDIATE",
        cached_statements=0,
    )


@contextlib.contextmanager
def connect() -> sqlite3.Cursor:
    with UPDATE_LOCK:
        conn = _sql_init()
        try:
            yield conn.cursor()
        finally:
            conn.commit()
            # It seems that sqlite is not MT-Safe so wait for all transactions
            # to finalize.
            while conn.in_transaction:
                time.sleep(0.01)
            conn.close()


sortblocks = lambda cfg: list(sorted(cfg.own_blocks(), key=lambda x: x.at()))


def process_source_file(cfg: CFG, filepath, cursor: sqlite3.Cursor):
    fields = set()

    def set_qualname(cfg: CFG, qualname: str):
        classgraph: CFG
        funcgraph: CFG
        for classgraph in cfg.classcfgs.values():
            classgraph.qualname = f"{qualname}.{classgraph.name}"
            set_qualname(classgraph, classgraph.qualname)
            fields.add(
                (classgraph.qualname, classgraph.lineno, classgraph.end_lineno,)
            )

        for funcgraph in cfg.functioncfgs.values():
            funcgraph.qualname = f"{qualname}.{funcgraph.name}"
            set_qualname(funcgraph, funcgraph.qualname)
            fields.add(
                (funcgraph.qualname, funcgraph.lineno, funcgraph.end_lineno,)
            )

    relpath = os.path.relpath(filepath)
    cfg.qualname = f"<{relpath}>"
    set_qualname(cfg, f"<{relpath}>")
    fields.add((f"<{relpath}>", cfg.lineno, cfg.end_lineno,))
    for qualname, lineno, end_lineno in fields:
        cursor.execute(
            r"""
                INSERT INTO Files (
                    qualname,
                    filepath,
                    lineno,
                    end_lineno
                ) VALUES (
                    ?, ?, ?, ?
                ) ON CONFLICT(qualname) DO
                UPDATE SET lineno=?, end_lineno=?, filepath=?
            """,
            [
                qualname,
                lineno,
                end_lineno,
                filepath,
                lineno,
                end_lineno,
                filepath,
            ],
        )
    data = pickle.dumps(cfg)
    cursor.execute(
        r"""
            INSERT INTO Data (
                filepath,
                data
            ) Values (
                ?, ?
            ) ON CONFLICT(filepath) DO
            UPDATE SET data=?
        """,
        [filepath, data, data],
    )

    for (qualname, lineno, end_lineno,) in fields:
        print_this = "{a:50}, {b:>3}, {c:>3},".format(
            a=qualname, b=lineno, c=end_lineno,
        )
        logger.debug(print_this)


def query_filename_lineno(
    filename: str, lineno: int, cursor: sqlite3.Cursor,
) -> Tuple[CFG, List[Block]]:

    cursor.execute(
        r"""
            SELECT files.qualname, data.data, files.lineno, files.end_lineno
            FROM files
            INNER JOIN data ON files.filepath=data.filepath
            WHERE files.filepath=? AND
                lineno<=? AND
                end_lineno>=?
    """,
        (filename, lineno, lineno),
    )

    # Which enclosing scope is the mostest-closest?
    def distance(start, end, lineno):
        start_dist, end_dist = abs(lineno - start), abs(lineno - end)
        return (start_dist + end_dist) / 2

    qualname: str
    cfg: CFG
    selected = cursor.fetchall()
    if not selected:
        raise Exception(f"{filename} not found in database")

    qualname, blob, _, _ = min(
        selected, key=lambda item: distance(item[2], item[3], lineno)
    )
    cfg = pickle.loads(blob)  # Possibly dangerous
    module_qual = f"<{os.path.relpath(filename)}>"
    qualname = qualname.replace(module_qual, "")
    if not qualname:
        return cfg, sortblocks(cfg)

    # Traverse path until we find the mostest-closest enclosing scope
    subcfg_path = qualname.split(".")[1:]
    while subcfg_path:
        name = subcfg_path.pop(0)
        if name in cfg.classcfgs:
            cfg = cfg.classcfgs[name]
        elif name in cfg.functioncfgs:
            cfg = cfg.functioncfgs[name]
        else:
            raise Exception("Reached supposedly unreachable code")

    return cfg, sortblocks(cfg)


def delete_rows(filepath, cursor: sqlite3.Cursor):
    cursor.execute(
        r"""
        DELETE FROM data
        WHERE filepath=?
    """,
        [filepath],
    )
    cursor.execute(
        r"""
        DELETE FROM files
        WHERE filepath=?
    """,
        [filepath],
    )
