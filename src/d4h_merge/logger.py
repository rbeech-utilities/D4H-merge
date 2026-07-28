from __future__ import annotations

import logging
import os
from pathlib import Path


def create_logger() -> logging.Logger:
    """
    Create and configure the application logger.
    """

    logger = logging.getLogger("d4h_merge")

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    appdata = Path(
        os.environ.get(
            "APPDATA",
            str(Path.home() / "AppData" / "Roaming"),
        )
    )

    log_folder = appdata / "D4H Merge"
    log_folder.mkdir(parents=True, exist_ok=True)

    log_file = log_folder / "d4h_merge.log"

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    file_handler = logging.FileHandler(
        log_file,
        encoding="utf-8",
    )

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    return logger