import json
import os
import win32com.client
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog, QMessageBox
from bs4 import BeautifulSoup
import requests

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(453, 298)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 20, 311, 221))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(["№", "Описание", "Время"])

        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_back.setGeometry(QtCore.QRect(350, 20, 75, 23))
        self.btn_back.setObjectName("btn_back")
        
        self.btn_take = QtWidgets.QPushButton(self.centralwidget)
        self.btn_take.setGeometry(QtCore.QRect(350, 50, 75, 23))
        self.btn_take.setObjectName("btn_take")
        
        self.btn_clear = QtWidgets.QPushButton(self.centralwidget)
        self.btn_clear.setGeometry(QtCore.QRect(350, 80, 75, 23))
        self.btn_clear.setObjectName("btn_clear")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 453, 21))
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
        
        self.btn_back.setText(_translate("MainWindow", "Назад"))
        self.btn_take.setText(_translate("MainWindow", "Получить"))
        self.btn_clear.setText(_translate("MainWindow", "Очистить"))

        # Подключение кнопок к функциям
        self.btn_back.clicked.connect(self.back)
        self.btn_take.clicked.connect(self.fetch_news)
        self.btn_clear.clicked.connect(self.clear_table)

    def back(self):
        QApplication.exit()

    def fetch_news(self):
        url = 'https://francais.news-pravda.com/'
        try:
            r = requests.get(url)
            r.raise_for_status()  # Проверка на ошибки HTTP
            soup = BeautifulSoup(r.text, 'html.parser')

            # Ищем новости и время для основного блока
            news = soup.find_all('div', class_='news-item__title')
            time = soup.find_all('div', class_='news-item__time')

            self.clear_table()

            for i in range(min(5, len(news))):  
                row_position = self.tableWidget.rowCount()
                self.tableWidget.insertRow(row_position)

                self.tableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(str(i + 1)))  # Номер
                self.tableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(news[i].text.strip()))  # Описание
                self.tableWidget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(time[i].text.strip()))  # Время

        except requests.exceptions.RequestException as e:
            QMessageBox.critical(None, 'Ошибка', f"Не удалось загрузить данные: {e}")

    def clear_table(self):
        self.tableWidget.setRowCount(0)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
