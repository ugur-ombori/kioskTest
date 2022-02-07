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
import wifi

class networkTest(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(networkTest, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        self.ui.ConnectionCheck_button.clicked.connect(self.checkConnection)
        self.ui.wifiConnect_button.clicked.connect(self.Connect)
        
        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
        print(CURRENT_DIRECTORY)
        filename = os.path.join(CURRENT_DIRECTORY, "../resource/ombori_mini.jpeg")
        self.ui.label.setPixmap(QtGui.QPixmap(filename))    
        
        
                
        self.checkConnection()
        self.show()
        
        #Create a separete thread. Without seperate thread page will freeze and wait untill all wifi's found (around 10sec)
        self.wifiScan = threading.Thread(target=self.Search)
        #Start wifi scan
        self.wifiScan.start()
    
    #Checks, does internet connection exist? if exists check the upload and download speed
    def checkConnection(self):
        connection = self.connectTest()
        if connection == True:
            IPaddress=socket.gethostbyname(socket.gethostname())
            self.ui.Ip_label.setText("Ip: " +IPaddress)
            
            self.ui.InternetOutput_label.setStyleSheet("color: rgb(115, 210, 22);")
            self.ui.InternetOutput_label.setText("Internet Connected")
            
            self.ui.speed_label.setText("Testing...\n \
            Download: Calculating.. \n \
            Upload  : Calculating..")
            #Create a separete thread. Without seperate thread page will freeze and wait untill connection speed test ends (around 45sec)
            self.speedTestProcess = threading.Thread(target=self.speedTestCalculate)
            if self.speedTestProcess.is_alive():
                print("Thread Alive")
                self.ui.speed_label.setText("Wait for current test End!\n \
                Download: Calculating.. \n \
                Upload  : Calculating..")
            else:
                #Starts the speed test Thread
                self.speedTestProcess.start()
        else:
            
            self.ui.Ip_label.setText("Ip: -" )
            
            self.ui.InternetOutput_label.setStyleSheet("color: rgb(239, 41, 41);")
            self.ui.InternetOutput_label.setText("Internet Not Connected")
    
    #Tests upload and download speed of connection
    def speedTestCalculate(self):
        speed = speedtest.Speedtest()
        print("started")
        download = speed.download()/1024/1024
        self.ui.speed_label.setText("Testing...\n \
        Download: {:.2f}Mb/s  \n \
        Upload  : Calculating..".format(download))
        
        upload = speed.upload()/1024/1024
        self.ui.speed_label.setText("Tested.\n \
        Download: {:.2f}Mb/s  \n \
        Upload  : {:.2f}Mb/s".format(download,upload)) 
        
        print("end")
    
    #Checks the connection with sending request to google.com           
    def connectTest(self, host='http://google.com'):
        try:
            urllib.request.urlopen(host) 
            return True
        except:
            return False
    
    #Scans the active wifi networks and add them to combobox
    def Search(self):
        wifilist = []
        #wlp2s0 needs to modify if another wifi interfaces is used.(ifconfig for finding interfaces)
        cells = wifi.Cell.all('wlp2s0')

        for cell in cells:
            wifilist.append(cell)

        for wifi_network in wifilist:
            self.ui.comboBox.addItem(wifi_network.ssid)
        
        return wifilist

    #Searchs a spesific SSID(wifi name) from all scanned wifi list
    def FindFromSearchList(self, ssid):
        wifilist = self.Search()

        for cell in wifilist:
            if cell.ssid == ssid:
                return cell

        return False

    #Searchs a spesific SSID(wifi name) from saved network list
    def FindFromSavedList(self, ssid):
        #wlp2s0 needs to modify if another wifi interfaces is used.(ifconfig for finding interfaces)
        cell = wifi.Scheme.find('wlp2s0', ssid)

        if cell:
            return cell

        return False

    #Connects to wifi network selected in the combo box.
    def Connect(self, password=None):
        ssid = self.ui.comboBox.currentText()
        password = self.ui.lineEdit_2.text()
        print(ssid)
        print(password)
        
        cell = self.FindFromSearchList(ssid)

        if cell:
            savedcell = self.FindFromSavedList(cell.ssid)

            # Already Saved from Setting
            if savedcell:
                savedcell.activate()
                return cell

            # First time to conenct
            else:
                if cell.encrypted:
                    if password:
                        scheme = self.Add(cell, password)

                        try:
                            scheme.activate()

                        # Wrong Password
                        except wifi.exceptions.ConnectionError:
                            self.Delete(ssid)
                            return False

                        return cell
                    else:
                        return False
                else:
                    scheme = self.Add(cell)

                    try:
                        scheme.activate()
                    except wifi.exceptions.ConnectionError:
                        self.Delete(ssid)
                        return False

                    return cell
        
        return False

    #Saves the network to connect easier later on
    def Add(self, cell, password=None):
        if not cell:
            return False
        #wlp2s0 needs to modify if another wifi interfaces is used.(ifconfig for finding interfaces)
        scheme = wifi.Scheme.for_cell('wlp2s0', cell.ssid, cell, password)
        scheme.save()
        return scheme

    #Deletes the network from saved list
    def Delete(self, ssid):
        if not ssid:
            return False

        cell = self.FindFromSavedList(ssid)

        if cell:
            cell.delete()
            return True

        return False