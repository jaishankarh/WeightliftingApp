# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'print_select.ui'
#
# Created: Mon Dec 15 11:59:37 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from PySide.QtCore import *
from PySide.QtGui import *
from printfn.print_competition import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 200)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.training_btn = QtGui.QPushButton(self.centralwidget)
        self.training_btn.setGeometry(QtCore.QRect(60, 50, 121, 61))
        self.training_btn.setObjectName("training_btn")
        self.comp_btn = QtGui.QPushButton(self.centralwidget)
        self.comp_btn.setGeometry(QtCore.QRect(210, 50, 121, 61))
        self.comp_btn.setObjectName("comp_btn")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 20, 211, 16))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.comp_btn.clicked.connect(self.openPrintOptionsWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Print Select Window", None, QtGui.QApplication.UnicodeUTF8))
        self.training_btn.setText(QtGui.QApplication.translate("MainWindow", "Training", None, QtGui.QApplication.UnicodeUTF8))
        self.comp_btn.setText(QtGui.QApplication.translate("MainWindow", "Competition", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Select what you want to print", None, QtGui.QApplication.UnicodeUTF8))

    def openPrintOptionsWindow(self):
        self.printWin = ControlPrintOptionsWindow.getCurrentInstance()
        self.printWin.show()
        self.printWin.raise_()



class ControlPrintSelectWindow(QMainWindow):

    currentInstance = None

    @classmethod
    def getCurrentInstance(cls):
        if cls.currentInstance is None:
            cls.currentInstance = ControlPrintSelectWindow()
            print("I was here")
            return cls.currentInstance
        return cls.currentInstance

    def __init__(self, parent=None):
        super(ControlPrintSelectWindow, self).__init__(parent)
        self.ui =  Ui_MainWindow()
        self.ui.setupUi(self)

