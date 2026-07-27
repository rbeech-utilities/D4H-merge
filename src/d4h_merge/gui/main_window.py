from PySide6.QtWidgets import *
from PySide6.QtGui import QAction
from .settings_dialog import SettingsDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("D4H Merge")
        self.resize(800,600)
        mb=self.menuBar()
        file_menu=mb.addMenu("&File")
        settings_menu=mb.addMenu("&Settings")
        help_menu=mb.addMenu("&Help")
        exit_action=QAction("Exit",self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        settings_action=QAction("Preferences...",self)
        settings_action.triggered.connect(self.show_settings)
        settings_menu.addAction(settings_action)
        help_menu.addAction(QAction("About",self))
        c=QWidget(); self.setCentralWidget(c)
        l=QVBoxLayout(c)
        l.addWidget(QLabel("Task Number(s)"))
        l.addWidget(QPlainTextEdit())
        l.addWidget(QPushButton("Download && Merge"))
        l.addWidget(QLabel("Status"))
        self.log=QTextEdit(); self.log.setReadOnly(True); l.addWidget(self.log)
        self.setStatusBar(QStatusBar())
        self.statusBar().showMessage("Ready")
    def append_log(self,msg): self.log.append(msg)
    def show_settings(self):
        SettingsDialog(self).exec()
