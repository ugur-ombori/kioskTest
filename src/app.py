from PyQt5 import QtWidgets
from Ui_kiosk import Ui_MainWindow
from networkTest import networkTest
from printerTest import printerTest
from PyQt5.uic import loadUi
import os
import sys

from printerTest import printerTest




class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #self.showFullScreen()

        
        self.ui.exit_Button.clicked.connect(self.exit_Button_clicked)
        self.ui.poweroff_Button.clicked.connect(self.poweroffButton_clicked)
        self.ui.TouchScreenTest_Button.clicked.connect(self.TouchScreenTest_Button_clicked)
        self.ui.networkTest_Button.clicked.connect(self.networkTest_Button_clicked)
        self.ui.PrinterTest_button.clicked.connect(self.printerTest_Button_clicked)
    def poweroffButton_clicked(self):
        os.system('shutdown -P now')
    
    def exit_Button_clicked(self):
        sys.exit(app.exec_())
        
    def TouchScreenTest_Button_clicked(self):
        os.system('xinput_calibrator')
        
    def networkTest_Button_clicked(self):
        dialogNetwork = networkTest()
        dialogNetwork.exec_()
        
    def printerTest_Button_clicked(self):
        dialogPrinter = printerTest()
        dialogPrinter.exec_()    
            
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
