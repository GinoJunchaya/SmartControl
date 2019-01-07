from PyQt5.QtWidgets import *

class Popup:
    def __init__(self):
        self.popup = QMessageBox()
    
    def showCriticalBasic(self, message):
        self.popup.setIcon(QMessageBox.Critical)
        self.popup.setText(message)
        self.popup.setWindowTitle(message)
        self.popup.setStandardButtons(QMessageBox.Ok)
        self.popup.exec_()        

    