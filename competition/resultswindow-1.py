# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resultswindow.ui'
#
# Created: Sat Dec 13 11:22:12 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_ResultsWindow(object):
    def setupUi(self, ResultsWindow):
        ResultsWindow.setObjectName("ResultsWindow")
        ResultsWindow.resize(800, 600)
        self.centralWidget = QtGui.QWidget(ResultsWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.back_btn = QtGui.QPushButton(self.centralWidget)
        self.back_btn.setGeometry(QtCore.QRect(30, 30, 80, 23))
        self.back_btn.setObjectName("back_btn")
        self.tableView = QtGui.QTableView(self.centralWidget)
        self.tableView.setGeometry(QtCore.QRect(40, 231, 721, 301))
        self.tableView.setObjectName("tableView")
        self.lift_type = QtGui.QComboBox(self.centralWidget)
        self.lift_type.setGeometry(QtCore.QRect(60, 90, 191, 23))
        self.lift_type.setEditable(False)
        self.lift_type.setCurrentText("")
        self.lift_type.setObjectName("lift_type")
        self.lift_name = QtGui.QComboBox(self.centralWidget)
        self.lift_name.setGeometry(QtCore.QRect(390, 90, 191, 23))
        self.lift_name.setEditable(False)
        self.lift_name.setCurrentText("")
        self.lift_name.setObjectName("lift_name")
        self.member_box = QtGui.QComboBox(self.centralWidget)
        self.member_box.setGeometry(QtCore.QRect(60, 150, 261, 23))
        self.member_box.setEditable(True)
        self.member_box.setObjectName("member_box")
        self.bdy_weight_btn = QtGui.QLineEdit(self.centralWidget)
        self.bdy_weight_btn.setGeometry(QtCore.QRect(340, 150, 91, 23))
        self.bdy_weight_btn.setObjectName("bdy_weight_btn")
        self.dateEdit = QtGui.QDateEdit(self.centralWidget)
        self.dateEdit.setGeometry(QtCore.QRect(610, 150, 110, 24))
        self.dateEdit.setObjectName("dateEdit")
        self.comp_name_lbl = QtGui.QLabel(self.centralWidget)
        self.comp_name_lbl.setGeometry(QtCore.QRect(190, 20, 251, 16))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comp_name_lbl.sizePolicy().hasHeightForWidth())
        self.comp_name_lbl.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comp_name_lbl.setFont(font)
        self.comp_name_lbl.setObjectName("comp_name_lbl")
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(590, 0, 89, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.year_val = QtGui.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.year_val.setFont(font)
        self.year_val.setObjectName("year_val")
        self.horizontalLayout.addWidget(self.year_val)
        self.label_4 = QtGui.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.save_btn = QtGui.QPushButton(self.centralWidget)
        self.save_btn.setGeometry(QtCore.QRect(449, 190, 111, 23))
        self.save_btn.setObjectName("save_btn")
        self.lift_weight = QtGui.QLineEdit(self.centralWidget)
        self.lift_weight.setGeometry(QtCore.QRect(460, 150, 113, 23))
        self.lift_weight.setObjectName("lift_weight")
        self.del_btn = QtGui.QPushButton(self.centralWidget)
        self.del_btn.setGeometry(QtCore.QRect(590, 190, 141, 23))
        self.del_btn.setObjectName("del_btn")
        self.choose_type_lbl = QtGui.QLabel(self.centralWidget)
        self.choose_type_lbl.setGeometry(QtCore.QRect(60, 70, 131, 16))
        self.choose_type_lbl.setObjectName("choose_type_lbl")
        self.lift_name_lbl = QtGui.QLabel(self.centralWidget)
        self.lift_name_lbl.setGeometry(QtCore.QRect(400, 70, 131, 16))
        self.lift_name_lbl.setObjectName("lift_name_lbl")
        self.mem_lbl = QtGui.QLabel(self.centralWidget)
        self.mem_lbl.setGeometry(QtCore.QRect(60, 130, 57, 15))
        self.mem_lbl.setObjectName("mem_lbl")
        self.bdy_wt_lbl = QtGui.QLabel(self.centralWidget)
        self.bdy_wt_lbl.setGeometry(QtCore.QRect(340, 130, 81, 16))
        self.bdy_wt_lbl.setObjectName("bdy_wt_lbl")
        self.lift_nm_lbl = QtGui.QLabel(self.centralWidget)
        self.lift_nm_lbl.setGeometry(QtCore.QRect(460, 130, 71, 16))
        self.lift_nm_lbl.setObjectName("lift_nm_lbl")
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.centralWidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(50, 190, 259, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.checkBox = QtGui.QCheckBox(self.horizontalLayoutWidget_2)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_2.addWidget(self.checkBox)
        self.dateEdit_2 = QtGui.QDateEdit(self.horizontalLayoutWidget_2)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.horizontalLayout_2.addWidget(self.dateEdit_2)
        ResultsWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(ResultsWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menuBar.setObjectName("menuBar")
        ResultsWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(ResultsWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        ResultsWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(ResultsWindow)
        self.statusBar.setObjectName("statusBar")
        ResultsWindow.setStatusBar(self.statusBar)

        self.retranslateUi(ResultsWindow)
        QtCore.QMetaObject.connectSlotsByName(ResultsWindow)

    def retranslateUi(self, ResultsWindow):
        ResultsWindow.setWindowTitle(QtGui.QApplication.translate("ResultsWindow", "ResultsWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.back_btn.setText(QtGui.QApplication.translate("ResultsWindow", "Back", None, QtGui.QApplication.UnicodeUTF8))
        self.bdy_weight_btn.setInputMask(QtGui.QApplication.translate("ResultsWindow", "000.00 Kg", None, QtGui.QApplication.UnicodeUTF8))
        self.comp_name_lbl.setText(QtGui.QApplication.translate("ResultsWindow", "Current Competition", None, QtGui.QApplication.UnicodeUTF8))
        self.year_val.setText(QtGui.QApplication.translate("ResultsWindow", "Year:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ResultsWindow", "2009", None, QtGui.QApplication.UnicodeUTF8))
        self.save_btn.setText(QtGui.QApplication.translate("ResultsWindow", "Save Result", None, QtGui.QApplication.UnicodeUTF8))
        self.lift_weight.setInputMask(QtGui.QApplication.translate("ResultsWindow", "000.00 Kg", None, QtGui.QApplication.UnicodeUTF8))
        self.del_btn.setText(QtGui.QApplication.translate("ResultsWindow", "Delete Selected", None, QtGui.QApplication.UnicodeUTF8))
        self.choose_type_lbl.setText(QtGui.QApplication.translate("ResultsWindow", "Choose Lift Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.lift_name_lbl.setText(QtGui.QApplication.translate("ResultsWindow", "Choose Lift Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.mem_lbl.setText(QtGui.QApplication.translate("ResultsWindow", "Member", None, QtGui.QApplication.UnicodeUTF8))
        self.bdy_wt_lbl.setText(QtGui.QApplication.translate("ResultsWindow", "Body Weight", None, QtGui.QApplication.UnicodeUTF8))
        self.lift_nm_lbl.setText(QtGui.QApplication.translate("ResultsWindow", "Lift Weight", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("ResultsWindow", "Filter by Date", None, QtGui.QApplication.UnicodeUTF8))

