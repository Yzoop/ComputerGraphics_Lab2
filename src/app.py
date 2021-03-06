import os
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.Qt import QFileDialog

import app_design
from image_data_manager import imgs_stat

class ExampleApp(QtWidgets.QMainWindow, app_design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.pushButton.clicked.connect(self.browse_folder)
        self.set_column_names()
        self._col_name_idx = {"NAME": 0,
                                    "SIZE": 1,
                                    "DPI": 2,
                                    "COLOR_DEPTH": 3,
                                    "COMPRESSION": 4}


    def set_column_names(self):
        _translate = QtCore.QCoreApplication.translate
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Имя файла"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Размер изображения"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Разрешение"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Глубина цвета"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Сжатие"))

    def browse_folder(self):
        fname = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        if fname:
            self.filepathLabel.setText(fname)
            self.sayfolderNotChosen.setText("Выбранная папка:")
            self.tableWidget.setRowCount(0)
            for row_i, image_stat in enumerate(imgs_stat(os.listdir(fname), fname)):
                #print(image_stat)
                self.tableWidget.insertRow(row_i)
                for (stat_key, stat_value) in image_stat.items():
                    self.tableWidget.setItem(row_i, self._col_name_idx[stat_key], QtWidgets.QTableWidgetItem(str(stat_value)))



def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение
    
if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()