# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyClean_Revised_Please_Use_This.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

import datetime
now = datetime.datetime.now()
# print ("Current date and time : into date and time dialouge")

import getpass
username = getpass.getuser()
# Print username in user box. 




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1943, 1309)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.RevealInExplorerbutton = QtWidgets.QPushButton(self.centralwidget)
        self.RevealInExplorerbutton.setGeometry(QtCore.QRect(690, 850, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.RevealInExplorerbutton.setFont(font)
        self.RevealInExplorerbutton.setObjectName("RevealInExplorerbutton")
        self.AnalyzeDriveButton = QtWidgets.QPushButton(self.centralwidget)
        self.AnalyzeDriveButton.setGeometry(QtCore.QRect(70, 210, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.AnalyzeDriveButton.setFont(font)
        self.AnalyzeDriveButton.setIconSize(QtCore.QSize(12, 12))
        self.AnalyzeDriveButton.setAutoDefault(False)
        self.AnalyzeDriveButton.setDefault(False)
        self.AnalyzeDriveButton.setFlat(False)
        self.AnalyzeDriveButton.setObjectName("AnalyzeDriveButton")
        self.DeleteForeverbutton = QtWidgets.QPushButton(self.centralwidget)
        self.DeleteForeverbutton.setGeometry(QtCore.QRect(1640, 850, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.DeleteForeverbutton.setFont(font)
        self.DeleteForeverbutton.setObjectName("DeleteForeverbutton")
        self.MoveToDrivebutton = QtWidgets.QPushButton(self.centralwidget)
        self.MoveToDrivebutton.setGeometry(QtCore.QRect(1260, 850, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.MoveToDrivebutton.setFont(font)
        self.MoveToDrivebutton.setObjectName("MoveToDrivebutton")
        self.Userlabel = QtWidgets.QLabel(self.centralwidget)
        self.Userlabel.setGeometry(QtCore.QRect(1720, 1190, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Userlabel.setFont(font)
        self.Userlabel.setObjectName("Userlabel")
        self.MoveToSelectedbutton = QtWidgets.QPushButton(self.centralwidget)
        self.MoveToSelectedbutton.setGeometry(QtCore.QRect(1020, 850, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.MoveToSelectedbutton.setFont(font)
        self.MoveToSelectedbutton.setObjectName("MoveToSelectedbutton")
        self.analyzeprogressbar = QtWidgets.QProgressBar(self.centralwidget)
        self.analyzeprogressbar.setGeometry(QtCore.QRect(400, 850, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.analyzeprogressbar.setFont(font)
        self.analyzeprogressbar.setProperty("value", 24)
        self.analyzeprogressbar.setObjectName("analyzeprogressbar")
        self.refreshlistbutton = QtWidgets.QPushButton(self.centralwidget)
        self.refreshlistbutton.setGeometry(QtCore.QRect(900, 850, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.refreshlistbutton.setFont(font)
        self.refreshlistbutton.setObjectName("refreshlistbutton")
        self.selectedlistwidget = QtWidgets.QListWidget(self.centralwidget)
        self.selectedlistwidget.setGeometry(QtCore.QRect(1260, 130, 601, 711))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.selectedlistwidget.setFont(font)
        self.selectedlistwidget.setObjectName("selectedlistwidget")
        item = QtWidgets.QListWidgetItem()
        self.selectedlistwidget.addItem(item)
        self.ExportLogbutton = QtWidgets.QPushButton(self.centralwidget)
        self.ExportLogbutton.setGeometry(QtCore.QRect(1640, 900, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ExportLogbutton.setFont(font)
        self.ExportLogbutton.setObjectName("ExportLogbutton")
        self.selectedpathlabel = QtWidgets.QLabel(self.centralwidget)
        self.selectedpathlabel.setGeometry(QtCore.QRect(250, 210, 211, 31))
        self.selectedpathlabel.setText("")
        self.selectedpathlabel.setObjectName("selectedpathlabel")
        self.Datelabel = QtWidgets.QLabel(self.centralwidget)
        self.Datelabel.setGeometry(QtCore.QRect(230, 1190, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Datelabel.setFont(font)
        self.Datelabel.setObjectName("Datelabel")
        self.clearlistbutton = QtWidgets.QPushButton(self.centralwidget)
        self.clearlistbutton.setGeometry(QtCore.QRect(1490, 850, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.clearlistbutton.setFont(font)
        self.clearlistbutton.setObjectName("clearlistbutton")
        self.Analyzelistbutton = QtWidgets.QPushButton(self.centralwidget)
        self.Analyzelistbutton.setGeometry(QtCore.QRect(520, 210, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Analyzelistbutton.setFont(font)
        self.Analyzelistbutton.setObjectName("Analyzelistbutton")
        self.ChangeDriveButton = QtWidgets.QPushButton(self.centralwidget)
        self.ChangeDriveButton.setGeometry(QtCore.QRect(290, 210, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ChangeDriveButton.setFont(font)
        self.ChangeDriveButton.setObjectName("ChangeDriveButton")
        self.generatedlistwidget = QtWidgets.QListWidget(self.centralwidget)
        self.generatedlistwidget.setGeometry(QtCore.QRect(690, 130, 541, 711))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.generatedlistwidget.setFont(font)
        self.generatedlistwidget.setObjectName("generatedlistwidget")
        item = QtWidgets.QListWidgetItem()
        self.generatedlistwidget.addItem(item)
        self.selectyourdrive = QtWidgets.QLabel(self.centralwidget)
        self.selectyourdrive.setGeometry(QtCore.QRect(70, 120, 461, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.selectyourdrive.setFont(font)
        self.selectyourdrive.setObjectName("selectyourdrive")
        self.listoffolders = QtWidgets.QLabel(self.centralwidget)
        self.listoffolders.setGeometry(QtCore.QRect(720, 80, 501, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.listoffolders.setFont(font)
        self.listoffolders.setObjectName("listoffolders")
        self.selectedfilesandfolders = QtWidgets.QLabel(self.centralwidget)
        self.selectedfilesandfolders.setGeometry(QtCore.QRect(1400, 80, 501, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.selectedfilesandfolders.setFont(font)
        self.selectedfilesandfolders.setObjectName("selectedfilesandfolders")
        self.selectdrive = QtWidgets.QComboBox(self.centralwidget)
        self.selectdrive.setGeometry(QtCore.QRect(70, 160, 591, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.selectdrive.setFont(font)
        self.selectdrive.setObjectName("selectdrive")
        self.selectdrive.addItem("")
        self.selectdrive.addItem("")
        self.filetree = QtWidgets.QTreeWidget(self.centralwidget)
        self.filetree.setGeometry(QtCore.QRect(70, 340, 591, 501))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.filetree.setFont(font)
        self.filetree.setObjectName("filetree")
        self.selecteddrive = QtWidgets.QLabel(self.centralwidget)
        self.selecteddrive.setGeometry(QtCore.QRect(70, 280, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.selecteddrive.setFont(font)
        self.selecteddrive.setObjectName("selecteddrive")
        self.treeinput = QtWidgets.QLineEdit(self.centralwidget)
        self.treeinput.setGeometry(QtCore.QRect(240, 280, 421, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.treeinput.setFont(font)
        self.treeinput.setObjectName("treeinput")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 1190, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1640, 1190, 69, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1943, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menubar.sizePolicy().hasHeightForWidth())
        self.menubar.setSizePolicy(sizePolicy)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuWindow = QtWidgets.QMenu(self.menubar)
        self.menuWindow.setObjectName("menuWindow")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionRun_as_Admin = QtWidgets.QAction(MainWindow)
        self.actionRun_as_Admin.setObjectName("actionRun_as_Admin")
        self.actionMinimize = QtWidgets.QAction(MainWindow)
        self.actionMinimize.setObjectName("actionMinimize")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionRun_as_Admin)
        self.menuFile.addAction(self.actionMinimize)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.RevealInExplorerbutton.setText(_translate("MainWindow", "Reveal in Explorer"))
        self.AnalyzeDriveButton.setText(_translate("MainWindow", "Analyze Drive"))
        self.DeleteForeverbutton.setText(_translate("MainWindow", "Delete Forever"))
        self.MoveToDrivebutton.setText(_translate("MainWindow", "Move to (x:) Drive"))
        self.Userlabel.setText(_translate("MainWindow", username))
        self.MoveToSelectedbutton.setText(_translate("MainWindow", "Move to Selected"))
        self.refreshlistbutton.setText(_translate("MainWindow", "Refresh"))
        __sortingEnabled = self.selectedlistwidget.isSortingEnabled()
        self.selectedlistwidget.setSortingEnabled(False)
        item = self.selectedlistwidget.item(0)
        item.setText(_translate("MainWindow", "listtest"))
        self.selectedlistwidget.setSortingEnabled(__sortingEnabled)
        self.ExportLogbutton.setText(_translate("MainWindow", "Export Change Log"))
        self.Datelabel.setText(_translate("MainWindow", (now.strftime("%Y-%m-%d %H:%M:%S"))))
        self.clearlistbutton.setText(_translate("MainWindow", "Clear"))
        self.Analyzelistbutton.setText(_translate("MainWindow", "Show List"))
        self.ChangeDriveButton.setText(_translate("MainWindow", "Change Drive"))
        __sortingEnabled = self.generatedlistwidget.isSortingEnabled()
        self.generatedlistwidget.setSortingEnabled(False)
        item = self.generatedlistwidget.item(0)
        item.setText(_translate("MainWindow", "listtest"))
        self.generatedlistwidget.setSortingEnabled(__sortingEnabled)
        self.selectyourdrive.setText(_translate("MainWindow", "Select your desired drive to analyze:"))
        self.listoffolders.setText(_translate("MainWindow", "List of folders according to their size."))
        self.selectedfilesandfolders.setText(_translate("MainWindow", "Selected Files and Folders"))
        self.selectdrive.setItemText(0, _translate("MainWindow", "C:/"))
        self.selectdrive.setItemText(1, _translate("MainWindow", "D:/"))
        self.filetree.headerItem().setText(0, _translate("MainWindow", "1"))
        self.filetree.headerItem().setText(1, _translate("MainWindow", "Test"))
        self.selecteddrive.setText(_translate("MainWindow", "Selected Drive:"))
        self.label.setText(_translate("MainWindow", "Date and time:"))
        self.label_2.setText(_translate("MainWindow", "User:"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuWindow.setTitle(_translate("MainWindow", "Window"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionRun_as_Admin.setText(_translate("MainWindow", "Run as Admin"))
        self.actionMinimize.setText(_translate("MainWindow", "Minimize"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
