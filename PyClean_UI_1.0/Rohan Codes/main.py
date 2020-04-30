from PyQt5.QtWidgets import QMainWindow, QApplication
from UI_File.pycleanui import Ui_MainWindow
import sys,os,win32api
from datetime import datetime


class PyClean(QMainWindow):
    def __init__(self):
        super (PyClean,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        username = os.getlogin()
        self.ui.Userlabel.setText(username)
        datenow = datetime.now()
        self.ui.Datelabel.setText((datenow.strftime("%Y-%m-%d %H:%M")))
        drives = win32api.GetLogicalDriveStrings()
        drives = drives.split('\000')[:-1]
        self.ui.selectdrive.clear
        self.ui.selectdrive.addItems(drives)


if __name__=='__main__':
    app = QApplication(sys.argv)
    window = PyClean()
    window.show()
    sys.exit(app.exec_())
