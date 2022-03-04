from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from Ui_printerTest import Ui_Dialog
import os
import sys
from escpos.connections import getUSBPrinter
import netifaces

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

        #filter the physical interfaces to not show HAL interfaces
        self._interfaces = netifaces.interfaces()
        try:#Eliminate the 'lo' interface
            self._interfaces.remove('lo')
        except:
            print("no lo interface found!")
        try:#Eliminate the 'docker' interface
            self._interfaces.remove('docker0')
        except:
            print("no docker0 interface found!")
        
        labelStr = ""
        for iface in self._interfaces:
            allAddrs = netifaces.ifaddresses(iface)
            labelStr += 'Interface '+  iface + "\n"
            for family in allAddrs:
                addrs = allAddrs[family]
                fam_name = netifaces.address_families[family]
                for addr in addrs:
                    if fam_name == "AF_PACKET":
                        labelStr+='   MAC Address  :'+ addr['addr'] + "\n"
        font2 = QtGui.QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setWeight(21)
        self.ui.speed_label.setFont(font2)
        self.ui.speed_label.setText(labelStr)

        self.show()
    #Connects to printer and prints a test reciept with a content of MAC Adresses    
    def printerPrint(self):
        #try to connect Epson TM-T20III USB printer device.
        try:
            printer = getUSBPrinter(commandSet='Generic')(idVendor=0x04b8,
                          			      idProduct=0x0e28, 
                          			      inputEndPoint=0x82,
                          		   	      outputEndPoint=0x01)
        except: 
            print("no Epson TM-T20III printer Found!")
        
        #try to connect Epson TM-M10 USB printer device. 
        try:
            printer = getUSBPrinter(commandSet='Generic')(idVendor=0x04b8,
                          			      idProduct=0x0e1f, 
                          			      inputEndPoint=0x82,
                          		   	      outputEndPoint=0x01)
        except: 
            print("no Epson TM-M10 printer Found!")

        printer.drawerKickPulse()	
        printer.doubleHeight()
        printer.doubleWidth()
        printer.bold() 
        #Scan eth and wifi interfaces and add to printing text
        try:
            for iface in self._interfaces:
                allAddrs = netifaces.ifaddresses(iface)
                printer.text('Interface %s:' % iface)
                print('Interface %s:' % iface)
                for family in allAddrs:
                    addrs = allAddrs[family]
                    fam_name = netifaces.address_families[family]
                    for addr in addrs:
                        if fam_name == "AF_PACKET":
                            printer.text('    MAC Address  : %s' % addr['addr'])
                            print('    Address  : %s' % addr['addr'])        
        except:
            printer.text('Scanning MAC Adresses... Try again in few seconds.')
        #print
        printer.lf()
        printer.drawerKickPulse()
        printer.cutPaper()
