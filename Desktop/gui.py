# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Samba.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(490, 467)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        MainWindow.setFont(font)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 290, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(16, 110, 211); border-style: solid; border-width: 1px; border-radius: 10px;")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 20, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 70, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 110, 271, 31))
        self.lineEdit.setStyleSheet("border-style: solid; border-width: 1px; border-radius: 10px;")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 160, 271, 31))
        self.lineEdit_2.setStyleSheet("border-style: solid; border-width: 1px; border-radius: 10px;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(160, 340, 171, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 240, 271, 31))
        self.lineEdit_3.setStyleSheet("border-style: solid; border-width: 1px; border-radius: 10px;")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_notif = QtWidgets.QLabel(self.centralwidget)
        self.label_notif.setGeometry(QtCore.QRect(170, 370, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_notif.setFont(font)
        self.label_notif.setStyleSheet("color: red")
        self.label_notif.setText("")
        self.label_notif.setObjectName("label_notif")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 490, 20))
        self.menubar.setObjectName("menubar")
        self.menuWeb = QtWidgets.QMenu(self.menubar)
        self.menuWeb.setObjectName("menuWeb")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSource_Code = QtWidgets.QAction(MainWindow)
        self.actionSource_Code.setObjectName("actionSource_Code")
        self.menuWeb.addAction(self.actionSource_Code)
        self.menuWeb.addSeparator()
        self.menubar.addAction(self.menuWeb.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Connexion"))
        self.pushButton.setText(_translate("MainWindow", "Se connecter"))
        self.label.setText(_translate("MainWindow", "ESTI Serveur"))
        self.label_2.setText(_translate("MainWindow", "Connexion compte"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Nom d\'utilisateur"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Mot de passe"))
        self.checkBox.setText(_translate("MainWindow", "Connecter au démarrage"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "Niveau"))
        self.menuWeb.setTitle(_translate("MainWindow", "Plus"))
        self.actionSource_Code.setText(_translate("MainWindow", "Source Code"))



class Fenetre(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.setupUi(parent)
        self.pushButton.clicked.connect(self.print_hello)


    def print_hello(self):
        print('hello')

def main():
    app = QApplication(sys.argv)
    Qinstance = QMainWindow()
    fenetre = Fenetre(Qinstance)
    Qinstance.show()
    app.exec_()


if __name__ == '__main__':
    import sys
    main()