from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from Ui_printerTest import Ui_Dialog
import os
import sys

class printerTest(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(printerTest, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        #self.ui.ConnectionCheck_button.clicked.connect(self.checkConnection)
        
        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
        print(CURRENT_DIRECTORY)
        filename = os.path.join(CURRENT_DIRECTORY, "../resource/ombori_mini.jpeg")
        self.ui.label.setPixmap(QtGui.QPixmap(filename))    
        
        self.show()
    