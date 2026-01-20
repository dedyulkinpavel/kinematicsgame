from PyQt6.QtCore import pyqtSignal

from PyQt6 import uic
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QDialog, QColorDialog

import ColorUtils


class EditPMObject(QDialog):
    onAcceptSignal = pyqtSignal(int, int, int, int, int)

    def __init__(self):
        super().__init__()
        self.color = None
        uic.loadUi("./ui/add_edit_pmobject.ui", self)

        color = QColor()
        color.setRed(255)


        self.set_color(color)
        self.colorLabel.setFixedHeight(50)

        self.accepted.connect(self.on_accepted)
        self.colorButton.clicked.connect(self.on_selColor)

    def on_accepted(self):
        self.onAcceptSignal.emit(self.pmXspinBox.value(), self.pmYspinBox.value(), self.pmFXspinBox.value(),
                                 self.pmFYspinBox.value(), self.color)

    def on_selColor(self):

        color = QColorDialog.getColor()
        if color.isValid():
            self.set_color(color)

    def set_color(self, color: QColor | None):
        self.color = ColorUtils.rgb_to_int(color.red(), color.green(), color.blue())
        color_str = ColorUtils.to_str(self.color)
        self.colorLabel.setStyleSheet(f'background-color: {color.name()}; border: 1px solid black;')
        self.colorLabel.setText(f'{color_str}')
