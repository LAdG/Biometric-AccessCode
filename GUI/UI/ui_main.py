# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/resource/main.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.hello_btn = QtWidgets.QPushButton(self.centralwidget)
        self.hello_btn.setGeometry(QtCore.QRect(320, 210, 161, 71))
        self.hello_btn.setObjectName("hello_btn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Biometric-AccessCode"))
        self.hello_btn.setText(_translate("MainWindow", "Hello"))

