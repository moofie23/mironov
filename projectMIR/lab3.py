import urllib.parse
import os
import win32com.client
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QFileDialog, QMessageBox
import pandas as pd

class Ui_MainWindow(object):

    def back(self):
        QApplication.quit()

    def excel(self):
        options = QFileDialog.Options()
        filePath, _ = QFileDialog.getOpenFileName(None, "Выберите файл Excel", "", "Файлы Excel (*.xlsx);;Все файлы (*)", options=options)
        
        if filePath:
            self.excel_file_path = filePath
            self.lineEdit.setText(self.excel_file_path)  # Отображаем путь в textEdit
        else:
            QMessageBox.warning(None, "Ошибка", "Не выбран файл Excel!")

    def word(self):
        options = QFileDialog.Options()
        filePath, _ = QFileDialog.getOpenFileName(None, "Выберите шаблон Word", "", "Файлы Word (*.docx);;Все файлы (*)", options=options)
        
        if filePath:
            # Убедимся, что путь правильный и нет лишних символов
            self.word_file_path = urllib.parse.unquote(filePath)  # Декодируем путь, чтобы убрать кодировки, как %20 для пробела
            
            # Проверим наличие лишнего двойного слэша и исправим
            self.word_file_path = self.word_file_path.replace("\\\\", "\\")  # Заменяем двойные слэши на один
            self.lineEdit_2.setText(self.word_file_path)  # Отображаем путь в textEdit
        else:
            QMessageBox.warning(None, "Ошибка", "Не выбран файл шаблона Word!")

    def select_save_path(self):
        options = QFileDialog.Options()
        savePath, _ = QFileDialog.getSaveFileName(None, "Сохранить файл", "", "Word Files (*.docx);;All Files (*)", options=options)
        if savePath:
            self.save_file_path = savePath
            self.lineEdit_3.setText(self.save_file_path)
        else:
            QMessageBox.warning(None, "Ошибка", "Не выбран путь для сохранения файла!")

    def create_file(self):
        # Проверяем, выбраны ли все необходимые файлы и путь для сохранения
        if not hasattr(self, 'excel_file_path') or not hasattr(self, 'word_file_path') or not hasattr(self, 'save_file_path'):
            QMessageBox.warning(None, "Ошибка", "Не все файлы или путь для сохранения выбраны!")
            return

        try:
            # Чтение данных из Excel
            data = pd.read_excel(self.excel_file_path)
            print("Данные из Excel загружены:")
            print(data.head())  # Выводим первые строки данных для отладки

            # Убираем пробелы в названиях столбцов
            data.columns = data.columns.str.strip()

            # Проверка наличия необходимых столбцов в Excel
            if 'Фамилия и имя' not in data.columns or 'Дата рождения' not in data.columns or 'Адрес' not in data.columns:
                QMessageBox.warning(None, "Ошибка", "Не найдены необходимые столбцы в файле Excel!")
                print("Не найдены необходимые столбцы в файле Excel!")
                return

            # Работа с документом Word через COM
            word = win32com.client.Dispatch("Word.Application")
            word.Visible = False  # Не показывать приложение Word
            document = word.Documents.Open(self.word_file_path)
            print("Документ Word открыт успешно.")

            # Проходим по строкам данных Excel и заменяем в шаблоне Word
            for index, row in data.iterrows():
                # Заменяем данные в Word шаблоне
                for paragraph in document.Paragraphs:
                    if "{Фамилия и имя}" in paragraph.Range.Text:
                        paragraph.Range.Text = paragraph.Range.Text.replace("{Фамилия и имя}", str(row['Фамилия и имя']))
                    if "{Дата рождения}" in paragraph.Range.Text:
                        paragraph.Range.Text = paragraph.Range.Text.replace("{Дата рождения}", str(row['Дата рождения']))
                    if "{Адрес}" in paragraph.Range.Text:
                        paragraph.Range.Text = paragraph.Range.Text.replace("{Адрес}", str(row['Адрес']))

            # Сохраняем измененный документ
            document.SaveAs(self.save_file_path)
            print(f"Файл успешно сохранен: {self.save_file_path}")
            document.Close()
            word.Quit()

            QMessageBox.information(None, "Успех", f"Файл успешно создан: {self.save_file_path}")

        except Exception as e:
            # Обработка ошибок
            print(f"Ошибка: {e}")
            QMessageBox.warning(None, "Ошибка", f"Произошла ошибка при создании файла: {e}")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(460, 288)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1.setGeometry(QtCore.QRect(220, 30, 111, 51))
        self.btn1.setObjectName("btn1")
        self.btn2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn2.setGeometry(QtCore.QRect(220, 110, 111, 51))
        self.btn2.setObjectName("btn2")
        self.btn3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn3.setGeometry(QtCore.QRect(350, 110, 101, 51))
        self.btn3.setObjectName("btn3")
        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_back.setGeometry(QtCore.QRect(370, 10, 81, 31))
        self.btn_back.setObjectName("btn_back")
        self.btn_back.clicked.connect(self.back)
        self.btn2_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn2_2.setGeometry(QtCore.QRect(220, 190, 111, 51))
        self.btn2_2.setObjectName("btn2_2")
        self.btn2_2.clicked.connect(self.select_save_path)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 50, 201, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 120, 201, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 200, 201, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        
        # Соединение кнопок с функциями
        self.btn1.clicked.connect(self.excel)
        self.btn2.clicked.connect(self.word)
        self.btn3.clicked.connect(self.create_file)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 460, 21))
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
        self.btn1.setText(_translate("MainWindow", "Выбрать excel"))
        self.btn2.setText(_translate("MainWindow", "Выбрать Word"))
        self.btn3.setText(_translate("MainWindow", "Создать файл"))
        self.btn_back.setText(_translate("MainWindow", "Назад"))
        self.btn2_2.setText(_translate("MainWindow", "Выбрать путь"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
