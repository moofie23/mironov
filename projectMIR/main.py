# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

# & 'c:\Users\PYst\AppData\Local\Programs\Python\Python313\python.exe' -m PyQt5.uic.pyuic main.ui -o main.py -x


from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess

class Ui_MainWindow(object):

    def openlab1(self):
        subprocess.run(["python", "mainwindow.py"])
    
    def openlab2(self):
        subprocess.run(["python", "lab2.py"])
    
    def openlab3(self):
        subprocess.run(["python", "lab3.py"])

    def openlab4(self):
        subprocess.run(["python", "lab4.py"])
        
    def openlab5(self):
        subprocess.run(["python", "lab5.py"])

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(418, 376)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lab2button = QtWidgets.QPushButton(self.centralwidget)
        self.lab2button.setGeometry(QtCore.QRect(120, 120, 75, 23))
        self.lab2button.setObjectName("lab2button")
        self.lab2button.clicked.connect(self.openlab2)
        self.lab3button = QtWidgets.QPushButton(self.centralwidget)
        self.lab3button.setGeometry(QtCore.QRect(120, 150, 75, 23))
        self.lab3button.setObjectName("lab3button")
        self.lab3button.clicked.connect(self.openlab3)
        self.lab4button = QtWidgets.QPushButton(self.centralwidget)
        self.lab4button.setGeometry(QtCore.QRect(120, 180, 75, 23))
        self.lab4button.setObjectName("lab4button")
        self.lab4button.clicked.connect(self.openlab4)
        self.lab5button = QtWidgets.QPushButton(self.centralwidget)
        self.lab5button.setGeometry(QtCore.QRect(120, 210, 75, 23))
        self.lab5button.setObjectName("lab5button")
        self.lab5button.clicked.connect(self.openlab5)
        self.lab1button = QtWidgets.QPushButton(self.centralwidget)
        self.lab1button.setGeometry(QtCore.QRect(120, 90, 75, 23))
        self.lab1button.setObjectName("lab1button")
        self.lab1button.clicked.connect(self.openlab1)
        self.lab6button = QtWidgets.QPushButton(self.centralwidget)
        self.lab6button.setGeometry(QtCore.QRect(200, 90, 75, 23))
        self.lab6button.setObjectName("lab6button")
        self.lab7button = QtWidgets.QPushButton(self.centralwidget)
        self.lab7button.setGeometry(QtCore.QRect(200, 120, 75, 23))
        self.lab7button.setObjectName("lab7button")
        self.lab9button = QtWidgets.QPushButton(self.centralwidget)
        self.lab9button.setGeometry(QtCore.QRect(200, 180, 75, 23))
        self.lab9button.setObjectName("lab9button")
        self.lab8button = QtWidgets.QPushButton(self.centralwidget)
        self.lab8button.setGeometry(QtCore.QRect(200, 150, 75, 23))
        self.lab8button.setObjectName("lab8button")
        self.lab10button = QtWidgets.QPushButton(self.centralwidget)
        self.lab10button.setGeometry(QtCore.QRect(200, 210, 75, 23))
        self.lab10button.setObjectName("lab10button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 50, 111, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 280, 101, 16))
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 418, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lab2button.setText(_translate("MainWindow", "2"))
        self.lab3button.setText(_translate("MainWindow", "3"))
        self.lab4button.setText(_translate("MainWindow", "4"))
        self.lab5button.setText(_translate("MainWindow", "5"))
        self.lab1button.setText(_translate("MainWindow", "1"))
        self.lab6button.setText(_translate("MainWindow", "6"))
        self.lab7button.setText(_translate("MainWindow", "7"))
        self.lab9button.setText(_translate("MainWindow", "9"))
        self.lab8button.setText(_translate("MainWindow", "8"))
        self.lab10button.setText(_translate("MainWindow", "10"))
        self.label.setText(_translate("MainWindow", "Лаборатрные работы"))
        self.label_2.setText(_translate("MainWindow", "Миронов ИС 22/9-П"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
