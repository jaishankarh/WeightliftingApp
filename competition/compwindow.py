# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'compwindow.ui'
#
# Created: Thu Oct 30 16:28:55 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

import sys

class Ui_CompWindow(object):
    def setupUi(self, Ui_CompWindow):
        Ui_CompWindow.setObjectName("Ui_CompWindow")
        Ui_CompWindow.resize(800, 600)
        self.centralWidget = QtGui.QWidget(Ui_CompWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayoutWidget = QtGui.QWidget(self.centralWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 10, 761, 531))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.main_options = QtGui.QHBoxLayout()
        self.main_options.setObjectName("main_options")
        self.enter_results = QtGui.QPushButton(self.verticalLayoutWidget)
        self.enter_results.setObjectName("enter_results")
        self.main_options.addWidget(self.enter_results)
        self.edit = QtGui.QPushButton(self.verticalLayoutWidget)
        self.edit.setObjectName("edit")
        self.main_options.addWidget(self.edit)
        self.pushButton_3 = QtGui.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.main_options.addWidget(self.pushButton_3)
        self.verticalLayout_2.addLayout(self.main_options)
        self.f_input = QtGui.QHBoxLayout()
        self.f_input.setObjectName("f_input")
        self.member_lbl = QtGui.QLabel(self.verticalLayoutWidget)
        self.member_lbl.setObjectName("member_lbl")
        self.f_input.addWidget(self.member_lbl)
        self.memberEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.memberEdit.setObjectName("memberEdit")
        self.f_input.addWidget(self.memberEdit)
        self.weight_lbl = QtGui.QLabel(self.verticalLayoutWidget)
        self.weight_lbl.setObjectName("weight_lbl")
        self.f_input.addWidget(self.weight_lbl)
        self.weightEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.weightEdit.sizePolicy().hasHeightForWidth())
        self.weightEdit.setSizePolicy(sizePolicy)
        self.weightEdit.setObjectName("weightEdit")
        self.f_input.addWidget(self.weightEdit)
        self.year_lbl = QtGui.QLabel(self.verticalLayoutWidget)
        self.year_lbl.setObjectName("year_lbl")
        self.f_input.addWidget(self.year_lbl)
        self.lineEdit_3 = QtGui.QLineEdit(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.f_input.addWidget(self.lineEdit_3)
        self.dateEdit = QtGui.QDateEdit(self.verticalLayoutWidget)
        self.dateEdit.setObjectName("dateEdit")
        self.f_input.addWidget(self.dateEdit)

        self.verticalLayout_2.addLayout(self.f_input)
        self.sec_input = QtGui.QHBoxLayout()
        self.sec_input.setObjectName("sec_input")
        self.lift_lbl = QtGui.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lift_lbl.sizePolicy().hasHeightForWidth())
        self.lift_lbl.setSizePolicy(sizePolicy)
        self.lift_lbl.setObjectName("lift_lbl")
        self.sec_input.addWidget(self.lift_lbl)
        self.liftBox = QtGui.QComboBox(self.verticalLayoutWidget)
        self.liftBox.setObjectName("liftBox")
        self.sec_input.addWidget(self.liftBox)
        spacerItem = QtGui.QSpacerItem(200, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.sec_input.addItem(spacerItem)
        self.save = QtGui.QPushButton(self.verticalLayoutWidget)
        self.save.setObjectName("save")
        self.sec_input.addWidget(self.save)
        self.verticalLayout_2.addLayout(self.sec_input)
        spacerItem1 = QtGui.QSpacerItem(20, 100, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem1)
        self.tableView = QtGui.QTableView(self.verticalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.verticalHeader().setStretchLastSection(True)
        self.verticalLayout_2.addWidget(self.tableView)
        Ui_CompWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(Ui_CompWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menuBar.setObjectName("menuBar")
        Ui_CompWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(Ui_CompWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        Ui_CompWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(Ui_CompWindow)
        self.statusBar.setObjectName("statusBar")
        Ui_CompWindow.setStatusBar(self.statusBar)

        self.retranslateUi(Ui_CompWindow)
        QtCore.QMetaObject.connectSlotsByName(Ui_CompWindow)

    def retranslateUi(self, Ui_CompWindow):
        Ui_CompWindow.setWindowTitle(QtGui.QApplication.translate("Ui_CompWindow", "Ui_CompWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.enter_results.setText(QtGui.QApplication.translate("Ui_CompWindow", "Enter Results", None, QtGui.QApplication.UnicodeUTF8))
        self.edit.setText(QtGui.QApplication.translate("Ui_CompWindow", "View", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("Ui_CompWindow", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.member_lbl.setText(QtGui.QApplication.translate("Ui_CompWindow", "Member", None, QtGui.QApplication.UnicodeUTF8))
        self.weight_lbl.setText(QtGui.QApplication.translate("Ui_CompWindow", "Weight", None, QtGui.QApplication.UnicodeUTF8))
        self.year_lbl.setText(QtGui.QApplication.translate("Ui_CompWindow", "Year", None, QtGui.QApplication.UnicodeUTF8))
        self.lift_lbl.setText(QtGui.QApplication.translate("Ui_CompWindow", "Lift", None, QtGui.QApplication.UnicodeUTF8))
        self.save.setText(QtGui.QApplication.translate("Ui_CompWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))


class ControlMainWindow(QtGui.QMainWindow):
  def __init__(self, parent=None):
    super(ControlMainWindow, self).__init__(parent)
    self.ui =  Ui_CompWindow()
    self.ui.setupUi(self)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mySW = ControlMainWindow()
    mySW.show()
    sys.exit(app.exec_())