# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_compdialog.ui'
#
# Created: Fri Dec 19 15:22:26 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from PySide.QtCore import *
from PySide.QtGui import *
from utils.db_classes import *
from utils.utils import *

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.Dialog = Dialog
        self.session = session
        Dialog.setObjectName("Dialog")
        Dialog.resize(503, 469)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(140, 410, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayoutWidget_3 = QtGui.QWidget(Dialog)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(30, 20, 451, 381))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.mainLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget_3)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.setObjectName("mainLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_lbl = QtGui.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.main_lbl.setFont(font)
        self.main_lbl.setTextFormat(QtCore.Qt.RichText)
        self.main_lbl.setObjectName("main_lbl")
        self.verticalLayout.addWidget(self.main_lbl)
        self.line = QtGui.QFrame(self.verticalLayoutWidget_3)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.name_lbl = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.name_lbl.setObjectName("name_lbl")
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.name_lbl)
        self.nameEdit = QtGui.QLineEdit(self.verticalLayoutWidget_3)
        self.nameEdit.setObjectName("nameEdit")
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.nameEdit)
        self.year_lbl = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.year_lbl.setObjectName("year_lbl")
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.year_lbl)
        self.yearEdit = QtGui.QLineEdit(self.verticalLayoutWidget_3)
        self.yearEdit.setObjectName("yearEdit")
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.yearEdit)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.save_btn = QtGui.QPushButton(self.verticalLayoutWidget_3)
        self.save_btn.setObjectName("save_btn")
        self.horizontalLayout_2.addWidget(self.save_btn)
        self.formLayout.setLayout(3, QtGui.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.error_lbl = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.error_lbl.setText("")
        self.error_lbl.setObjectName("error_lbl")
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.error_lbl)
        self.verticalLayout.addLayout(self.formLayout)
        self.mainLayout.addLayout(self.verticalLayout)
        self.savedComp = False

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
                comps = self.session.query(Competition).filter(Competition.year == year).first()
                if comps is not None:
                    QMessageBox.critical(self.Dialog, "Duplicate Entries", "Sorry an entry for this year already exists, you could select it in the list and update it!", QMessageBox.Ok)
                    return

                self.curr_comp = Competition(name=name, year=year)

                try:
                    self.session.add(self.curr_comp )
                    self.session.commit()
                    self.savedComp=True
                    self.error_lbl.setText("")
                except:
                    self.session.rollback()
                    QMessageBox.critical(self.Dialog, "Error", "Sorry there was an unforeseen critical database error, could not save the competition!", QMessageBox.Ok)
                    QtGui.QDialog.reject(self)
                    return

            else:
                self.error_lbl.setText("<font color=red>Year has to be numeric</font>")
        else:
            self.error_lbl.setText("<font color=red>The name or year cannot be left blank</font>")

        if not self.savedComp:
            return

        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.hint_lbl = QtGui.QLabel(self.verticalLayoutWidget_3)
        self.hint_lbl.setWordWrap(True)
        self.hint_lbl.setObjectName("hint_lbl")
        self.verticalLayout_2.addWidget(self.hint_lbl)
        self.line_2 = QtGui.QFrame(self.verticalLayoutWidget_3)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.coeffs_lbl = QtGui.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.coeffs_lbl.setFont(font)
        self.coeffs_lbl.setObjectName("coeffs_lbl")
        self.verticalLayout_2.addWidget(self.coeffs_lbl)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lift_type_box = QtGui.QComboBox(self.verticalLayoutWidget_3)
        self.lift_type_box.setObjectName("lift_type_box")
        ls = self.session.query(Lift_Type.liftType).distinct()
        print(ls)
        #ls = [("Olympic Lift", "Snatch"), ("Power Lift", "Squat")]
        self.liftypes = []
        for l in ls:
            self.liftypes.append(l[0])
        self.lift_type_box.insertItems(0, self.liftypes)
        self.horizontalLayout.addWidget(self.lift_type_box)
        self.gender_box = QtGui.QComboBox(self.verticalLayoutWidget_3)
        self.gender_box.setObjectName("gender_box")
        self.gender_box_opts = ["Male", "Female", "Other"]
        self.gender_box.insertItems(0, self.gender_box_opts)
        self.horizontalLayout.addWidget(self.gender_box)
        self.AEdit = QtGui.QLineEdit(self.verticalLayoutWidget_3)
        self.AEdit.setObjectName("AEdit")
        self.floatValidator = QDoubleValidator(self.Dialog)
        self.AEdit.setValidator(self.floatValidator)
        self.horizontalLayout.addWidget(self.AEdit)
        self.BEdit = QtGui.QLineEdit(self.verticalLayoutWidget_3)
        self.BEdit.setValidator(self.floatValidator)
        self.BEdit.setObjectName("BEdit")
        self.horizontalLayout.addWidget(self.BEdit)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.CEdit = QtGui.QLineEdit(self.verticalLayoutWidget_3)
        self.CEdit.setValidator(self.floatValidator)
        self.CEdit.setObjectName("CEdit")
        self.horizontalLayout_4.addWidget(self.CEdit)
        self.DEdit = QtGui.QLineEdit(self.verticalLayoutWidget_3)
        self.DEdit.setValidator(self.floatValidator)
        self.DEdit.setObjectName("DEdit")
        self.horizontalLayout_4.addWidget(self.DEdit)
        self.EEdit = QtGui.QLineEdit(self.verticalLayoutWidget_3)
        self.EEdit.setValidator(self.floatValidator)
        self.EEdit.setObjectName("EEdit")
        self.horizontalLayout_4.addWidget(self.EEdit)
        self.FEdit = QtGui.QLineEdit(self.verticalLayoutWidget_3)
        self.FEdit.setValidator(self.floatValidator)
        self.FEdit.setObjectName("FEdit")
        self.horizontalLayout_4.addWidget(self.FEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.add_btn = QtGui.QPushButton(self.verticalLayoutWidget_3)
        self.add_btn.setObjectName("add_btn")
        self.horizontalLayout_3.addWidget(self.add_btn)
        self.del_btn = QtGui.QPushButton(self.verticalLayoutWidget_3)
        self.del_btn.setObjectName("del_btn")
        self.horizontalLayout_3.addWidget(self.del_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.tableView = QtGui.QTableView(self.verticalLayoutWidget_3)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_2.addWidget(self.tableView)
        self.mainLayout.addLayout(self.verticalLayout_2)

        self.header_data = ["Lift Type", "Competition Year", "Gender", "A", "B", "C", "D", "E", "F"]
        self.data = []

        for instance in self.session.query(Coefficient).filter(Coefficient.year == self.curr_comp.year):
            self.data.append((instance.liftType, instance.year, instance.gender, instance.a, instance.b, instance.c, instance.d, instance.e, instance.f))


        self.model =  MyTableModel(self.Dialog, self.data, self.header_data)
        self.tableView.setModel(self.model)

        #self.tableView.hideColumn(0) #hide column 'id'
        # self.tableView.horizontalHeader().stretchLastSection()
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows) #select Row
        self.tableView.setSelectionMode(QAbstractItemView.MultiSelection) #enable multiselect
        self.tableView.setSortingEnabled(True)
        self.tableView.sortByColumn(0, Qt.AscendingOrder)
        self.tableView.resizeColumnsToContents()
        header = self.tableView.horizontalHeader()
        header.setStretchLastSection(True)


        self.add_btn.clicked.connect(self.add_btn_clicked)

        self.hint_lbl.setText(QtGui.QApplication.translate("Dialog", "Hint: Save the competition details first. Every competition can have only one set of coefficients for a given lift type.", None, QtGui.QApplication.UnicodeUTF8))
        self.coeffs_lbl.setText(QtGui.QApplication.translate("Dialog", "Coefficients for this competition", None, QtGui.QApplication.UnicodeUTF8))
        self.AEdit.setPlaceholderText(QtGui.QApplication.translate("Dialog", "A", None, QtGui.QApplication.UnicodeUTF8))
        self.BEdit.setPlaceholderText(QtGui.QApplication.translate("Dialog", "B", None, QtGui.QApplication.UnicodeUTF8))
        self.CEdit.setPlaceholderText(QtGui.QApplication.translate("Dialog", "C", None, QtGui.QApplication.UnicodeUTF8))
        self.DEdit.setPlaceholderText(QtGui.QApplication.translate("Dialog", "D", None, QtGui.QApplication.UnicodeUTF8))
        self.EEdit.setPlaceholderText(QtGui.QApplication.translate("Dialog", "E", None, QtGui.QApplication.UnicodeUTF8))
        self.FEdit.setPlaceholderText(QtGui.QApplication.translate("Dialog", "F", None, QtGui.QApplication.UnicodeUTF8))
        self.add_btn.setText(QtGui.QApplication.translate("Dialog", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.del_btn.setText(QtGui.QApplication.translate("Dialog", "Delete", None, QtGui.QApplication.UnicodeUTF8))


    def refresh_table(self):
        self.header_data = ["Lift Type", "Competition Year", "Gender", "A", "B", "C", "D", "E", "F"]
        self.data = []

        for instance in self.session.query(Coefficient).filter(Coefficient.year == self.curr_comp.year):
            self.data.append((instance.liftType, instance.year, instance.gender, instance.a, instance.b, instance.c, instance.d, instance.e, instance.f))


        self.model =  MyTableModel(self.Dialog, self.data, self.header_data)
        self.tableView.setModel(self.model)

    def add_btn_clicked(self):
        print("I was here add btn")
        year = self.curr_comp.year
        ltype = self.lift_type_box.currentText()
        gender = self.gender_box.currentText()
        c_objs = self.session.query(Coefficient).filter(Coefficient.year == year, Coefficient.liftType == ltype, Coefficient.gender == gender).all()
        print(c_objs)
        if len(c_objs) > 0:
            QMessageBox.critical(self.Dialog, "Duplicate Entry", "Coefficients for this lift type and gender already exist for this competition year. No Duplicate entries allowed!", QMessageBox.Ok).show()
            return
        alledits = [self.AEdit, self.BEdit, self.CEdit, self.DEdit, self.EEdit, self.FEdit]
        coeffs = []
        for edit in alledits:
            res = self.floatValidator.validate(edit.text(), 0)
            if res[0] == QValidator.State.Acceptable:
                    coeffs.append(float(edit.text()))
            elif edit.text() == "":
                coeffs.append(0)
            else:
                QMessageBox.critical(self.Dialog, "Invalid Coefficients", "Some of the coefficients entered are invalid. \n Note: Blanks are considered to be 0, and scientific notation is allowed!", QMessageBox.Ok).show()



        coeff_obj = Coefficient(liftType=ltype, year=year, gender=gender, a=coeffs[0], b=coeffs[1], c=coeffs[2], d=coeffs[3], e=coeffs[4], f=coeffs[5])
        try:

            self.session.add(coeff_obj)
            self.session.commit()
        except:
            self.session.rollback()
            raise
        self.refresh_table()

        self.AEdit.clear()
        self.BEdit.clear()
        self.CEdit.clear()
        self.DEdit.clear()
        self.EEdit.clear()
        self.FEdit.clear()


class ControlNewCompDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(ControlNewCompDialog, self).__init__(parent)
        self.session = session
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

    ################## proper validation to be done message box to be popped up
    def accept(self, *args, **kwargs):
        if len(self.ui.liftypes) != len(self.ui.tableView.model().mylist):
            QMessageBox.critical(self, "Insufficient number of Coefficients", "Too few coefficients are added. \n Every lift type requires coefficients to be added!!", QMessageBox.Ok).show()
        QtGui.QDialog.accept(self)
        print("I was here accept")




    def reject(self, *args, **kwargs):
        if self.ui.savedComp:
            try:
                self.session.delete(self.ui.curr_comp)
                self.session.commit()
            except:
                self.session.rollback()
        QtGui.QDialog.reject(self)
        print("I was here reject")

