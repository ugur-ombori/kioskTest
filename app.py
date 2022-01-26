from PyQt5 import QtWidgets
from Ui_kiosk import Ui_MainWindow
import sys


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.showFullScreen()

        
        self.ui.exitButton.clicked.connect(self.exitButton_clicked)
        self.ui.poweroffButton.clicked.connect(self.poweroffButton_clicked)
        
    def poweroffButton_clicked(self):
        print("poweroff pressed do nothing atm.")
    
    def exitButton_clicked(self):
        sys.exit(app.exec_())

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
