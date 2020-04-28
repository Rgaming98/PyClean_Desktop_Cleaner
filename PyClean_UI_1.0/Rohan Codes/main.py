from PyQt5 import QtCore, QtGui, QtWidgets, uic

class PyClean(QtWidgets.QMainWindow):
    def __init__(self):
        super (PyClean,self).__init__()
        uic.loadUi('PyClean_Revised_Please_Use_This.ui',self)

if __name__=='__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = PyClean()
    window.show()
    sys.exit(app.exec_())
