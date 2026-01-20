from PyQt6 import uic
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QDialog


class Aboutdialog(QDialog):
    onAcceptSignal = pyqtSignal(int, int, int, int)

    def __init__(self):
        super().__init__()
        uic.loadUi("./ui/aboutdialog.ui", self)
        self.pixmap = QPixmap('./ui/ABOUT.png')
        self.imagelabel.setPixmap(self.pixmap)
