from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from Ui_barcodeTest import Ui_Dialog
import os
import sys

class barcodeTest(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(barcodeTest, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
        print(CURRENT_DIRECTORY)
        filename = os.path.join(CURRENT_DIRECTORY, "../resource/ombori_mini.jpeg")
        self.ui.label.setPixmap(QtGui.QPixmap(filename))  

        self.show()
