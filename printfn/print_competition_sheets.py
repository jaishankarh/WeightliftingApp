# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'print_competition_sheets.ui'
#
# Created: Wed Dec 17 15:55:16 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_print_win(object):
    def setupUi(self, print_win):
        print_win.setObjectName("print_win")
        print_win.resize(800, 600)
        self.centralwidget = QtGui.QWidget(print_win)
        self.centralwidget.setObjectName("centralwidget")
        self.table_select = QtGui.QComboBox(self.centralwidget)
        self.table_select.setGeometry(QtCore.QRect(160, 10, 151, 23))
        self.table_select.setObjectName("table_select")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 10, 101, 16))
        self.label.setObjectName("label")
        self.print_btn = QtGui.QPushButton(self.centralwidget)
        self.print_btn.setGeometry(QtCore.QRect(609, 530, 141, 23))
        self.print_btn.setObjectName("print_btn")
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 40, 701, 481))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.choose_lbl = QtGui.QLabel(self.verticalLayoutWidget)
        self.choose_lbl.setObjectName("choose_lbl")
        self.horizontalLayout.addWidget(self.choose_lbl)
        self.choose_table_box = QtGui.QComboBox(self.verticalLayoutWidget)
        self.choose_table_box.setObjectName("choose_table_box")
        self.horizontalLayout.addWidget(self.choose_table_box)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.comp_yearEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.comp_yearEdit.setObjectName("comp_yearEdit")
        self.horizontalLayout_2.addWidget(self.comp_yearEdit)
        self.fromYearEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.fromYearEdit.setObjectName("fromYearEdit")
        self.horizontalLayout_2.addWidget(self.fromYearEdit)
        self.toYearEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.toYearEdit.setObjectName("toYearEdit")
        self.horizontalLayout_2.addWidget(self.toYearEdit)
        self.comboBox_2 = QtGui.QComboBox(self.verticalLayoutWidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout_2.addWidget(self.comboBox_2)
        self.filter_btn = QtGui.QPushButton(self.verticalLayoutWidget)
        self.filter_btn.setObjectName("filter_btn")
        self.horizontalLayout_2.addWidget(self.filter_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.tableView = QtGui.QTableView(self.verticalLayoutWidget)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_2.addWidget(self.tableView)
        print_win.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(print_win)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        print_win.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(print_win)
        self.statusbar.setObjectName("statusbar")
        print_win.setStatusBar(self.statusbar)

        self.retranslateUi(print_win)
        QtCore.QMetaObject.connectSlotsByName(print_win)

    def retranslateUi(self, print_win):
        print_win.setWindowTitle(QtGui.QApplication.translate("print_win", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("print_win", "Choose Table", None, QtGui.QApplication.UnicodeUTF8))
        self.print_btn.setText(QtGui.QApplication.translate("print_win", "Print", None, QtGui.QApplication.UnicodeUTF8))
        self.choose_lbl.setText(QtGui.QApplication.translate("print_win", "Choose :", None, QtGui.QApplication.UnicodeUTF8))
        self.comp_yearEdit.setPlaceholderText(QtGui.QApplication.translate("print_win", "Competition Year", None, QtGui.QApplication.UnicodeUTF8))
        self.fromYearEdit.setPlaceholderText(QtGui.QApplication.translate("print_win", "From Year", None, QtGui.QApplication.UnicodeUTF8))
        self.toYearEdit.setPlaceholderText(QtGui.QApplication.translate("print_win", "To Year", None, QtGui.QApplication.UnicodeUTF8))
        self.filter_btn.setText(QtGui.QApplication.translate("print_win", "Filter", None, QtGui.QApplication.UnicodeUTF8))

