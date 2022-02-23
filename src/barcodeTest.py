from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from Ui_barcodeTest import Ui_Dialog
import os
import sys
from PyQt5.QtWidgets import QMessageBox
from Ui_barcodeConfigure import Ui_Dialog as Ui_Dialog_2

class barcodeTest(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(barcodeTest, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        self.CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
        print(self.CURRENT_DIRECTORY)
        filename = os.path.join(self.CURRENT_DIRECTORY, "../resource/ombori_mini.jpeg")
        self.ui.label.setPixmap(QtGui.QPixmap(filename))  

        self.ui.BarcodeScannerConfigure_button.clicked.connect(self.barcodeConfigure)
        
        self.show()

    def barcodeConfigure(self):
        dialogPrinter = barcodeConfigure()
        dialogPrinter.exec_()
        
class barcodeConfigure(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(barcodeConfigure, self).__init__()
        self.ui = Ui_Dialog_2()
        self.ui.setupUi(self)
        
        self.CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
        print(self.CURRENT_DIRECTORY)
        filename = os.path.join(self.CURRENT_DIRECTORY, "../resource/Configurator2.png")
        self.ui.label_5.setPixmap(QtGui.QPixmap(filename))  
        
        self.show()