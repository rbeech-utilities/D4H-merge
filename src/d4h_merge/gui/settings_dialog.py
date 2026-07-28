from __future__ import annotations

from pathlib import Path

from PySide6.QtWidgets import (
    QFileDialog,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QHBoxLayout,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QWidget,
)

from d4h_merge.config import Config


class SettingsDialog(QDialog):

    def __init__(self, config: Config, parent=None):

        super().__init__(parent)

        self.config = config

        self.setWindowTitle("Settings")

        layout = QFormLayout(self)

        self.api_token = QLineEdit()
        self.api_token.setEchoMode(QLineEdit.Password)

        self.team_id = QLineEdit()

        self.subdomain = QLineEdit()

        self.report_order = QLineEdit()

        self.output_folder = QLineEdit()

        browse = QPushButton("Browse...")

        browse.clicked.connect(self.browse_folder)

        folder = QWidget()

        folder_layout = QHBoxLayout(folder)

        folder_layout.setContentsMargins(0, 0, 0, 0)

        folder_layout.addWidget(self.output_folder)

        folder_layout.addWidget(browse)

        layout.addRow("API Token", self.api_token)
        layout.addRow("Team ID", self.team_id)
        layout.addRow("Subdomain", self.subdomain)
        layout.addRow("Report Order", self.report_order)
        layout.addRow("Output Folder", folder)

        buttons = QDialogButtonBox(
            QDialogButtonBox.Save | QDialogButtonBox.Cancel
        )

        buttons.accepted.connect(self.save)

        buttons.rejected.connect(self.reject)

        layout.addRow(buttons)

        self.load()

    def load(self):

        self.api_token.setText(self.config.api_token)

        self.team_id.setText(str(self.config.team_id))

        self.subdomain.setText(self.config.subdomain)

        self.report_order.setText(
            ",".join(str(x) for x in self.config.report_order)
        )

        self.output_folder.setText(
            self.config.output_folder
        )

    def browse_folder(self):

        folder = QFileDialog.getExistingDirectory(
            self,
            "Output Folder",
            self.output_folder.text(),
        )

        if folder:

            self.output_folder.setText(folder)

    def save(self):

        try:

            self.config.team_id = int(
                self.team_id.text()
            )

            reports = [
                int(x.strip())
                for x in self.report_order.text().split(",")
            ]

            self.config.report_order = reports

            self.config.api_token = self.api_token.text().strip()

            self.config.subdomain = (
                self.subdomain.text().strip()
            )

            self.config.output_folder = (
                self.output_folder.text().strip()
            )

            self.config.save()

            self.accept()

        except Exception as ex:

            QMessageBox.critical(
                self,
                "Invalid Settings",
                str(ex),
            )