# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'memberswindow.ui'
#
# Created: Fri Oct 24 10:47:33 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from PySide.QtGui import QMainWindow
import sys

class Ui_MembersWindow(object):
    def setupUi(self, MembersWindow):
        MembersWindow.setObjectName("MembersWindow")
        MembersWindow.resize(800, 600)
        MembersWindow.setMinimumSize(QtCore.QSize(0, 0))
        self.centralWidget = QtGui.QWidget(MembersWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.tableView = QtGui.QTableView(self.centralWidget)
        self.tableView.setGeometry(QtCore.QRect(20, 140, 761, 401))
        self.tableView.setObjectName("tableView")
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 759, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_btn = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.add_btn.setMinimumSize(QtCore.QSize(0, 8))
        self.add_btn.setObjectName("add_btn")
        self.horizontalLayout.addWidget(self.add_btn)
        self.update_btn = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.update_btn.setObjectName("update_btn")
        self.horizontalLayout.addWidget(self.update_btn)
        self.del_btn = QtGui.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.del_btn.sizePolicy().hasHeightForWidth())
        self.del_btn.setSizePolicy(sizePolicy)
        self.del_btn.setMinimumSize(QtCore.QSize(0, 0))
        self.del_btn.setObjectName("del_btn")
        self.horizontalLayout.addWidget(self.del_btn)
        self.search_btn = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.search_btn.setObjectName("search_btn")
        self.horizontalLayout.addWidget(self.search_btn)
        self.print_btn = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.print_btn.setMinimumSize(QtCore.QSize(0, 8))
        self.print_btn.setObjectName("print_btn")
        self.horizontalLayout.addWidget(self.print_btn)
        self.horizontalLayoutWidget_7 = QtGui.QWidget(self.centralWidget)
        self.horizontalLayoutWidget_7.setGeometry(QtCore.QRect(20, 50, 741, 80))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.all_fields = QtGui.QHBoxLayout(self.horizontalLayoutWidget_7)
        self.all_fields.setContentsMargins(0, 0, 0, 0)
        self.all_fields.setObjectName("all_fields")
        self.names = QtGui.QVBoxLayout()
        self.names.setObjectName("names")
        self.fname_lay = QtGui.QHBoxLayout()
        self.fname_lay.setObjectName("fname_lay")
        self.fname_lbl = QtGui.QLabel(self.horizontalLayoutWidget_7)
        self.fname_lbl.setObjectName("fname_lbl")
        self.fname_lay.addWidget(self.fname_lbl)
        self.fname = QtGui.QLineEdit(self.horizontalLayoutWidget_7)
        self.fname.setObjectName("fname")
        self.fname_lay.addWidget(self.fname)
        self.names.addLayout(self.fname_lay)
        self.lname_lay = QtGui.QHBoxLayout()
        self.lname_lay.setObjectName("lname_lay")
        self.lname_lbl = QtGui.QLabel(self.horizontalLayoutWidget_7)
        self.lname_lbl.setObjectName("lname_lbl")
        self.lname_lay.addWidget(self.lname_lbl)
        self.lname = QtGui.QLineEdit(self.horizontalLayoutWidget_7)
        self.lname.setObjectName("lname")
        self.lname_lay.addWidget(self.lname)
        self.names.addLayout(self.lname_lay)
        self.all_fields.addLayout(self.names)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.grp_gen = QtGui.QVBoxLayout()
        self.grp_gen.setObjectName("grp_gen")
        self.grp_lay = QtGui.QHBoxLayout()
        self.grp_lay.setObjectName("grp_lay")
        self.grp_lbl = QtGui.QLabel(self.horizontalLayoutWidget_7)
        self.grp_lbl.setObjectName("grp_lbl")
        self.grp_lay.addWidget(self.grp_lbl)
        self.group = QtGui.QComboBox(self.horizontalLayoutWidget_7)
        self.group.setObjectName("group")
        self.grp_lay.addWidget(self.group)
        self.grp_gen.addLayout(self.grp_lay)
        self.gen = QtGui.QHBoxLayout()
        self.gen.setObjectName("gen")
        self.gen_lbl = QtGui.QLabel(self.horizontalLayoutWidget_7)
        self.gen_lbl.setObjectName("gen_lbl")
        self.gen.addWidget(self.gen_lbl)
        self.gender = QtGui.QComboBox(self.horizontalLayoutWidget_7)
        self.gender.setObjectName("gender")
        self.gen.addWidget(self.gender)
        self.grp_gen.addLayout(self.gen)
        self.horizontalLayout_6.addLayout(self.grp_gen)
        self.label_5 = QtGui.QLabel(self.horizontalLayoutWidget_7)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.dateEdit = QtGui.QDateEdit(self.horizontalLayoutWidget_7)
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout_6.addWidget(self.dateEdit)
        self.all_fields.addLayout(self.horizontalLayout_6)
        MembersWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MembersWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menuBar.setObjectName("menuBar")
        MembersWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MembersWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MembersWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MembersWindow)
        self.statusBar.setObjectName("statusBar")
        MembersWindow.setStatusBar(self.statusBar)
        self.toolBar = QtGui.QToolBar(MembersWindow)
        self.toolBar.setObjectName("toolBar")
        MembersWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MembersWindow)
        QtCore.QMetaObject.connectSlotsByName(MembersWindow)

    def retranslateUi(self, MembersWindow):
        MembersWindow.setWindowTitle(QtGui.QApplication.translate("MembersWindow", "TrainingWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.add_btn.setText(QtGui.QApplication.translate("MembersWindow", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.update_btn.setText(QtGui.QApplication.translate("MembersWindow", "Update", None, QtGui.QApplication.UnicodeUTF8))
        self.del_btn.setText(QtGui.QApplication.translate("MembersWindow", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.search_btn.setText(QtGui.QApplication.translate("MembersWindow", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.print_btn.setText(QtGui.QApplication.translate("MembersWindow", "Print", None, QtGui.QApplication.UnicodeUTF8))
        self.fname_lbl.setText(QtGui.QApplication.translate("MembersWindow", "First Name", None, QtGui.QApplication.UnicodeUTF8))
        self.lname_lbl.setText(QtGui.QApplication.translate("MembersWindow", "Last Name", None, QtGui.QApplication.UnicodeUTF8))
        self.grp_lbl.setText(QtGui.QApplication.translate("MembersWindow", "Group", None, QtGui.QApplication.UnicodeUTF8))
        self.gen_lbl.setText(QtGui.QApplication.translate("MembersWindow", "Gender", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MembersWindow", "Date of Birth", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MembersWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))


# class ControlMembersWindow(QMainWindow):
#
#     currentInstance = None
#
#     @classmethod
#     def getCurrentInstance(cls):
#         if cls.currentInstance is None:
#             currentInstance = ControlMembersWindow()
#             print("I was here")
#             return currentInstance
#         return cls.currentInstance
#
#     def __init__(self, parent=None):
#         super(ControlMembersWindow, self).__init__(parent)
#         self.ui =  Ui_MembersWindow()
#         self.ui.setupUi(self)

class ControlMainWindow(QtGui.QMainWindow):
  def __init__(self, parent=None):
    super(ControlMainWindow, self).__init__(parent)
    self.ui =  Ui_MembersWindow()
    self.ui.setupUi(self)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mySW = ControlMainWindow()
    mySW.show()
    sys.exit(app.exec_())