# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import random

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from main import *
import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as canvas
from matplotlib.figure import Figure

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1375, 877)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1341, 841))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        self.tab_1.setObjectName("tab_1")
        self.value_slider = QtWidgets.QLabel(self.tab_1)
        self.value_slider.setGeometry(QtCore.QRect(470, 220, 261, 41))
        self.value_slider.setText("")
        self.value_slider.setObjectName("value_slider")
        self.label_rooms = QtWidgets.QLabel(self.tab_1)
        self.label_rooms.setGeometry(QtCore.QRect(10, 10, 261, 41))
        self.label_rooms.setObjectName("label_rooms")
        self.select_nurses = QtWidgets.QPushButton(self.tab_1)
        self.select_nurses.setGeometry(QtCore.QRect(140, 130, 93, 41))
        self.select_nurses.setObjectName("select_nurses")
        self.rooms = QtWidgets.QLineEdit(self.tab_1)
        self.rooms.setGeometry(QtCore.QRect(12, 50, 121, 31))
        self.rooms.setObjectName("rooms")
        self.error_nurse = QtWidgets.QLabel(self.tab_1)
        self.error_nurse.setGeometry(QtCore.QRect(140, 170, 261, 41))
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
        self.select_year = QtWidgets.QPushButton(self.tab_1)
        self.select_year.setGeometry(QtCore.QRect(740, 140, 93, 41))
        self.select_year.setObjectName("select_year")
        self.label_nurses = QtWidgets.QLabel(self.tab_1)
        self.label_nurses.setGeometry(QtCore.QRect(10, 93, 261, 41))
        self.label_nurses.setObjectName("label_nurses")
        self.estimated_number_of_nurses = QtWidgets.QLabel(self.tab_1)
        self.estimated_number_of_nurses.setGeometry(QtCore.QRect(250, 50, 261, 41))
        self.estimated_number_of_nurses.setText("")
        self.estimated_number_of_nurses.setObjectName("estimated_number_of_nurses")
        self.month = QtWidgets.QSpinBox(self.tab_1)
        self.month.setGeometry(QtCore.QRect(610, 61, 121, 31))
        self.month.setMinimum(1)
        self.month.setMaximum(12)
        self.month.setObjectName("month")
        self.label_more_qualified_nurses = QtWidgets.QLabel(self.tab_1)
        self.label_more_qualified_nurses.setGeometry(QtCore.QRect(10, 190, 261, 41))
        self.label_more_qualified_nurses.setObjectName("label_more_qualified_nurses")
        self.year = QtWidgets.QSpinBox(self.tab_1)
        self.year.setGeometry(QtCore.QRect(610, 150, 121, 31))
        self.year.setMinimum(1970)
        self.year.setMaximum(2023)
        self.year.setValue(2023)
        self.year.setObjectName("year")
        self.select_month = QtWidgets.QPushButton(self.tab_1)
        self.select_month.setGeometry(QtCore.QRect(738, 57, 93, 41))
        self.select_month.setObjectName("select_month")
        self.label_month = QtWidgets.QLabel(self.tab_1)
        self.label_month.setGeometry(QtCore.QRect(608, 20, 261, 41))
        self.label_month.setObjectName("label_month")
        self.select_rooms = QtWidgets.QPushButton(self.tab_1)
        self.select_rooms.setGeometry(QtCore.QRect(140, 47, 93, 41))
        self.select_rooms.setObjectName("select_rooms")
        self.percent_of_3nurses = QtWidgets.QSlider(self.tab_1)
        self.percent_of_3nurses.setGeometry(QtCore.QRect(10, 240, 451, 22))
        self.percent_of_3nurses.setMaximum(100)
        self.percent_of_3nurses.setOrientation(QtCore.Qt.Horizontal)
        self.percent_of_3nurses.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.percent_of_3nurses.setObjectName("percent_of_3nurses")
        self.label_year = QtWidgets.QLabel(self.tab_1)
        self.label_year.setGeometry(QtCore.QRect(610, 103, 261, 41))
        self.label_year.setObjectName("label_year")
        self.nurses = QtWidgets.QLineEdit(self.tab_1)
        self.nurses.setGeometry(QtCore.QRect(12, 133, 121, 31))
        self.nurses.setObjectName("nurses")
        self.error_room = QtWidgets.QLabel(self.tab_1)
        self.error_room.setGeometry(QtCore.QRect(140, 90, 261, 41))
        self.error_room.setText("")
        self.error_room.setObjectName("error_room")
        self.submit = QtWidgets.QPushButton(self.tab_1)
        self.submit.setGeometry(QtCore.QRect(20, 460, 93, 28))
        self.submit.setObjectName("submit")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_1)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 500, 1321, 311))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.tableWidget)
        self.error_solution = QtWidgets.QLabel(self.tab_1)
        self.error_solution.setGeometry(QtCore.QRect(130, 450, 611, 31))
        self.error_solution.setText("")
        self.error_solution.setObjectName("error_solution")
        self.reset = QtWidgets.QPushButton(self.tab_1)
        self.reset.setGeometry(QtCore.QRect(900, 460, 93, 28))
        self.reset.setObjectName("reset")
        self.tabWidget.addTab(self.tab_1, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.scrollArea = QtWidgets.QScrollArea(self.tab_3)
        self.scrollArea.setGeometry(QtCore.QRect(50, 50, 900, 700))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 900, 700))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scroll_nurses = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.scroll_nurses.setText("")
        self.scroll_nurses.setObjectName("scroll_nurses")
        self.verticalLayout_2.addWidget(self.scroll_nurses)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.tab_4)
        self.scrollArea_2.setGeometry(QtCore.QRect(50, 50, 900, 700))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 900, 700))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scroll_rooms = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.scroll_rooms.setObjectName("scroll_rooms")
        self.verticalLayout_3.addWidget(self.scroll_rooms)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.tabWidget.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
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
        self.reset.clicked.connect(self.resetf)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_rooms.setText(_translate("MainWindow", "Hello, select number of rooms:"))
        self.select_nurses.setText(_translate("MainWindow", "Select nurses"))
        self.select_year.setText(_translate("MainWindow", "Select year"))
        self.label_nurses.setText(_translate("MainWindow", "Select numer of nurses:"))
        self.label_more_qualified_nurses.setText(_translate("MainWindow", "Select percent of more qualified nurses:"))
        self.select_month.setText(_translate("MainWindow", "Select month"))
        self.label_month.setText(_translate("MainWindow", "Select month (1-12)"))
        self.select_rooms.setText(_translate("MainWindow", "Select rooms"))
        self.label_year.setText(_translate("MainWindow", "Select year"))
        self.submit.setText(_translate("MainWindow", "Submit"))
        self.reset.setText(_translate("MainWindow", "RESET"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "Menu"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Graph"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Nurses"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Rooms"))

    def save_rooms(self):
        try:
            self.rooms_ = int(self.rooms.text())
            self.estimated_number_of_nurses.setText("The minimum required number of nurses is: " + str(int(min_number_of_nurses(self.rooms_))))
            self.error_room.setText("")
        except:
            self.error_room.setText("ERROR")
            self.error_room.setStyleSheet("color: red")

    def save_nurses(self):
        try:
            self.nurses_ = int(self.nurses.text())
            self.error_nurse.setText("")
        except:
            self.error_nurse.setText("ERROR")
            self.error_nurse.setStyleSheet("color: red")

    def save_month(self):
        self.month_ = self.month.text()

    def save_year(self):
        self.year_ = self.year.text()

    def show_table(self):
        if self.nurses_ == None or self.rooms_ == None or self.year_ == None or self.month_ == None:
            pass
        else:
            try:
                print(self.nurses_, " ", self.rooms_, " ", self.year_, " ", self.month_)
                self.data = Solution(int(self.year_), int(self.month_), self.nurses_, self.rooms_)

                self.tableWidget.setColumnCount(self.data.best_sol.solution.shape[0])
                self.tableWidget.setRowCount(self.data.best_sol.solution.shape[1]+1)

                counter_days = 1

                for i in range(self.data.best_sol.solution.shape[0]):
                    table = QtWidgets.QTableWidgetItem("Day " + str(counter_days))
                    table.setTextAlignment(4)
                    self.tableWidget.setItem(0, i, table)
                    for j in range(self.data.best_sol.solution.shape[1]):
                        self.tableWidget.setItem(j+1, i, QtWidgets.QTableWidgetItem(str(self.data.best_sol.solution[i][j])))

                    if i % 4 == 0:
                        self.tableWidget.setSpan(0, i, 1, 4)
                        counter_days += 1

                self.try_to_show_graph()
                self.print_nursesf()
                self.print_roomsf()

                if self.data.value_of_solution() == inf:
                    self.error_solution.setText("Solution couldn't be found")
                    self.error_solution.setStyleSheet("color: red")

                else:
                    self.error_solution.setText("")
            except:
                self.error_solution.setText("Solution couldn't be found")
                self.error_solution.setStyleSheet("color: red")

    def value_change_slider(self):
        self.value_slider.setText(str(self.percent_of_3nurses.value()))

    def try_to_show_graph(self):
        try:
            self.layout = QtWidgets.QVBoxLayout(self.tab_2)
            x = np.arange(len(self.data.data_for_chart))
            y1 = self.data.data_for_chart
            y2 = self.data.best_solutions
            y3 = self.data.tabu_list_for_chart
            self.figure = plt.figure(figsize=(10, 5), layout='constrained')
            ax = self.figure.add_subplot(2,1,1)
            ax.plot(x, y1, x, y2)
            ax.set_title('Objective function graph')
            ax.set_xlabel('Iterations')
            ax.set_ylabel('Function value')
            ax.legend(["Solution", "Best solution"])
            ax2 = self.figure.add_subplot(2,1,2)
            ax2.plot(x, y3, 'g')
            ax2.set_title('Tabu list graph')
            ax2.set_xlabel('Iterations')
            ax2.set_ylabel('Tabu list length')
            self.canvas = FigureCanvas(self.figure)
            self.layout.addWidget(self.canvas)
            self.canvas.draw()
        except:
            pass

    def print_nursesf(self):
        try:
            self.print_nurses_ = self.data.best_sol.data.print_nurses()
            self.scroll_nurses.setText(self.print_nurses_)
        except:
            self.scroll_nurses.setText("")

    def print_roomsf(self):
        try:
            self.print_rooms_ = self.data.best_sol.data.print_room()
            self.scroll_rooms.setText(self.print_rooms_)
        except:
            self.scroll_rooms.setText("")

    def try_to_reset_graph(self):
        self.tabWidget.removeTab(1)
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.insertTab(1,self.tab_2, "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), "Graph")

    def resetf(self):
        self.rooms.setText("")
        self.estimated_number_of_nurses.setText("")
        self.error_room.setText("")
        self.rooms_ = None
        self.nurses.setText("")
        self.nurses_ = None
        self.error_nurse.setText("")
        self.month.setValue(1)
        self.year.setValue(2023)

        while self.tableWidget.rowCount() > 0:
            self.tableWidget.removeRow(0)

        self.data = None
        self.print_nursesf()
        self.print_roomsf()
        self.try_to_reset_graph()

def app():

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

