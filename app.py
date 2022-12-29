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
        self.label_rooms = QtWidgets.QLabel(self.centralwidget)
        self.label_rooms.setGeometry(QtCore.QRect(40, 30, 261, 41))
        self.label_rooms.setObjectName("label_rooms")
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
        self.nurses = QtWidgets.QLineEdit(self.centralwidget)
        self.nurses.setGeometry(QtCore.QRect(42, 153, 121, 31))
        self.nurses.setObjectName("nurses")
        self.label_nurses = QtWidgets.QLabel(self.centralwidget)
        self.label_nurses.setGeometry(QtCore.QRect(40, 113, 261, 41))
        self.label_nurses.setObjectName("label_nurses")
        self.select_nurses = QtWidgets.QPushButton(self.centralwidget)
        self.select_nurses.setGeometry(QtCore.QRect(170, 150, 93, 41))
        self.select_nurses.setObjectName("select_nurses")
        self.estimated_number_of_nurses = QtWidgets.QLabel(self.centralwidget)
        self.estimated_number_of_nurses.setGeometry(QtCore.QRect(280, 70, 261, 41))
        self.estimated_number_of_nurses.setText("")
        self.estimated_number_of_nurses.setObjectName("estimated_number_of_nurses")
        self.label_month = QtWidgets.QLabel(self.centralwidget)
        self.label_month.setGeometry(QtCore.QRect(638, 40, 261, 41))
        self.label_month.setObjectName("label_month")
        self.select_month = QtWidgets.QPushButton(self.centralwidget)
        self.select_month.setGeometry(QtCore.QRect(768, 77, 93, 41))
        self.select_month.setObjectName("select_month")
        self.label_year = QtWidgets.QLabel(self.centralwidget)
        self.label_year.setGeometry(QtCore.QRect(640, 123, 261, 41))
        self.label_year.setObjectName("label_year")
        self.select_year = QtWidgets.QPushButton(self.centralwidget)
        self.select_year.setGeometry(QtCore.QRect(770, 160, 93, 41))
        self.select_year.setObjectName("select_year")
        self.month = QtWidgets.QSpinBox(self.centralwidget)
        self.month.setGeometry(QtCore.QRect(640, 81, 121, 31))
        self.month.setMinimum(1)
        self.month.setMaximum(12)
        self.month.setObjectName("month")
        self.percent_of_3nurses = QtWidgets.QSlider(self.centralwidget)
        self.percent_of_3nurses.setGeometry(QtCore.QRect(40, 260, 451, 22))
        self.percent_of_3nurses.setMaximum(0)
        self.percent_of_3nurses.setMaximum(100)
        self.percent_of_3nurses.setOrientation(QtCore.Qt.Horizontal)
        self.percent_of_3nurses.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.percent_of_3nurses.setObjectName("percent_of_3nurses")
        self.label_more_qualified_nurses = QtWidgets.QLabel(self.centralwidget)
        self.label_more_qualified_nurses.setGeometry(QtCore.QRect(40, 210, 261, 41))
        self.label_more_qualified_nurses.setObjectName("label_more_qualified_nurses")
        self.year = QtWidgets.QSpinBox(self.centralwidget)
        self.year.setGeometry(QtCore.QRect(640, 170, 121, 31))
        self.year.setMinimum(1970)
        self.year.setMaximum(2023)
        self.year.setObjectName("year")
        self.error_room = QtWidgets.QLabel(self.centralwidget)
        self.error_room.setGeometry(QtCore.QRect(170, 110, 261, 41))
        self.error_room.setText("")
        self.error_room.setObjectName("error_room")
        self.value_slider = QtWidgets.QLabel(self.centralwidget)
        self.value_slider.setGeometry(QtCore.QRect(500, 240, 261, 41))
        self.value_slider.setText("0")
        self.value_slider.setObjectName("value_slider")
        self.error_nurse = QtWidgets.QLabel(self.centralwidget)
        self.error_nurse.setGeometry(QtCore.QRect(170, 190, 261, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 4))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 4))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.error_nurse.setPalette(palette)
        self.error_nurse.setText("")
        self.error_nurse.setObjectName("error_nurse")
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

        self.nurses_ = None
        self.rooms_ = None
        self.year_ = None
        self.month_ = None

        self.select_rooms.clicked.connect(self.save_rooms)
        self.select_nurses.clicked.connect(self.save_nurses)
        self.select_year.clicked.connect(self.save_year)
        self.select_month.clicked.connect(self.save_month)
        self.submit.clicked.connect(self.show_table)
        self.percent_of_3nurses.valueChanged.connect(self.value_change_slider)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_rooms.setText(_translate("MainWindow", "Hello, select number of rooms:"))
        self.submit.setText(_translate("MainWindow", "Submit"))
        self.select_rooms.setText(_translate("MainWindow", "Select rooms"))
        self.label_nurses.setText(_translate("MainWindow", "Select numer of nurses:"))
        self.select_nurses.setText(_translate("MainWindow", "Select nurses"))
        self.label_month.setText(_translate("MainWindow", "Select month (1-12)"))
        self.select_month.setText(_translate("MainWindow", "Select month"))
        self.label_year.setText(_translate("MainWindow", "Select year"))
        self.select_year.setText(_translate("MainWindow", "Select year"))
        self.label_more_qualified_nurses.setText(_translate("MainWindow", "Select percent of more qualified nurses:"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))

    def save_rooms(self):
        try:
            self.rooms_ = int(self.rooms.text())
            self.estimated_number_of_nurses.setText(str(6))
            self.error_room.setText("")
        except:
            self.error_room.setText("ERROR")

    def save_nurses(self):
        try:
            self.nurses_ = int(self.nurses.text())
            self.error_nurse.setText("")
        except:
            self.error_nurse.setText("ERROR")

    def save_month(self):
        self.month_ = self.month.text()

    def save_year(self):
        self.year_ = self.year.text()

    def show_table(self):

        if self.nurses_ == None or self.rooms_ == None or self.year_ == None or self.month_ == None:
            pass
        else:
            print(self.nurses_, " ", self.rooms_, " ", self.year_, " ", self.month_)
            self.data = Solution(int(self.year_), int(self.month_), self.nurses_, self.rooms_)

            self.tableWidget.setColumnCount(self.data.solution.shape[0])
            self.tableWidget.setRowCount(self.data.solution.shape[1])

            for i in range(self.data.solution.shape[0]):
                for j in range(self.data.solution.shape[1]):
                    self.tableWidget.setItem(j, i, QtWidgets.QTableWidgetItem(str(self.data.solution[i][j])))

    def value_change_slider(self):
        self.value_slider.setText(str(self.percent_of_3nurses.value()))

def app():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())




