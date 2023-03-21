from get_and_write_info import get_sources
import sys
import PyQt5
import sqlite3
from PyQt5 import QtWidgets, QtWebEngineWidgets
from PyQt5.QtCore import QSize, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit, QPushButton


class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.initUI()
        #self.key_word_btn()
        #self.country_btn()
    
    def initUI(self):
        self.setMinimumSize(QSize(320, 150))

        self.line_keyword = QLineEdit(self)
        self.line_keyword.move(80, 20)
        self.line_keyword.resize(200, 32)

        self.line_country = QLineEdit(self)
        self.line_country.move(80, 60)
        self.line_country.resize(200, 32)

        self.nameLabel = QLabel(self)
        self.nameLabel.setText('key word:')
        self.nameLabel.move(15, 20)

        self.nameLabe2 = QLabel(self)
        self.nameLabe2.setText('country:')
        self.nameLabe2.move(15, 60)

        button = QPushButton('OK', self)
        button.clicked.connect(self.get_values)
        button.resize(200,32)
        button.move(80, 100)

    def get_values(self):

        keyword = self.line_keyword.text()
        print('Your keyword: ' + keyword)
        self.line_keyword.setText('')

        country = self.line_country.text()
        print('Your country: ' + country)
        self.line_country.setText('')


        get_sources(keyword, country)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())



