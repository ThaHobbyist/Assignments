import logging
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEvent, RegexMatchingEventHandler
from py2cfg.builder import CFGBuilder
from .util import getcwd, normalizer
from .db import connect, process_source_file, delete_rows

logger = logging.getLogger(__name__)


class FileHandler(RegexMatchingEventHandler):
    def on_modified(self, event: FileSystemEvent):
        src_path = normalizer(event.src_path)
        with connect() as cursor:
            try:
                cfg = CFGBuilder(short=True).build_from_file("", src_path)
            except:
                return
            else:
                delete_rows(src_path, cursor)
                process_source_file(cfg, src_path, cursor)
                logger.warn(f"Modified: {src_path}")

    def on_deleted(self, event):
        src_path = normalizer(event.src_path)
        with connect() as cursor:
            delete_rows(src_path, cursor)
            logger.warn(f"Deleted: {src_path}")


def create_managed_database(
    ignore_regexes=None, ignore_directories=False, case_sensitive=False,
) -> None:
    observer = Observer()
    observer.schedule(
        FileHandler(
            regexes=[r".*\.py$"],
            ignore_regexes=ignore_regexes,
            ignore_directories=ignore_directories,
            case_sensitive=case_sensitive,
        ),
        getcwd(),
        recursive=True,
    )
    observer.start()

    with connect() as cursor:
        for root, path, files in os.walk(getcwd()):
            for file in files:
                if file.endswith(".py"):
                    filepath = os.path.join(root, file)
                    try:
                        cfg = CFGBuilder(short=True).build_from_file(
                            "", filepath
                        )
                    except:
                        logger.error(f"Failed to build cfg {filepath}")
                        continue
                    else:
                        process_source_file(cfg, filepath, cursor)
                        logger.debug(f"Built {filepath}")
