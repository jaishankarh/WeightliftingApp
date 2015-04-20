# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_compdialog.ui'
#
# Created: Fri Dec 19 14:50:12 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from PySide.QtCore import *
from PySide.QtGui import *
from utils.db_classes import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.Dialog = Dialog
        self.session = session
        Dialog.setObjectName("Dialog")
        Dialog.resize(503, 469)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(100, 410, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayoutWidget = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 20, 331, 141))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_lbl = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.main_lbl.setFont(font)
        self.main_lbl.setTextFormat(QtCore.Qt.RichText)
        self.main_lbl.setObjectName("main_lbl")
        self.verticalLayout.addWidget(self.main_lbl)
        self.line = QtGui.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.name_lbl = QtGui.QLabel(self.verticalLayoutWidget)
        self.name_lbl.setObjectName("name_lbl")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.name_lbl)
        self.nameEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.nameEdit.setObjectName("nameEdit")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.nameEdit)
        self.year_lbl = QtGui.QLabel(self.verticalLayoutWidget)
        self.year_lbl.setObjectName("year_lbl")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.year_lbl)
        self.yearEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.yearEdit.setObjectName("yearEdit")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.yearEdit)
        self.verticalLayout.addLayout(self.formLayout)
        self.save_btn = QtGui.QPushButton(self.Dialog)
        self.save_btn.setGeometry(QtCore.QRect(280, 180, 80, 23))
        self.save_btn.setObjectName("save_btn")
        self.savedComp = False
        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.verticalLayout.addWidget(self.label_4)


        self.retranslateUi(Dialog)
        self.save_btn.clicked.connect(self.saveComp)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "New Competition", None, QtGui.QApplication.UnicodeUTF8))
        self.main_lbl.setText(QtGui.QApplication.translate("Dialog", "Add a new competition", None, QtGui.QApplication.UnicodeUTF8))
        self.name_lbl.setText(QtGui.QApplication.translate("Dialog", "Name:  ", None, QtGui.QApplication.UnicodeUTF8))
        self.year_lbl.setText(QtGui.QApplication.translate("Dialog", "Year:", None, QtGui.QApplication.UnicodeUTF8))
        self.save_btn.setText(QtGui.QApplication.translate("Dialog", "Save", None, QtGui.QApplication.UnicodeUTF8))


    def saveComp(self):
        name = self.nameEdit.text()
        year = self.yearEdit.text()

        print(name == "")
        if name != "" and year != "":
            if year.isdigit():
                self.curr_comp = Competition(name=name, year=year)
                self.session = session
                try:
                    self.session.add(self.curr_comp )
                    self.session.commit()
                    self.savedComp=True
                except:
                    self.session.rollback()
                    QMessageBox.critical(self.Dialog, "Error", "Sorry there was an unseen critical database error, could not save the competition!", QMessageBox.Ok)
                    QtGui.QDialog.reject(self)
                    return

            else:
                self.label_4.setText("<font color=red>Year has to be numeric</font>")
        else:
            self.label_4.setText("<font color=red>The name or year cannot be left blank</font>")

        if not self.savedComp:
            return
        self.verticalLayoutWidget_2 = QtGui.QWidget(self.Dialog)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(30, 220, 441, 189))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtGui.QLabel(self.verticalLayoutWidget_2)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.line_2 = QtGui.QFrame(self.verticalLayoutWidget_2)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.coeffs_lbl = QtGui.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.coeffs_lbl.setFont(font)
        self.coeffs_lbl.setObjectName("coeffs_lbl")
        self.verticalLayout_2.addWidget(self.coeffs_lbl)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lift_type_box = QtGui.QComboBox(self.verticalLayoutWidget_2)
        self.lift_type_box.setObjectName("lift_type_box")
        ls = self.session.query(Lift_Type.liftType).distinct()
        print(ls)
        #ls = [("Olympic Lift", "Snatch"), ("Power Lift", "Squat")]
        self.liftypes = []
        for l in ls:
            self.liftypes.append(l[0])
        self.lift_type_box.insertItems(0, self.liftypes)
        self.horizontalLayout.addWidget(self.lift_type_box)
        self.AEdit = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.AEdit.setObjectName("AEdit")
        self.horizontalLayout.addWidget(self.AEdit)
        self.BEdit = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.BEdit.setObjectName("BEdit")
        self.horizontalLayout.addWidget(self.BEdit)
        self.CEdit = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.CEdit.setObjectName("CEdit")
        self.horizontalLayout.addWidget(self.CEdit)
        self.DEdit = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.DEdit.setObjectName("DEdit")
        self.horizontalLayout.addWidget(self.DEdit)
        self.EEdit = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.EEdit.setObjectName("EEdit")
        self.horizontalLayout.addWidget(self.EEdit)
        self.FEdit = QtGui.QLineEdit(self.verticalLayoutWidget_2)
        self.FEdit.setObjectName("FEdit")
        self.horizontalLayout.addWidget(self.FEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.add_btn = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.add_btn.setObjectName("add_btn")
        self.horizontalLayout_3.addWidget(self.add_btn)
        self.del_btn = QtGui.QPushButton(self.verticalLayoutWidget_2)
        self.del_btn.setObjectName("del_btn")
        self.horizontalLayout_3.addWidget(self.del_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.tableView = QtGui.QTableView(self.verticalLayoutWidget_2)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_2.addWidget(self.tableView)
        self.Dialog.layout().addWidget(self.verticalLayoutWidget_2)


        self.label.setText(QtGui.QApplication.translate("Dialog", "Hint: Save the competition details first. Every competition can have only one set of coefficients for a given lift type.", None, QtGui.QApplication.UnicodeUTF8))
        self.coeffs_lbl.setText(QtGui.QApplication.translate("Dialog", "Coefficients for this competition", None, QtGui.QApplication.UnicodeUTF8))
        self.AEdit.setPlaceholderText(QtGui.QApplication.translate("Dialog", "A", None, QtGui.QApplication.UnicodeUTF8))
        self.BEdit.setPlaceholderText(QtGui.QApplication.translate("Dialog", "B", None, QtGui.QApplication.UnicodeUTF8))
        self.CEdit.setPlaceholderText(QtGui.QApplication.translate("Dialog", "C", None, QtGui.QApplication.UnicodeUTF8))
        self.DEdit.setPlaceholderText(QtGui.QApplication.translate("Dialog", "D", None, QtGui.QApplication.UnicodeUTF8))
        self.EEdit.setPlaceholderText(QtGui.QApplication.translate("Dialog", "E", None, QtGui.QApplication.UnicodeUTF8))
        self.FEdit.setPlaceholderText(QtGui.QApplication.translate("Dialog", "F", None, QtGui.QApplication.UnicodeUTF8))
        self.add_btn.setText(QtGui.QApplication.translate("Dialog", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.del_btn.setText(QtGui.QApplication.translate("Dialog", "Delete", None, QtGui.QApplication.UnicodeUTF8))



class ControlNewCompDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(ControlNewCompDialog, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    ################## proper validation to be done message box to be popped up
    def accept(self, *args, **kwargs):
        print("I was here accept")




    def reject(self, *args, **kwargs):
        QtGui.QDialog.reject(self)
        print("I was here reject")

