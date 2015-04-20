# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'print_competition.ui'
#
# Created: Mon Dec 15 12:09:26 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from PySide.QtGui import *
from PySide.QtCore import *
from utils.db_classes import *
from utils.utils import *
import os
import xlsxwriter
from datetime import *
import math

class Ui_print_win(object):
    def setupUi(self, print_win):
        self.session = session
        self.print_win = print_win
        print_win.setObjectName("print_win")
        print_win.resize(800, 600)
        self.createMemberLayout()






    def changeLayout(self):
        ind = self.table_select.currentIndex()
        current_table = self.tables[ind]
        if current_table == "Member":
            self.createMemberLayout()
        elif current_table == "Lift":
            self.createLiftLayout()
        elif current_table == "Competition":
            self.createCompetitionLayout()


    def createMemberLayout(self):
        self.centralwidget = QtGui.QWidget(self.print_win)
        self.centralwidget.setObjectName("centralwidget")
        self.tables = ['Member', 'Lift', 'Competition']
        self.table_select = QtGui.QComboBox(self.centralwidget)
        self.table_select.setGeometry(QtCore.QRect(160, 10, 151, 23))
        self.table_select.addItems(self.tables)
        self.table_select.setObjectName("table_select")
        self.table_select.setCurrentIndex(0)
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
        self.fname_cb = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.fname_cb.setObjectName("fname_cb")
        self.fname_cb.setChecked(True)
        self.horizontalLayout.addWidget(self.fname_cb)
        self.lname_cb = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.lname_cb.setObjectName("lname_cb")
        self.lname_cb.setChecked(True)
        self.horizontalLayout.addWidget(self.lname_cb)
        self.gender_cb = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.gender_cb.setObjectName("gender_cb")
        self.gender_cb.setChecked(True)
        self.horizontalLayout.addWidget(self.gender_cb)

        self.group_cb = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.group_cb.setObjectName("group_cb")
        self.group_cb.setChecked(True)
        self.horizontalLayout.addWidget(self.group_cb)
        self.dob_cb = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.dob_cb.setObjectName("dob_cb")
        self.dob_cb.setChecked(True)
        self.horizontalLayout.addWidget(self.dob_cb)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.comp_yearEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.comp_yearEdit.setObjectName("comp_yearEdit")
        self.horizontalLayout_2.addWidget(self.comp_yearEdit)
        self.groupEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.groupEdit.setObjectName("groupEdit")
        self.horizontalLayout_2.addWidget(self.groupEdit)
        self.fromYearEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.fromYearEdit.setObjectName("fromYearEdit")
        self.horizontalLayout_2.addWidget(self.fromYearEdit)
        self.toYearEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.toYearEdit.setObjectName("toYearEdit")
        self.horizontalLayout_2.addWidget(self.toYearEdit)
        self.groups = ['All', 'D', 'C','B1', 'B2', 'A1', 'A2', 'A3','Other']
        self.group_box = QtGui.QComboBox(self.verticalLayoutWidget)
        self.group_box.setObjectName("comboBox_2")
        self.group_box.addItems(self.groups);
        self.horizontalLayout_2.addWidget(self.group_box)
        self.filter_btn = QtGui.QPushButton(self.verticalLayoutWidget)
        self.filter_btn.setObjectName("filter_btn")
        self.horizontalLayout_2.addWidget(self.filter_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.sort_key_box = QtGui.QComboBox(self.verticalLayoutWidget)
        self.sort_key_box.setObjectName("sort_key_box")
        self.horizontalLayout_6.addWidget(self.sort_key_box)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.sort_order_box = QtGui.QComboBox(self.verticalLayoutWidget)
        self.sort_order_box.setObjectName("sort_order_box")
        self.horizontalLayout_4.addWidget(self.sort_order_box)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.tableView = QtGui.QTableView(self.verticalLayoutWidget)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_2.addWidget(self.tableView)


        self.cbs = [self.fname_cb, self.lname_cb, self.group_cb, self.gender_cb, self.dob_cb]

        self.header_data = ["First Name", "Last Name", "Group", "Gender", "D.O.B"]
        self.data = []

        counter = 0
        for instance in self.session.query(Member):
            counter += 1
            self.data.append((instance.fname, instance.lname, instance.grp, instance.gender, instance.dob))

        self.model =  MyTableModel(self.print_win, self.data, self.header_data)
        self.tableView.setModel(self.model)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows) #select Row
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection) #disable multiselect
        #self.tableView.hideColumn(2)
        #self.tableView.resizeColumnsToContents()
        header = self.tableView.horizontalHeader()
        header.setStretchLastSection(True)
        self.tableView.setSortingEnabled(True)


        self.shownColumns = range(len(self.data[0]))
        print(self.shownColumns)
        for cb in self.cbs:
            cb.clicked.connect(self.hideColumns)

        self.print_win.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(self.print_win)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        self.print_win.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(self.print_win)
        self.statusbar.setObjectName("statusbar")
        self.print_win.setStatusBar(self.statusbar)

        self.table_select.currentIndexChanged.connect(self.changeLayout)
        self.retranslateUi(self.print_win)
        QtCore.QMetaObject.connectSlotsByName(self.print_win)

        self.filter_btn.clicked.connect(self.filterMemberData)
        self.print_btn.clicked.connect(self.save)



        self.fname_cb.setText(QtGui.QApplication.translate("print_win", "First Name", None, QtGui.QApplication.UnicodeUTF8))
        self.lname_cb.setText(QtGui.QApplication.translate("print_win", "Last Name", None, QtGui.QApplication.UnicodeUTF8))
        self.gender_cb.setText(QtGui.QApplication.translate("print_win", "Gender", None, QtGui.QApplication.UnicodeUTF8))
        self.group_cb.setText(QtGui.QApplication.translate("print_win", "Group", None, QtGui.QApplication.UnicodeUTF8))
        self.dob_cb.setText(QtGui.QApplication.translate("print_win", "D.O.B", None, QtGui.QApplication.UnicodeUTF8))
        self.comp_yearEdit.setPlaceholderText(QtGui.QApplication.translate("print_win", "Competition Year", None, QtGui.QApplication.UnicodeUTF8))
        self.groupEdit.setPlaceholderText(QtGui.QApplication.translate("print_win", "Group", None, QtGui.QApplication.UnicodeUTF8))
        self.fromYearEdit.setPlaceholderText(QtGui.QApplication.translate("print_win", "From Year", None, QtGui.QApplication.UnicodeUTF8))
        self.toYearEdit.setPlaceholderText(QtGui.QApplication.translate("print_win", "To Year", None, QtGui.QApplication.UnicodeUTF8))
        self.filter_btn.setText(QtGui.QApplication.translate("print_win", "Filter", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("print_win", "Sort Key", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("print_win", "Sort Order", None, QtGui.QApplication.UnicodeUTF8))

    def createLiftLayout(self):
        self.centralwidget = QtGui.QWidget(self.print_win)
        self.centralwidget.setObjectName("centralwidget")
        self.tables = ['Member', 'Lift', 'Competition']
        self.table_select = QtGui.QComboBox(self.centralwidget)
        self.table_select.setGeometry(QtCore.QRect(160, 10, 151, 23))
        self.table_select.addItems(self.tables)
        self.table_select.setObjectName("table_select")
        self.table_select.setCurrentIndex(1)
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
        self.name_cb = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.name_cb.setObjectName("name_cb")
        self.name_cb.setChecked(True)
        self.horizontalLayout.addWidget(self.name_cb)
        self.gender_cb = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.gender_cb.setObjectName("gender_cb")
        self.horizontalLayout.addWidget(self.gender_cb)
        self.group_cb = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.group_cb.setObjectName("group_cb")
        self.group_cb.setChecked(True)
        self.horizontalLayout.addWidget(self.group_cb)
        self.age_cb = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.age_cb.setObjectName("age_cb")
        self.horizontalLayout.addWidget(self.age_cb)
        self.bdy_weight_cb = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.bdy_weight_cb.setObjectName("bdy_weight_cb")
        self.bdy_weight_cb.setChecked(True)
        self.horizontalLayout.addWidget(self.bdy_weight_cb)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lift_type_cb = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.lift_type_cb.setObjectName("lift_type_cb")
        self.horizontalLayout_3.addWidget(self.lift_type_cb)
        self.lift_name_cb = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.lift_name_cb.setObjectName("lift_name_cb")
        self.lift_name_cb.setChecked(True)
        self.horizontalLayout_3.addWidget(self.lift_name_cb)
        self.lift_wt_cb = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.lift_wt_cb.setChecked(True)
        self.lift_wt_cb.setObjectName("lift_wt_cb")
        self.horizontalLayout_3.addWidget(self.lift_wt_cb)
        self.date_cb = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.date_cb.setObjectName("date_cb")
        self.horizontalLayout_3.addWidget(self.date_cb)
        self.year_cb = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.year_cb.setObjectName("year_cb")
        self.year_cb.setChecked(True)
        self.horizontalLayout_3.addWidget(self.year_cb)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.comp_yearEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.comp_yearEdit.setObjectName("comp_yearEdit")
        self.horizontalLayout_2.addWidget(self.comp_yearEdit)
        self.lift_name_box = QtGui.QComboBox(self.verticalLayoutWidget)
        self.lift_name_box.setObjectName("lift_name_box")
        self.horizontalLayout_2.addWidget(self.lift_name_box)

        self.liftnames = []
        self.liftnames.append('All')
        for l in self.session.query(Lift_Type).all():
            self.liftnames.append(l.liftName)

        self.lift_name_box.insertItems(0,self.liftnames)

        self.fromYearEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.fromYearEdit.setObjectName("fromYearEdit")
        self.horizontalLayout_2.addWidget(self.fromYearEdit)
        self.toYearEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.toYearEdit.setObjectName("toYearEdit")
        self.horizontalLayout_2.addWidget(self.toYearEdit)
        self.filter_btn = QtGui.QPushButton(self.verticalLayoutWidget)
        self.filter_btn.setObjectName("filter_btn")
        self.horizontalLayout_2.addWidget(self.filter_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.tableView = QtGui.QTableView(self.verticalLayoutWidget)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_2.addWidget(self.tableView)

        self.cbs = [self.name_cb, self.gender_cb, self.group_cb, self.age_cb, self.bdy_weight_cb, self.lift_type_cb, self.lift_name_cb, self.lift_wt_cb, self.date_cb, self.year_cb]

        self.header_data = ["Name", "Gender", "Group", "Age", "Body Weight", "Lift Type", "Lift Name", "Lift Weight", "Date", "Year"]
        self.data = []


        for instance in self.session.query(Lift).join(Lift.competition).join(Lift.member):
            age = ""
            print("Dob is " + instance.member.dob)
            if instance.member.dob != "" and instance.member.dob is not None and instance.date != "" and instance.date is not None:
                d1 = datetime.strptime(instance.member.dob, "%d-%m-%Y")
                d2 = datetime.strptime(instance.date, "%d-%m-%Y")
                age = int((d2 - d1).days / 365)
            print(age)
            lname = ""
            if instance.member.lname != "":
                lname = instance.member.lname[0]
            self.data.append((instance.member.fname + " " + lname, instance.member.gender, instance.member.grp, age, instance.body_weight, instance.lift_type.liftType, instance.lift_type.liftName, instance.lift_weight, instance.date, instance.competition.year))
            # print(instance)

        self.model =  MyTableModel(self.print_win, self.data, self.header_data)
        self.tableView.setModel(self.model)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows) #select Row
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection) #disable multiselect
        #self.tableView.hideColumn(2)
        #self.tableView.resizeColumnsToContents()
        header = self.tableView.horizontalHeader()
        header.setStretchLastSection(True)
        self.tableView.setSortingEnabled(True)

        self.shownColumns = []
        counter = 0
        for cb in self.cbs:
            if cb.isChecked():
                self.shownColumns.append(counter)
            else:
                self.tableView.hideColumn(counter)
            counter += 1
        print(self.shownColumns)
        for cb in self.cbs:
            cb.clicked.connect(self.hideColumns)


        self.print_win.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(self.print_win)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        self.print_win.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(self.print_win)
        self.statusbar.setObjectName("statusbar")
        self.print_win.setStatusBar(self.statusbar)

        self.table_select.currentIndexChanged.connect(self.changeLayout)
        self.filter_btn.clicked.connect(self.filterLiftData)
        self.print_btn.clicked.connect(self.save)
        self.retranslateUi(self.print_win)
        QtCore.QMetaObject.connectSlotsByName(self.print_win)

        self.name_cb.setText(QtGui.QApplication.translate("print_win", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.gender_cb.setText(QtGui.QApplication.translate("print_win", "Gender", None, QtGui.QApplication.UnicodeUTF8))
        self.group_cb.setText(QtGui.QApplication.translate("print_win", "Group", None, QtGui.QApplication.UnicodeUTF8))
        self.age_cb.setText(QtGui.QApplication.translate("print_win", "Age", None, QtGui.QApplication.UnicodeUTF8))
        self.bdy_weight_cb.setText(QtGui.QApplication.translate("print_win", "Body Weight", None, QtGui.QApplication.UnicodeUTF8))
        self.lift_type_cb.setText(QtGui.QApplication.translate("print_win", "Lift Type", None, QtGui.QApplication.UnicodeUTF8))
        self.lift_name_cb.setText(QtGui.QApplication.translate("print_win", "Lift Name", None, QtGui.QApplication.UnicodeUTF8))
        self.lift_wt_cb.setText(QtGui.QApplication.translate("print_win", "Lift Weight", None, QtGui.QApplication.UnicodeUTF8))
        self.date_cb.setText(QtGui.QApplication.translate("print_win", "Date", None, QtGui.QApplication.UnicodeUTF8))
        self.year_cb.setText(QtGui.QApplication.translate("print_win", "Year", None, QtGui.QApplication.UnicodeUTF8))
        self.comp_yearEdit.setPlaceholderText(QtGui.QApplication.translate("print_win", "Competition Year", None, QtGui.QApplication.UnicodeUTF8))
        self.fromYearEdit.setPlaceholderText(QtGui.QApplication.translate("print_win", "From Year", None, QtGui.QApplication.UnicodeUTF8))
        self.toYearEdit.setPlaceholderText(QtGui.QApplication.translate("print_win", "To Year", None, QtGui.QApplication.UnicodeUTF8))
        self.filter_btn.setText(QtGui.QApplication.translate("print_win", "Filter", None, QtGui.QApplication.UnicodeUTF8))

    def createCompetitionLayout(self):
        self.centralwidget = QtGui.QWidget(self.print_win)
        self.centralwidget.setObjectName("centralwidget")
        self.tables = ['Member', 'Lift', 'Competition']
        self.table_select = QtGui.QComboBox(self.centralwidget)
        self.table_select.setGeometry(QtCore.QRect(160, 10, 151, 23))
        self.table_select.addItems(self.tables)
        self.table_select.setObjectName("table_select")
        self.table_select.setCurrentIndex(2)
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
        self.lifts_select = []
        self.lifts_select.append("Overall")
        self.ltypes = self.session.query(Lift_Type.liftType).distinct().all()
        # print(ls)
        for l in self.ltypes:
            self.lifts_select.append(l[0])
        ls = self.session.query(Lift_Type.liftName).all()


        for l in ls:
            self.lifts_select.append(l[0])
        # print(self.lifts_select)


        self.choose_table_box = QtGui.QComboBox(self.verticalLayoutWidget)
        self.choose_table_box.setObjectName("choose_table_box")
        self.choose_table_box.insertItems(0, self.lifts_select)
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
        self.help_lbl = QtGui.QLabel(self.verticalLayoutWidget)
        self.help_lbl.setObjectName("help_lbl")
        self.help_lbl.setText("Please choose a lift and year and click on View. Enter either a single year or enter from and to, don't fill in all three fields.")
        self.verticalLayout_2.addWidget(self.help_lbl)
        self.tableView = QtGui.QTableView(self.verticalLayoutWidget)
        self.tableView.setObjectName("tableView")
        # msg = ("Please choose a lift and year and click on View. Enter either a single year or enter from and to, don't fill in all three fields.",)
        # self.model =  MyTableModel(self.print_win, [msg,], [("",),])
        # self.tableView.setModel(self.model)
        # header = self.tableView.horizontalHeader()
        # header.setStretchLastSection(True)


        self.verticalLayout_2.addWidget(self.tableView)
        self.print_win.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(self.print_win)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        self.print_win.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(self.print_win)
        self.statusbar.setObjectName("statusbar")
        self.print_win.setStatusBar(self.statusbar)


        self.table_select.currentIndexChanged.connect(self.changeLayout)
        self.filter_btn.clicked.connect(self.filterCompData)
        self.print_btn.clicked.connect(self.save)
        self.retranslateUi(self.print_win)
        QtCore.QMetaObject.connectSlotsByName(self.print_win)

        self.choose_lbl.setText(QtGui.QApplication.translate("print_win", "Choose :", None, QtGui.QApplication.UnicodeUTF8))
        self.comp_yearEdit.setPlaceholderText(QtGui.QApplication.translate("print_win", "Competition Year", None, QtGui.QApplication.UnicodeUTF8))
        self.fromYearEdit.setPlaceholderText(QtGui.QApplication.translate("print_win", "From Year", None, QtGui.QApplication.UnicodeUTF8))
        self.toYearEdit.setPlaceholderText(QtGui.QApplication.translate("print_win", "To Year", None, QtGui.QApplication.UnicodeUTF8))
        self.filter_btn.setText(QtGui.QApplication.translate("print_win", "View", None, QtGui.QApplication.UnicodeUTF8))


    def filterCompData(self):
        ind = self.choose_table_box.currentIndex()
        lift_name = self.lifts_select[ind]
        if lift_name == "Overall":
            self.getOverallResults(None)
        else:
            onofthese = False
            for l in self.ltypes:
                if lift_name == l[0]:
                    onofthese = True
                    self.getOverallResults(lift_name)
            if not onofthese:
                self.getfilteredCompResults(lift_name)

    def getfilteredCompResults(self, liftnm):
        cy = self.comp_yearEdit.text()
        comp_year = None
        if cy is not None and cy != "" and cy.isdigit():
            comp_year = int(cy)
        else:
            QMessageBox.critical(self.print_win, "Invalid Year", "Please input a valid year and try again!", QMessageBox.Ok).show()
            return

        self.header_data = ["Name",]
        self.header_data.append("Body Weight")
        self.header_data.append("Coefficient")
        self.header_data.append(liftnm + " Weight")
        self.header_data.append(liftnm + " Points")

        print(self.header_data)

        self.shownColumns = range(len(self.header_data))

        self.data = []

        comp = self.session.query(Competition).filter(Competition.year == comp_year).first()
        if comp is None:
            QMessageBox.critical(self.print_win, "No Results", "No Results found for this combination, please try again!", QMessageBox.Ok)
        for member in comp.members:
            obj = [member.fname + " " + member.lname[0], ]
            print(member.fname)
            gtw = [] #grand tottal weight
            gtp = [] #grand total points
            lift_query = self.session.query(Lift).join(Lift.competition).join(Lift.member).join(Lift.lift_type).filter(Competition.year == comp_year).filter(Member.id == member.id).filter(Lift_Type.liftName == liftnm)
            lift = lift_query.first()

            cf = None
            if lift is not None:
                    coeff = self.session.query(Coefficient).filter(Coefficient.liftType == lift.lift_type.liftType).filter(Coefficient.year == comp_year).filter(Coefficient.gender == member.gender).first()
                    obj.append(lift.body_weight)
                    if lift.lift_type.liftType == "Power Lift":
                                a = coeff.a
                                b = coeff.b
                                c = coeff.c
                                d = coeff.d
                                e = coeff.e
                                f = coeff.f
                                w = lift.body_weight
                                cf = 500/(a + b*w + c*w**2 + d*w**3 + e*w**4 + f*w**5)
                                cf = round(cf, 5)
                    elif lift.lift_type.liftType == "Olympic Lift":
                                a = coeff.a
                                b = coeff.b
                                w = lift.body_weight
                                cf = 10**(a*(math.log10(w/b))**2)
                                cf = round(cf, 5)
                    obj.append(cf)
                    points = cf * lift.lift_weight
                    points = round(points, 1)
                    rltw = round(lift.lift_weight, 1)
                    obj.append(rltw)
                    obj.append(points)

            else:
                obj.append("NA")
                obj.append("NA")
                obj.append("NA")
                obj.append("NA")

            self.data.append(obj)



            # print(instance)

        self.model =  MyTableModel(self.print_win, self.data, self.header_data)
        self.tableView.setModel(self.model)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows) #select Row
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection) #disable multiselect
        #self.tableView.hideColumn(2)
        self.tableView.resizeColumnsToContents()
        header = self.tableView.horizontalHeader()
        header.setStretchLastSection(True)
        self.tableView.setSortingEnabled(True)




    def getOverallResults(self,overall):
        cy = self.comp_yearEdit.text()
        comp_year = None
        if cy is not None and cy != "" and cy.isdigit():
            comp_year = int(cy)
        else:
            QMessageBox.critical(self.print_win, "Invalid Year", "Please input a valid year and try again!", QMessageBox.Ok).show()
            return

        self.header_data = ["Name",]
        if overall is None:
            ls = self.session.query(Lift_Type.liftType).distinct().all()
        else:
            ls = self.session.query(Lift_Type.liftType).distinct().filter(Lift_Type.liftType == overall).all()

        for l in ls:
            self.header_data.append("Body Weight")
            self.header_data.append("Coefficient")
            lnames = self.session.query(Lift_Type).filter(Lift_Type.liftType == l[0]).all()
            for ln in lnames:
                self.header_data.append(ln.liftName)
                self.header_data.append(ln.liftName + " Points")
            self.header_data.append(l[0] + " Weight")
            self.header_data.append(l[0] + " Points")

        if overall is None:
            self.header_data.append("Grand Weight Total")
            self.header_data.append("Grand Points Total")

        print(self.header_data)

        self.shownColumns = range(len(self.header_data))

        self.data = []

        comp = self.session.query(Competition).filter(Competition.year == comp_year).first()
        if comp is None:
            QMessageBox.critical(self.print_win, "No Results", "No Results found for this combination, please try again!", QMessageBox.Ok)
            return
        for member in comp.members:
            lname = ""
            if member.lname != "":
                lname = member.lname[0]
            obj = [member.fname + " " + lname, ]
            print(member.fname)
            gtw = [] #grand tottal weight
            gtp = [] #grand total points
            for l in ls: #by lift type
                lnames = self.session.query(Lift_Type).filter(Lift_Type.liftType == l[0]).all()
                lift_query = self.session.query(Lift).join(Lift.competition).join(Lift.member).join(Lift.lift_type).filter(Competition.year == comp_year).filter(Member.id == member.id)
                lift = lift_query.all()
                gen = member.gender
                if member.gender == "":
                    gen = "Male"
                coeff = self.session.query(Coefficient).filter(Coefficient.liftType == l[0]).filter(Coefficient.year == comp_year).filter(Coefficient.gender == gen).first()
                if coeff is None:
                    QMessageBox.critical(self.print_win, "No Coefficients available", "No coefficients were found this competition %s, please update the competition entry and try again!" %(comp_year), QMessageBox.Ok)

                b_w = lift_query.filter(Lift_Type.liftType == l[0]).first()
                cf = None
                if b_w is not None:
                    obj.append(b_w.body_weight)
                    if l[0] == "Power Lift":
                                a = coeff.a
                                b = coeff.b
                                c = coeff.c
                                d = coeff.d
                                e = coeff.e
                                f = coeff.f
                                w = b_w.body_weight
                                cf = 500/(a + b*w + c*w**2 + d*w**3 + e*w**4 + f*w**5)
                                cf = round(cf, 5)
                    elif l[0] == "Olympic Lift":
                                a = coeff.a
                                b = coeff.b
                                w = b_w.body_weight
                                cf = 10**(a*(math.log10(w/b))**2)
                                cf = round(cf, 5)
                    obj.append(cf)


                tw = [] #tottal weight
                tp = [] #tottal points
                bdy_weight_inserted = False
                for ln in lnames: #by lift name
                    print(ln.liftName)
                    found = False
                    for lt in lift:
                        print(lt)
                        if lt.lift_type.liftName == ln.liftName:
                            points = cf * lt.lift_weight
                            points = round(points, 1)
                            print(coeff)
                            found = True


                            rltw = round(lt.lift_weight, 1)
                            obj.append(rltw)

                            tw.append(rltw)
                            tp.append(points)
                            obj.append(points)


                    if found == False:
                        obj.append("NA")
                        obj.append("NA")



                print("************")
                print(tw)
                print("************")
                print(tp)
                obj.append(round(sum(tw),1))
                obj.append(round(sum(tp),1))
                gtw.append(round(sum(tw),1))
                gtp.append(round(sum(tp),1))
            if overall is None:
                obj.append(round(sum(gtw),1))
                obj.append(round(sum(gtp),1))
            self.data.append(obj)
            print(self.data)

            # print(instance)

        self.model =  MyTableModel(self.print_win, self.data, self.header_data)
        self.tableView.setModel(self.model)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows) #select Row
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection) #disable multiselect
        #self.tableView.hideColumn(2)
        self.tableView.resizeColumnsToContents()
        header = self.tableView.horizontalHeader()
        header.setStretchLastSection(True)
        self.tableView.setSortingEnabled(True)
        self.tableView.sortByColumn(0, Qt.AscendingOrder)


    def retranslateUi(self, print_win):
        print_win.setWindowTitle(QtGui.QApplication.translate("print_win", "Print Options Window", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("print_win", "Choose Table", None, QtGui.QApplication.UnicodeUTF8))
        self.print_btn.setText(QtGui.QApplication.translate("print_win", "Print", None, QtGui.QApplication.UnicodeUTF8))


    def hideColumns(self):

        self.tableView.resizeColumnsToContents()
        for counter in range(len(self.cbs)):
            if not self.cbs[counter].isChecked():
                self.tableView.hideColumn(counter)
                print(counter)
                if counter in self.shownColumns:
                    self.shownColumns.remove(counter)
            else:
                self.tableView.showColumn(counter)
                if counter not in self.shownColumns:
                    self.shownColumns.append(counter)
            counter += 1


    def filterMemberData(self):
        cy = self.comp_yearEdit.text()
        comp_year = None
        if cy is not None and cy != "" and cy.isdigit():
            comp_year = int(cy)
        fyear = self.fromYearEdit.text()
        tyear = self.toYearEdit.text()

        fdata = None
        if comp_year is not None and comp_year != "":
            fdata = self.session.query(Competition).filter(Competition.year == comp_year).first().members

        self.data = []


        for instance in fdata:
            self.data.append((instance.fname, instance.lname, instance.grp, instance.gender, instance.dob))

        self.model =  MyTableModel(self.print_win, self.data, self.header_data)
        self.tableView.setModel(self.model)

        self.header_data = ["First Name", "Last Name", "Group", "Gender", "D.O.B"]

        for i in range(len(self.data[0])):
            if i not in self.shownColumns:
                self.tableView.hideColumn(i)

    def filterLiftData(self):
        cy = self.comp_yearEdit.text()
        comp_year = None
        if cy is not None and cy != "" and cy.isdigit():
            comp_year = int(cy)
        fyear = self.fromYearEdit.text()
        tyear = self.toYearEdit.text()

        if comp_year is not None and (fyear != "" or tyear != ""):
            QMessageBox.critical(self.print_win, "Cannot use multiple filters", "Incompatible filters used,  please use a different combination and try again!", QMessageBox.Ok).show()
            return
        if fyear != "":
            if (not fyear.isdigit()) or tyear == "" or (not tyear.isdigit()):
                QMessageBox.critical(self.print_win, "Invalid use of filter", "Please input valid from or to years and filter again!", QMessageBox.Ok).show()
                return
        else:
            if tyear != "":
                QMessageBox.critical(self.print_win, "Invalid use of filter", "Please input a valid 'From year' and filter again!", QMessageBox.Ok).show()
                return

        l_ind = self.lift_name_box.currentIndex()

        fdata = None
        query_var = None
        if comp_year is not None and comp_year != "":
            query_var = self.session.query(Lift).join(Lift.competition).join(Lift.member).filter(Competition.year == comp_year)
            if query_var.first() is None:
                QMessageBox.information(self.print_win, "No records found", "No records for this competition were found in the database. \n Please change the filter and try again!", QMessageBox.Ok).show()
                return
            #fdata = query_var.first().lifts

        if fyear is not None and fyear != "":
            fyear = int(fyear)
            tyear = int(tyear)
            query_var = self.session.query(Lift).join(Lift.competition).join(Lift.member).filter(Competition.year >= fyear, Competition.year <= tyear)
            if query_var.all() is None or len(query_var.all()) == 0:
                QMessageBox.information(self.print_win, "No records found", "No records for this filter were found in the database. \n Please change the filter and try again!", QMessageBox.Ok).show()
                return
            #fdata = query_var.all()

        if l_ind > 0:
            liftname = self.liftnames[l_ind]
            print(liftname)
            if query_var is not None:
                print(query_var.all())
                print("**************")
                fdata = query_var.filter(Lift_Type.liftName == liftname).all()
                print("**************")
                print(fdata)

            else:
                fdata = self.session.query(Lift).join(Lift.competition).join(Lift.member).filter(Lift_Type.liftName == liftname).all()

        self.data = []
        if fdata is None or len(fdata) == 0:
                QMessageBox.information(self.print_win, "No records found", "No records for this filter were found in the database. \n Please change the filter and try again!", QMessageBox.Ok).show()
                return

        for instance in fdata:
            #print(instance)
            if instance.member.dob != "":
                d1 = datetime.strptime(instance.member.dob, "%d-%m-%Y")
                d2 = datetime.strptime(instance.date, "%d-%m-%Y")
                age = int((d2 - d1).days / 365)
            #print(age)
            lname = ""
            if instance.member.lname != "":
                lname = instance.member.lname[0]
            self.data.append((instance.member.fname + " " + lname, instance.member.gender, instance.member.grp, age, instance.body_weight, instance.lift_type.liftType, instance.lift_type.liftName, instance.lift_weight, instance.date, instance.competition.year))

        self.model =  MyTableModel(self.print_win, self.data, self.header_data)
        self.tableView.setModel(self.model)

        self.header_data = ["Name", "Gender", "Group", "Age", "Body Weight", "Lift Type", "Lift Name", "Lift Weight", "Date", "Year"]

        for i in range(len(self.data[0])):
            if i not in self.shownColumns:
                self.tableView.hideColumn(i)

    def save(self):
        if len(self.model.mylist) == 0 or len(self.shownColumns) < 2:
            QMessageBox.critical(self.print_win, "Too few columns or rows", "Number or columns or rows are too few, please change filter options!", QMessageBox.Ok).show()
            return
        savedir = QFileDialog.getOpenFileName(self.print_win, 'Save to file', os.getcwd())
        print(savedir)
        workbook = xlsxwriter.Workbook(savedir[0])
        worksheet = workbook.add_worksheet()
        pdata = []

        alterdata = self.tableView.model().mylist
        #print(alterdata)
        for row in alterdata:
            tple = []
            for v in self.shownColumns:
                tple.append(row[v])
            pdata.append(tple)

        pheader_data = []
        hd = self.tableView.model().header

        for i in range(len(hd)):
            if i in self.shownColumns:
                pheader_data.append(hd[i])

        rowstart = 0
        colstart = 0
        rowno = rowstart+1
        colno = colstart
        format = workbook.add_format({'bold': True, 'font_color': 'red'})

        for h in pheader_data:
            worksheet.write(rowstart, colno, h, format)
            colno += 1
        colno = colstart
        columnswidth = []
        for item in pheader_data:
            columnswidth.append(len(str(item)) + 1)
        for rowitem in pdata:
            for item in rowitem:
                worksheet.write(rowno, colno, item)
                if len(str(item)) + 1 > columnswidth[colno]:
                    columnswidth[colno] = len(str(item)) + 1
                colno += 1
            colno = colstart
            rowno += 1

        colno = colstart
        for width in columnswidth:
            worksheet.set_column(colno,colno,width)
            colno += 1
        workbook.close()
        QMessageBox.information(self.print_win, "Success!", "Done file generated successfully!", QMessageBox.Ok)

        # QMessageBox.information(self.print_win, "The file location: ", savedir, QMessageBox.Ok).show()



class ControlPrintOptionsWindow(QMainWindow):

    currentInstance = None

    @classmethod
    def getCurrentInstance(cls):
        if cls.currentInstance is None:
            cls.currentInstance = ControlPrintOptionsWindow()
            print("I was here")
            return cls.currentInstance
        return cls.currentInstance

    def __init__(self, parent=None):
        super(ControlPrintOptionsWindow, self).__init__(parent)
        self.ui =  Ui_print_win()
        self.ui.setupUi(self)
