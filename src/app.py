from PyQt5 import QtWidgets, QtCore
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
        self.showFullScreen()

        self.ui.verticalLayout.setAlignment(QtCore.Qt.AlignCenter)

        self.ui.exit_Button.clicked.connect(self.exit_Button_clicked)
        self.ui.poweroff_Button.clicked.connect(self.poweroffButton_clicked)
        self.ui.TouchScreenTest_Button.clicked.connect(self.TouchScreenTest_Button_clicked)
        self.ui.networkTest_Button.clicked.connect(self.networkTest_Button_clicked)
        self.ui.PrinterTest_button.clicked.connect(self.printerTest_Button_clicked)
    
    #Shuts down the Kiosk
    def poweroffButton_clicked(self):
        os.system('shutdown -P now')
    #Closes the FAT Software
    def exit_Button_clicked(self):
        sys.exit(app.exec_())
    #Opens xinput_calibrator to Test and Calibrate kiosk touch screeen    
    def TouchScreenTest_Button_clicked(self):
        os.system('xinput_calibrator')
    #Opens wifi&ethernet test page    
    def networkTest_Button_clicked(self):
        dialogNetwork = networkTest()
        dialogNetwork.exec_()
    #Opens printer test page    
    def printerTest_Button_clicked(self):
        dialogPrinter = printerTest()
        dialogPrinter.exec_()    
            
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
