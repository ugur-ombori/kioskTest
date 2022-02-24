from PyQt5 import QtWidgets, QtCore
from Ui_kiosk import Ui_MainWindow
from networkTest import networkTest
from printerTest import printerTest
from barcodeTest import barcodeTest
from PyQt5.uic import loadUi
import os
import sys
import subprocess
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
        self.ui.BarcodeScanner_button.clicked.connect(self.BarcodeScanner_Button_clicked)
        self.ui.rotate_down_button.clicked.connect(self.rotate_down)
        self.ui.rotate_left_button.clicked.connect(self.rotate_left)
        self.ui.rotate_right_button.clicked.connect(self.rotate_right)
        self.ui.rotate_up_button.clicked.connect(self.rotate_up)
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
    
    def BarcodeScanner_Button_clicked(self):
        barcodeTester = barcodeTest()
        barcodeTester.exec_()  
    
    def rotate_down(self):
        subprocess.run(['/home/ubuntu/kioskTest/rotate.sh','inverted'])
 
    def rotate_left(self):
        subprocess.run(['/home/ubuntu/kioskTest/rotate.sh','left'])

    def rotate_right(self):
        subprocess.run(['/home/ubuntu/kioskTest/rotate.sh','right'])
        
    def rotate_up(self):  
        subprocess.run(['/home/ubuntu/kioskTest/rotate.sh','normal'])
        
if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
