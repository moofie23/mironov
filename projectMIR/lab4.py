import json
import os
import win32com.client
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog, QMessageBox
import pandas as pd


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        def back(self):
            QApplication.quit()

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(665, 276)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_back.setGeometry(QtCore.QRect(580, 20, 75, 23))
        self.btn_back.setObjectName("btn_back")
        self.btn_back.clicked.connect(back)
        
        self.btn_take = QtWidgets.QPushButton(self.centralwidget)
        self.btn_take.setGeometry(QtCore.QRect(580, 50, 75, 23))
        self.btn_take.setObjectName("btn_take")
        
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear.setGeometry(QtCore.QRect(580, 80, 75, 23))
        self.btn_clear.setObjectName("btn_clear")
        self.btn_clear.clicked.connect(self.clear_table)  
        
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 20, 521, 181))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 665, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.btn_take.clicked.connect(self.load_json_data)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_back.setText(_translate("MainWindow", "Назад"))
        self.btn_take.setText(_translate("MainWindow", "Получить"))
        self.btn_clear.setText(_translate("MainWindow", "Очистить"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "mdix"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "modTs"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "usage"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "dn"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "id"))

    def load_json_data(self):
        options = QFileDialog.Options()
        filePath, _ = QFileDialog.getOpenFileName(None, "Выберите файл JSON", "", "JSON Files (*.json);;All Files (*)", options=options)
            with open(filePath, 'r', encoding='utf-8') as file:
                json_data = json.load(file)
            
            imdata = json_data.get("imdata", [])
            
            self.tableWidget.setRowCount(len(imdata))

            for row_index, item in enumerate(imdata):
                    dn = item["l1PhysIf"]["attributes"]["dn"]
                    mdix = item["l1PhysIf"]["attributes"].get("mdix", "")
                    modTs = item["l1PhysIf"]["attributes"].get("modTs", "")
                    usage = item["l1PhysIf"]["attributes"].get("usage", "")
                    id_ = item["l1PhysIf"]["attributes"].get("id", "")

                    self.tableWidget.setItem(row_index, 0, QtWidgets.QTableWidgetItem(mdix))
                    self.tableWidget.setItem(row_index, 1, QtWidgets.QTableWidgetItem(modTs))
                    self.tableWidget.setItem(row_index, 2, QtWidgets.QTableWidgetItem(usage))
                    self.tableWidget.setItem(row_index, 3, QtWidgets.QTableWidgetItem(dn))
                    self.tableWidget.setItem(row_index, 4, QtWidgets.QTableWidgetItem(id_))
                
    def clear_table(self):
        row_count = self.tableWidget.rowCount()
        for row in range(row_count):
            self.tableWidget.removeRow(0)  

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
