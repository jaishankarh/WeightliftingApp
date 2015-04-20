# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'competition_members.ui'
#
# Created: Tue Dec  9 14:37:27 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from PySide.QtCore import *
from PySide.QtGui import *
from utils.db_classes import *
from sqlalchemy.orm import subqueryload


class Ui_competitionMembers(object):
    def setupUi(self, competitionMembers, comp):
        self.comp_id = comp.id
        competitionMembers.setObjectName("competitionMembers")
        competitionMembers.resize(800, 600)
        self.centralwidget = QtGui.QWidget(competitionMembers)
        self.centralwidget.setObjectName("centralwidget")
        self.back_btn = QtGui.QPushButton(self.centralwidget)
        self.back_btn.setGeometry(QtCore.QRect(20, 20, 80, 23))
        self.back_btn.setObjectName("back_btn")
        self.listView = QtGui.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(130, 110, 271, 411))
        self.listView.setObjectName("listView")
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(420, 110, 271, 261))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        #self.nameEdit = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.nameEdit = QtGui.QComboBox(self.verticalLayoutWidget)
        self.nameEdit.setObjectName("nameEdit")
        self.verticalLayout.addWidget(self.nameEdit)
        self.enroll_btn = QtGui.QPushButton(self.verticalLayoutWidget)
        self.enroll_btn.setObjectName("enroll_btn")
        self.verticalLayout.addWidget(self.enroll_btn)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.del_btn = QtGui.QPushButton(self.verticalLayoutWidget)
        self.del_btn.setObjectName("del_btn")
        self.verticalLayout.addWidget(self.del_btn)
        self.particiating_lbl = QtGui.QLabel(self.centralwidget)
        self.particiating_lbl.setGeometry(QtCore.QRect(140, 80, 171, 16))
        self.particiating_lbl.setObjectName("particiating_lbl")
        self.results_btn = QtGui.QPushButton(self.centralwidget)
        self.results_btn.setGeometry(QtCore.QRect(609, 20, 161, 23))
        self.results_btn.setObjectName("results_btn")
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(150, 0, 391, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comp_name_lbl = QtGui.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comp_name_lbl.setFont(font)
        self.comp_name_lbl.setObjectName("comp_name_lbl")
        self.horizontalLayout.addWidget(self.comp_name_lbl)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.year_lbl = QtGui.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.year_lbl.setFont(font)
        self.year_lbl.setObjectName("year_lbl")
        self.horizontalLayout.addWidget(self.year_lbl)
        self.year_val = QtGui.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.year_val.setFont(font)
        self.year_val.setObjectName("year_val")
        self.horizontalLayout.addWidget(self.year_val)
        competitionMembers.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(competitionMembers)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        competitionMembers.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(competitionMembers)
        self.statusbar.setObjectName("statusbar")
        competitionMembers.setStatusBar(self.statusbar)
        self.session = session
        #print(comp_id)
        self.comp = comp
        self.all_members = self.session.query(Member).all()
        self.all_members_str = []
        for instance in self.all_members:
            self.all_members_str.append(str(instance.fname) + " " + str(instance.lname))
        self.nameEdit.insertItems(0, self.all_members_str)
        self.nameEdit.setEditable(True)
        #self.completer = QCompleter(self.all_members_str, self)
        #self.nameEdit.setCompleter(self.completer)
        self.comp_name_lbl.setText(self.comp.name)
        self.year_val.setText(str(self.comp.year))

        self.data = []
        self.dataStringList = []
        self.model = QStringListModel()

        for instance in self.comp.members:
            self.data.append((instance.id,instance))
            self.dataStringList.append(str(instance.id) + " " + instance.fname + " " + instance.lname)



        self.model.setStringList(self.dataStringList)
        self.listView.setModel(self.model)


        self.enroll_btn.clicked.connect(self.enroll_btn_clicked)
        self.del_btn.clicked.connect(self.del_btn_clicked)
        self.results_btn.clicked.connect(competitionMembers.open_results_win)
        self.back_btn.clicked.connect(competitionMembers.go_back)

        self.retranslateUi(competitionMembers)
        QtCore.QMetaObject.connectSlotsByName(competitionMembers)

    def retranslateUi(self, competitionMembers):
        competitionMembers.setWindowTitle(QtGui.QApplication.translate("competitionMembers", "Competition Participants", None, QtGui.QApplication.UnicodeUTF8))
        self.back_btn.setText(QtGui.QApplication.translate("competitionMembers", "Back", None, QtGui.QApplication.UnicodeUTF8))
        #self.nameEdit.setPlaceholderText(QtGui.QApplication.translate("competitionMembers", "Enter a name", None, QtGui.QApplication.UnicodeUTF8))
        self.enroll_btn.setText(QtGui.QApplication.translate("competitionMembers", "Enroll", None, QtGui.QApplication.UnicodeUTF8))
        self.del_btn.setText(QtGui.QApplication.translate("competitionMembers", "Delete Selected", None, QtGui.QApplication.UnicodeUTF8))
        self.particiating_lbl.setText(QtGui.QApplication.translate("competitionMembers", "Participating Members", None, QtGui.QApplication.UnicodeUTF8))
        self.results_btn.setText(QtGui.QApplication.translate("competitionMembers", "Continue to Enter Results", None, QtGui.QApplication.UnicodeUTF8))
        # self.comp_name_lbl.setText(QtGui.QApplication.translate("competitionMembers", "Current Competition Name", None, QtGui.QApplication.UnicodeUTF8))
        self.year_lbl.setText(QtGui.QApplication.translate("competitionMembers", "Year:", None, QtGui.QApplication.UnicodeUTF8))
        # self.year_val.setText(QtGui.QApplication.translate("competitionMembers", "2009", None, QtGui.QApplication.UnicodeUTF8))

    def refresh_table(self):
        self.data = []
        self.dataStringList = []
        self.model = QStringListModel()
        #self.comp = None
        #self.comp = self.session.query(Competition).filter(Competition.id == self.comp_id).first()
        #self.session.refresh(self.comp, ['members',])
        #self.comp = self.session.query(Competition).options(subqueryload(Competition.members)).filter(Competition.id == self.comp_id).first()
        for instance in self.comp.members:
            self.data.append((instance.id, instance))
            self.dataStringList.append(str(instance.id) + " " + instance.fname + " " + instance.lname)
            print(instance)


        self.model.setStringList(self.dataStringList)
        self.listView.setModel(self.model)

    def enroll_btn_clicked(self):
        index = self.nameEdit.currentIndex()
        sel_mem = self.all_members[index]
        sel_id = sel_mem.id

        if sel_mem in self.comp.members:
            msgBox = QMessageBox()
            msgBox.setText("That member already has already been enrolled!")
            msgBox.exec_()
        else:
            self.comp.members.append(sel_mem)
            try:
                self.session.commit()
                self.nameEdit.clearEditText()
                self.refresh_table()
            except:
                self.session.rollback()
                # rais

    def del_btn_clicked(self):
        index = self.listView.currentIndex().row()
        del_obj = self.data[index][1]
        self.comp.members.remove(del_obj)
        try:
            self.session.commit()
            self.refresh_table()
        except:
            self.session.rollback()



class ControlCompMemWindow(QMainWindow):

    currentInstance = None

    @classmethod
    def getCurrentInstance(cls):
        if cls.currentInstance is None:
            cls.currentInstance = ControlCompMemWindow()
            print("I was here")
            return cls.currentInstance
        return cls.currentInstance

    def __init__(self, parent=None):
        super(ControlCompMemWindow, self).__init__(parent)
        self.ui =  ControlCompMemWindow()
        self.ui.setupUi(self)