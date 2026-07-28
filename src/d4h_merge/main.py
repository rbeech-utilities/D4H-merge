from __future__ import annotations

import sys

from PySide6.QtWidgets import QApplication

from d4h_merge.config import Config
from d4h_merge.gui.main_window import MainWindow
from d4h_merge.logger import create_logger


def main() -> None:

    app = QApplication(sys.argv)

    logger = create_logger()
    logger.info("Application started.")

    config = Config()

    window = MainWindow(config)

    window.append_log("D4H Merge started.")
    window.append_log(f"Team ID: {config.team_id}")
    window.append_log(f"Subdomain: {config.subdomain}")
    window.append_log("")
    window.append_log("Ready.")

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()