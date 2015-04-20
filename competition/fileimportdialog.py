# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fileimportdialog.ui'
#
# Created: Sat Jan 24 11:19:17 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
import sys
import threading
from PySide.QtCore import *
from PySide.QtGui import QHeaderView
from PySide.QtGui import *
from PySide.QtSql import *
from PySide.QtCore import Signal
from utils.database_api import *
import operator
from PySide import QtSql
from utils.db_classes import*
import xlrd
#from members.manageMembers import AddMemberWidget

from utils.utils import *

class Ui_FileImportDialog(object):
    def setupUi(self, Dialog, callback1, callback2):
        self.callback1 = callback1
        self.callback2 = callback2
        self.Dialog = Dialog
        Dialog.setObjectName("Dialog")
        Dialog.resize(320, 240)
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 30, 221, 161))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.genFileImport = QtGui.QPushButton(self.verticalLayoutWidget)
        self.genFileImport.setObjectName("genFileImport")
        self.verticalLayout.addWidget(self.genFileImport)
        self.pushButton_2 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        Dialog.setModal(True)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.genFileImport.clicked.connect(self.gen_file_import);
        self.pushButton_2.clicked.connect(self.con_import);

    def gen_file_import(self):
        self.callback1()
        self.Dialog.close()

    def con_import(self):
        self.callback2()
        self.Dialog.close()

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.genFileImport.setText(QtGui.QApplication.translate("Dialog", "Generate File for Import", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Dialog", "Import from file", None, QtGui.QApplication.UnicodeUTF8))





class ControlFileImportDialog(QDialog):

    currentInstance = None

    @classmethod
    def getCurrentInstance(cls):
        if cls.currentInstance is None:
            cls.currentInstance = ControlFileImportDialog()
            print("I was here")
            return cls.currentInstance
        return cls.currentInstance

    def __init__(self, callback1, callback2, parent=None):
        super(ControlFileImportDialog, self).__init__(parent)
        self.ui =  Ui_FileImportDialog()
        self.ui.setupUi(self, callback1, callback2)


