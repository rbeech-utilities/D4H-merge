from PySide6.QtWidgets import (
    QDialog,QFormLayout,QLineEdit,QPushButton,QDialogButtonBox,
    QFileDialog,QHBoxLayout,QWidget
)

class SettingsDialog(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("Settings")
        layout=QFormLayout(self)

        self.api_token=QLineEdit()
        self.api_token.setEchoMode(QLineEdit.Password)

        self.team_id=QLineEdit("426")
        self.subdomain=QLineEdit("rosslandsar")
        self.report_order=QLineEdit("4,5,3")

        folder_widget=QWidget()
        h=QHBoxLayout(folder_widget)
        h.setContentsMargins(0,0,0,0)
        self.output_folder=QLineEdit()
        browse=QPushButton("Browse...")
        browse.clicked.connect(self.browse_folder)
        h.addWidget(self.output_folder)
        h.addWidget(browse)

        layout.addRow("API Token",self.api_token)
        layout.addRow("Team ID",self.team_id)
        layout.addRow("Subdomain",self.subdomain)
        layout.addRow("Report Order",self.report_order)
        layout.addRow("Output Folder",folder_widget)

        buttons=QDialogButtonBox(QDialogButtonBox.Save|QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addRow(buttons)

    def browse_folder(self):
        folder=QFileDialog.getExistingDirectory(self,"Select Output Folder")
        if folder:
            self.output_folder.setText(folder)
