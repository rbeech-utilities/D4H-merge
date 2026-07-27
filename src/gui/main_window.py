from __future__ import annotations
from PySide6.QtWidgets import *
from PySide6.QtGui import QAction

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("D4H Merge")
        self.resize(800,600)
        mb=QMenuBar(self)
        self.setMenuBar(mb)
        fm=mb.addMenu("&File")
        sm=mb.addMenu("&Settings")
        hm=mb.addMenu("&Help")
        exit_action=QAction("E&xit",self)
        exit_action.triggered.connect(self.close)
        fm.addAction(exit_action)
        sm.addAction(QAction("&Preferences...",self))
        hm.addAction(QAction("&About",self))
        c=QWidget()
        self.setCentralWidget(c)
        l=QVBoxLayout(c)
        l.addWidget(QLabel("Task Number(s)"))
        self.task_numbers=QPlainTextEdit()
        l.addWidget(self.task_numbers)
        self.download_button=QPushButton("Download && Merge")
        l.addWidget(self.download_button)
        l.addWidget(QLabel("Status"))
        self.log=QTextEdit()
        self.log.setReadOnly(True)
        l.addWidget(self.log)
        self.setStatusBar(QStatusBar())
        self.statusBar().showMessage("Ready")
    def append_log(self,msg:str):
        self.log.append(msg)
