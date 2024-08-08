from collections import defaultdict
from py2cfg.model import Block, CFG
from typing import Dict, Tuple, List


class _Database:
    def __init__(self):
        self.__dict__ = defaultdict(dict)


F_lineno = Tuple[str, int]  # filename, lineno
F_function = Tuple[str, str]  # filename, funcname
CFG_Blocks = Tuple[CFG, List[Block]]


class CFG_Database(_Database):
    """Database of CFG Indices"""

    def has_file(self, filename):
        return filename in set(f[0] for f in self.__dict__.keys())

    def index(self, filename, cfg: CFG):
        assert not self.has_file(filename)
        sortblocks = lambda cfg: list(
            sorted(cfg.own_blocks(), key=lambda x: x.at())
        )
        topcfg = cfg, sortblocks(cfg)
        if not cfg.entryblock:
            raise TypeError("Expecting cfg.entryblock to be not None")
        self.at_lineno[filename, cfg.entryblock.at()] = topcfg
        self.at_function[filename, "<module>"] = topcfg

        for funcgraph in cfg.functioncfgs.values():
            subcfg = funcgraph, sortblocks(funcgraph)
            self.at_lineno[filename, funcgraph.lineno] = subcfg
            self.at_function[filename, funcgraph.name] = subcfg

        for classgraph in cfg.classcfgs.values():
            pass

    @property
    def at_lineno(self) -> Dict[F_lineno, CFG_Blocks]:
        """A mapping indexed by lineno of function def"""
        return self.__dict__["_lineno"]  # type: ignore

    @property
    def at_function(self) -> Dict[F_function, CFG_Blocks]:
        """A mapping indexed by name of function"""
        return self.__dict__["_function"]  # type: ignore
