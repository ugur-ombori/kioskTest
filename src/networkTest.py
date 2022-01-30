from sqlite3 import connect
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from Ui_networkTest import Ui_Dialog
import os
import sys
import urllib.request
import socket
import speedtest
import threading

class networkTest(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(networkTest, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.ConnectionCheck_button.clicked.connect(self.checkConnection)
        
        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
        print(CURRENT_DIRECTORY)
        filename = os.path.join(CURRENT_DIRECTORY, "../resource/ombori_mini.jpeg")
        self.ui.label.setPixmap(QtGui.QPixmap(filename))    
        
        self.checkConnection()
        self.show()
    
    def checkConnection(self):
        connection = self.connect()
        if connection == True:
            IPaddress=socket.gethostbyname(socket.gethostname())
            self.ui.Ip_label.setText("Ip: " +IPaddress)
            
            self.ui.InternetOutput_label.setStyleSheet("color: rgb(115, 210, 22);")
            self.ui.InternetOutput_label.setText("Internet Connected")
            
            self.ui.speed_label.setText("Testing...\n \
            Download: Calculating.. \n \
            Upload  : Calculating..")
            
            self.speedTestProcess = threading.Thread(target=self.speedTestCalculate)
            if self.speedTestProcess.is_alive():
                print("Thread Alive")
                self.ui.speed_label.setText("Wait for current test End!\n \
                Download: Calculating.. \n \
                Upload  : Calculating..")
            else:
                self.speedTestProcess.start()
                
                
                
            
        else:
            self.ui.Ip_label.setText("Ip: -" )
            
            self.ui.InternetOutput_label.setStyleSheet("color: rgb(239, 41, 41);")
            self.ui.InternetOutput_label.setText("Internet Not Connected")
    
    def speedTestCalculate(self):
        speed = speedtest.Speedtest()
        print("basladi")
        download = speed.download()/1024/1024
        self.ui.speed_label.setText("Testing...\n \
        Download: {:.2f}Mb/s  \n \
        Upload  : Calculating..".format(download))
        
        upload = speed.upload()/1024/1024
        self.ui.speed_label.setText("Tested.\n \
        Download: {:.2f}Mb/s  \n \
        Upload  : {:.2f}Mb/s".format(download,upload)) 
        
        print("bitti")
               
    def connect(self, host='http://google.com'):
        try:
            urllib.request.urlopen(host) #Python 3.x
            return True
        except:
            return False