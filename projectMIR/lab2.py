from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QMessageBox, QVBoxLayout
import os
from datetime import datetime

class Ui_MainWindow(object):

    def select_file(self):
        file_name, _ = QFileDialog.getOpenFileName(None, 'Выберите файл', '', 'Все файлы (*)')

        if file_name:
            file_size = os.path.getsize(file_name)  
            file_extension = os.path.splitext(file_name)[1]  
            file_creation_time = os.path.getctime(file_name)  
            file_modified_time = os.path.getmtime(file_name)  

            file_creation_time = datetime.fromtimestamp(file_creation_time).strftime('%Y-%m-%d %H:%M:%S')
            file_modified_time = datetime.fromtimestamp(file_modified_time).strftime('%Y-%m-%d %H:%M:%S')

            self.label_name.setText(f"Название файла: {os.path.basename(file_name)}")
            self.label_res.setText(f"Расширение: {file_extension}")
            self.label_create.setText(f"Дата создания: {file_creation_time}")
            self.label_size.setText(f"Размер: {file_size} байт")
            self.label_put.setText(f"Путь: {file_name}")

    def back(self):
        QApplication.quit()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(324, 289)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.btn_select = QtWidgets.QPushButton(self.centralwidget)
        self.btn_select.setGeometry(QtCore.QRect(220, 50, 75, 21))
        self.btn_select.setObjectName("btn_select")
        self.btn_select.clicked.connect(self.select_file)

        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_back.setGeometry(QtCore.QRect(220, 10, 75, 23))
        self.btn_back.setObjectName("btn_back")
        self.btn_back.clicked.connect(self.back)

        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(20, 100, 280, 16))
        self.label_name.setObjectName("label_name")

        self.label_res = QtWidgets.QLabel(self.centralwidget)
        self.label_res.setGeometry(QtCore.QRect(20, 130, 280, 16))
        self.label_res.setObjectName("label_res")

        self.label_create = QtWidgets.QLabel(self.centralwidget)
        self.label_create.setGeometry(QtCore.QRect(20, 160, 280, 16))
        self.label_create.setObjectName("label_create")

        self.label_size = QtWidgets.QLabel(self.centralwidget)
        self.label_size.setGeometry(QtCore.QRect(20, 190, 280, 16))
        self.label_size.setObjectName("label_size")

        self.label_put = QtWidgets.QLabel(self.centralwidget)
        self.label_put.setGeometry(QtCore.QRect(20, 220, 280, 16))
        self.label_put.setObjectName("label_put")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 324, 21))
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
        self.btn_select.setText(_translate("MainWindow", "Выбрать"))
        self.btn_back.setText(_translate("MainWindow", "Назад"))
        self.label_name.setText(_translate("MainWindow", "Название файла"))
        self.label_res.setText(_translate("MainWindow", "Расширение"))
        self.label_create.setText(_translate("MainWindow", "Дата создания"))
        self.label_size.setText(_translate("MainWindow", "Размер"))
        self.label_put.setText(_translate("MainWindow", "Путь"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())