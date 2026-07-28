from __future__ import annotations

from PySide6.QtGui import QAction
from PySide6.QtWidgets import (
    QLabel,
    QMainWindow,
    QMenuBar,
    QMessageBox,
    QPlainTextEdit,
    QPushButton,
    QStatusBar,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

from d4h_merge.config import Config
from d4h_merge.gui.settings_dialog import SettingsDialog


class MainWindow(QMainWindow):

    def __init__(self, config: Config):

        super().__init__()

        self.config = config

        self.setWindowTitle("D4H Merge")

        self.resize(800, 600)

        self.build_menu()

        self.build_ui()

    def build_menu(self):

        menu = QMenuBar(self)

        self.setMenuBar(menu)

        file_menu = menu.addMenu("&File")

        settings_menu = menu.addMenu("&Settings")

        help_menu = menu.addMenu("&Help")

        exit_action = QAction("E&xit", self)

        exit_action.triggered.connect(self.close)

        settings_action = QAction("&Preferences...", self)

        settings_action.triggered.connect(
            self.open_settings
        )

        about_action = QAction("&About", self)

        about_action.triggered.connect(
            self.about
        )

        file_menu.addAction(exit_action)

        settings_menu.addAction(settings_action)

        help_menu.addAction(about_action)

    def build_ui(self):

        central = QWidget()

        self.setCentralWidget(central)

        layout = QVBoxLayout(central)

        layout.addWidget(QLabel("Task Number(s)"))

        self.task_numbers = QPlainTextEdit()

        self.task_numbers.setPlaceholderText(
            "Enter one task number per line.\n\n"
            "26-00001\n"
            "26-00002"
        )

        layout.addWidget(self.task_numbers)

        self.download_button = QPushButton(
            "Download && Merge"
        )

        layout.addWidget(self.download_button)

        layout.addWidget(QLabel("Status"))

        self.log = QTextEdit()

        self.log.setReadOnly(True)

        layout.addWidget(self.log)

        self.setStatusBar(QStatusBar())

        self.statusBar().showMessage("Ready")

    def append_log(self, message: str):

        self.log.append(message)

    def open_settings(self):

        dialog = SettingsDialog(
            self.config,
            self,
        )

        if dialog.exec():

            self.append_log(
                "Settings updated."
            )

    def about(self):

        QMessageBox.about(
            self,
            "About D4H Merge",
            (
                "D4H Merge\n\n"
                "Version 1.0 (Development)\n\n"
                "Downloads and merges D4H Team Manager "
                "incident PDFs."
            ),
        )