from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from Ui_printerTest import Ui_Dialog
import os
import sys
from escpos.connections import getUSBPrinter

class printerTest(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(printerTest, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        self.ui.print_button.clicked.connect(self.printerPrint)
        
        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
        print(CURRENT_DIRECTORY)
        filename = os.path.join(CURRENT_DIRECTORY, "../resource/ombori_mini.jpeg")
        self.ui.label.setPixmap(QtGui.QPixmap(filename))    
        
        self.show()
        
    def printerPrint():
        printer = getUSBPrinter()(idVendor=0x04e7,
                          idProduct=0x2902, 
                          inputEndPoint=0x81,
                          outputEndPoint=0x01)

        printer.text('AA11')
        printer.lf()