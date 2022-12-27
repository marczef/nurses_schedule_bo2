# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from main import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1121, 686)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.nam = QtWidgets.QLabel(self.centralwidget)
        self.nam.setGeometry(QtCore.QRect(40, 30, 261, 41))
        self.nam.setObjectName("nam")
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(30, 310, 93, 28))
        self.submit.setObjectName("submit")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 360, 1041, 251))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.rooms = QtWidgets.QLineEdit(self.centralwidget)
        self.rooms.setGeometry(QtCore.QRect(42, 70, 121, 31))
        self.rooms.setObjectName("rooms")
        self.select_rooms = QtWidgets.QPushButton(self.centralwidget)
        self.select_rooms.setGeometry(QtCore.QRect(170, 67, 93, 41))
        self.select_rooms.setObjectName("select_rooms")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1121, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.data = Solution(2022, 12, 25, 4)

        self.submit.clicked.connect(self.show_table)
        self.select_rooms.clicked.connect(self.save_rooms)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.nam.setText(_translate("MainWindow", "Hello, select number of nurses and rooms:"))
        self.submit.setText(_translate("MainWindow", "Submit"))
        self.select_rooms.setText(_translate("MainWindow", "Select rooms"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))

    def save_rooms(self):
        self.text = self.rooms.text()
        self.rooms.clear()

    def show_table(self):
        self.tableWidget.setColumnCount(self.data.solution.shape[0])
        self.tableWidget.setRowCount(self.data.solution.shape[1])

        for i in range(self.data.solution.shape[0]):
            for j in range(self.data.solution.shape[1]):
                self.tableWidget.setItem(j, i, QtWidgets.QTableWidgetItem(str(self.data.solution[i][j])))

def app():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

