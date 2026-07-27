from PySide6.QtWidgets import QApplication,QMessageBox
import sys

def main():
 app=QApplication(sys.argv); QMessageBox.information(None,"D4H Merge","Project skeleton is working."); sys.exit(app.exec())

if __name__=="__main__": main()
