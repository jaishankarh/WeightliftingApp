# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'memberswindow.ui'
#
# Created: Sun Jul 13 18:47:18 2014
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

#from PySide import QtCore, QtGui
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
#from members.manageMembers import AddMemberWidget




class Ui_MembersWindow(object):

    header = []
    data_list = []
    def __init__(self):
        # if you want a menubar or statusbar, you have to use
        # QMainWindow since QWidget does not have those

        #super(QMainWindow, self).__init__()
        self.setupDb("utils/example.db")
        #self.setupUi(self)



    def setupDb(self,dbname):
        self.db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(dbname)
        ok = self.db.open()
        if not ok:
            QMessageBox.warning(self, "Error", "Invalid database!")
            self.close()
            return False
        return True

    def setupUi(self, MembersWindow):
        MembersWindow.setObjectName("MembersWindow")
        MembersWindow.resize(800, 600)
        #MembersWindow.setMinimumSize(QSize(0, 0))
        self.centralWidget = QWidget(MembersWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.tableView = QTableView(self.centralWidget)
        self.tableView.setGeometry(QRect(20, 140, 761, 401))
        self.tableView.setObjectName("tableView")
        self.horizontalLayoutWidget = QWidget(self.centralWidget)
        self.horizontalLayoutWidget.setGeometry(QRect(10, 0, 759, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_btn = QPushButton(self.horizontalLayoutWidget)
        self.add_btn.setMinimumSize(QSize(0, 8))
        self.add_btn.setObjectName("add_btn")
        self.horizontalLayout.addWidget(self.add_btn)
        self.update_btn = QPushButton(self.horizontalLayoutWidget)
        self.update_btn.setObjectName("update_btn")
        self.horizontalLayout.addWidget(self.update_btn)
        self.del_btn = QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.del_btn.sizePolicy().hasHeightForWidth())
        self.del_btn.setSizePolicy(sizePolicy)
        self.del_btn.setMinimumSize(QSize(0, 0))
        self.del_btn.setObjectName("del_btn")
        self.horizontalLayout.addWidget(self.del_btn)
        self.search_btn = QPushButton(self.horizontalLayoutWidget)
        self.search_btn.setObjectName("search_btn")
        self.horizontalLayout.addWidget(self.search_btn)
        self.refresh_btn = QPushButton(self.horizontalLayoutWidget)
        self.refresh_btn.setMinimumSize(QSize(0, 8))
        self.refresh_btn.setObjectName("refresh_btn")
        self.horizontalLayout.addWidget(self.refresh_btn)
        self.print_btn = QPushButton(self.horizontalLayoutWidget)
        self.print_btn.setMinimumSize(QSize(0, 8))
        self.print_btn.setObjectName("print_btn")
        self.horizontalLayout.addWidget(self.print_btn)
        self.clear_btn = QPushButton(self.horizontalLayoutWidget)
        self.clear_btn.setMinimumSize(QSize(0, 8))
        self.clear_btn.setObjectName("clear_btn")
        self.horizontalLayout.addWidget(self.clear_btn)
        self.horizontalLayoutWidget_7 = QWidget(self.centralWidget)
        self.horizontalLayoutWidget_7.setGeometry(QRect(20, 50, 741, 80))
        self.horizontalLayoutWidget_7.setObjectName("horizontalLayoutWidget_7")
        self.all_fields = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.all_fields.setContentsMargins(0, 0, 0, 0)
        self.all_fields.setObjectName("all_fields")
        self.names = QVBoxLayout()
        self.names.setObjectName("names")
        self.fname_lay = QHBoxLayout()
        self.fname_lay.setObjectName("fname_lay")
        self.fname_lbl = QLabel(self.horizontalLayoutWidget_7)
        self.fname_lbl.setObjectName("fname_lbl")
        self.fname_lay.addWidget(self.fname_lbl)
        self.fname = QLineEdit(self.horizontalLayoutWidget_7)
        self.fname.setObjectName("fname")
        self.fname.setPlaceholderText("eg. 'Akash' or 'Prithiv'")
        self.fname_lay.addWidget(self.fname)
        self.names.addLayout(self.fname_lay)
        self.lname_lay = QHBoxLayout()
        self.lname_lay.setObjectName("lname_lay")
        self.lname_lbl = QLabel(self.horizontalLayoutWidget_7)
        self.lname_lbl.setObjectName("lname_lbl")
        self.lname_lay.addWidget(self.lname_lbl)
        self.lname = QLineEdit(self.horizontalLayoutWidget_7)
        self.lname.setObjectName("lname")
        self.lname.setPlaceholderText("eg. 'Kandoi' or 'Sassisegarane'")
        self.lname_lay.addWidget(self.lname)
        self.names.addLayout(self.lname_lay)
        self.all_fields.addLayout(self.names)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.grp_gen = QVBoxLayout()
        self.grp_gen.setObjectName("grp_gen")
        self.grp_lay = QHBoxLayout()
        self.grp_lay.setObjectName("grp_lay")
        self.grp_lbl = QLabel(self.horizontalLayoutWidget_7)
        self.grp_lbl.setObjectName("grp_lbl")
        self.grp_lay.addWidget(self.grp_lbl)

        self.groups = ['D', 'C','B1', 'B2', 'A1', 'A2', 'A3','Other']
        self.group = QComboBox(self.horizontalLayoutWidget_7)
        self.group.setObjectName("group")
        self.group.addItems(self.groups);
        self.grp_lay.addWidget(self.group)
        self.grp_gen.addLayout(self.grp_lay)
        self.gen = QHBoxLayout()
        self.gen.setObjectName("gen")
        self.gen_lbl = QLabel(self.horizontalLayoutWidget_7)
        self.gen_lbl.setObjectName("gen_lbl")
        self.gen.addWidget(self.gen_lbl)
        self.genders = ['Male', 'Female', 'Other']
        self.gender = QComboBox(self.horizontalLayoutWidget_7)
        self.gender.setObjectName("gender")
        self.gender.addItems(self.genders);
        self.gen.addWidget(self.gender)
        self.grp_gen.addLayout(self.gen)
        self.horizontalLayout_6.addLayout(self.grp_gen)
        self.label_5 = QLabel(self.horizontalLayoutWidget_7)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.dob = QDateEdit(self.horizontalLayoutWidget_7)
        self.dob.setObjectName("dob")
        self.dob.setDisplayFormat("dd-MM-yyyy")
        self.dob.setCalendarPopup(True);
        self.horizontalLayout_6.addWidget(self.dob)
        self.all_fields.addLayout(self.horizontalLayout_6)
        MembersWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QMenuBar(MembersWindow)
        self.menuBar.setGeometry(QRect(0, 0, 800, 20))
        self.menuBar.setObjectName("menuBar")
        MembersWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QToolBar(MembersWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MembersWindow.addToolBar(Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QStatusBar(MembersWindow)
        self.statusBar.setObjectName("statusBar")
        MembersWindow.setStatusBar(self.statusBar)
        self.toolBar = QToolBar(MembersWindow)
        self.toolBar.setObjectName("toolBar")
        MembersWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MembersWindow)
        QMetaObject.connectSlotsByName(MembersWindow)

        self.refresh_btn.clicked.connect(self.refresh_btn_clicked)
        self.add_btn.clicked.connect(self.add_btn_clicked)
        self.del_btn.clicked.connect(self.delete_btn_clicked)
        self.clear_btn.clicked.connect(self.clear_btn_clicked)
        self.update_btn.clicked.connect(self.update_btn_clicked)
        self.tableView.clicked.connect(self.setUpdateParams)

        self.model =  QtSql.QSqlQueryModel()
        self.model.setQuery("SELECT * FROM PARTICIPANT")
        self.model.setHeaderData(1, Qt.Horizontal, "First Name")
        self.model.setHeaderData(2, Qt.Horizontal, "Last Name")
        self.model.setHeaderData(3, Qt.Horizontal, "Group")
        self.model.setHeaderData(4, Qt.Horizontal, "Gender")
        self.model.setHeaderData(5, Qt.Horizontal, "D.O.B")


        self.tableView.setModel(self.model)

        #self.tableView.hideColumn(0) #hide column 'id'
        # self.tableView.horizontalHeader().stretchLastSection()
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows) #select Row
        self.tableView.setSelectionMode(QAbstractItemView.SingleSelection) #disable multiselect
        #self.tableView.resizeColumnsToContents()
        header = self.tableView.horizontalHeader()
        header.setStretchLastSection(True)







    def retranslateUi(self, MembersWindow):
        MembersWindow.setWindowTitle(QApplication.translate("MembersWindow", "Members Window", None, QApplication.UnicodeUTF8))
        self.add_btn.setText(QApplication.translate("MembersWindow", "Add", None, QApplication.UnicodeUTF8))
        self.clear_btn.setText(QApplication.translate("MembersWindow", "Clear Fields", None, QApplication.UnicodeUTF8))
        self.refresh_btn.setText(QApplication.translate("MembersWindow", "Refresh", None, QApplication.UnicodeUTF8))
        self.update_btn.setText(QApplication.translate("MembersWindow", "Update", None, QApplication.UnicodeUTF8))
        self.del_btn.setText(QApplication.translate("MembersWindow", "Delete", None, QApplication.UnicodeUTF8))
        self.search_btn.setText(QApplication.translate("MembersWindow", "Search", None, QApplication.UnicodeUTF8))
        self.print_btn.setText(QApplication.translate("MembersWindow", "Print", None, QApplication.UnicodeUTF8))
        self.fname_lbl.setText(QApplication.translate("MembersWindow", "First Name", None, QApplication.UnicodeUTF8))
        self.lname_lbl.setText(QApplication.translate("MembersWindow", "Last Name", None, QApplication.UnicodeUTF8))
        self.grp_lbl.setText(QApplication.translate("MembersWindow", "Group", None, QApplication.UnicodeUTF8))
        self.gen_lbl.setText(QApplication.translate("MembersWindow", "Gender", None, QApplication.UnicodeUTF8))
        self.label_5.setText(QApplication.translate("MembersWindow", "Date of Birth", None, QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QApplication.translate("MembersWindow", "toolBar", None, QApplication.UnicodeUTF8))




    @Slot(QModelIndex)
    def setUpdateParams(self,index):
        if self.tableView.currentIndex():
            #index = self.tableView.selectedIndexes()[0].row() <<--You must use this for multiselect
            ind = self.tableView.currentIndex().row()
            db_id = self.model.record(ind).value("id")
            fname = self.model.record(ind).value("fname")
            lname = self.model.record(ind).value("lname")
            gen = self.model.record(ind).value("gender")
            group = self.model.record(ind).value("grp")
            dob = self.model.record(ind).value("dob")
            self.fname.clear()
            self.lname.clear()
            self.fname.insert(fname)
            self.lname.insert(lname)
            self.group.setCurrentIndex(self.groups.index(group))
            self.gender.setCurrentIndex(self.genders.index(gen))
            self.dob.setDate(QDate.fromString(dob,"dd-MM-yyyy"))



    def update_btn_clicked(self):
        query = QtSql.QSqlQuery()
        fn = self.fname.text()
        ln = self.lname.text()
        gender = self.gender.currentText()

        group = self.group.currentText()
        date = self.dob.date().toString("dd-MM-yyyy");
        db_id = self.get_current_id()
        sql = "UPDATE PARTICIPANT SET fname = '%s', lname = '%s', grp = '%s', gender = '%s', dob = '%s' \
                                  WHERE id = %d" % (fn, ln, group, gender, date, db_id)
        print(sql)
        try:
            query.exec_(sql)
            self.db.commit()
        except:
            # Rollback in case there is any error
            print("There was an error")
            self.db.rollback()
        self.fname.clear()
        self.lname.clear()
        #gender = self.gender.clear()
        #group = self.group.clear()
        #date = self.dob.()
        self.refresh_table()


    def refresh_btn_clicked(self):
        self.refresh_table()

    def clear_btn_clicked(self):
        self.fname.setText("")
        self.lname.setText("")
        self.dob.setDate(QDate(2000,1,1))
        self.group.setCurrentIndex(0)
        self.gender.setCurrentIndex(0)


    def add_btn_clicked(self):
        query = QtSql.QSqlQuery()
        query.prepare("INSERT INTO PARTICIPANT (fname,\
                    lname,grp,gender,dob) VALUES (:fn, :ln, :grp, :gen, :dob)")
        fn = self.fname.text()
        ln = self.lname.text()
        gender = self.gender.currentText()
        group = self.group.currentText()
        date = self.dob.date().toString("dd-MM-yyyy")
        db_id = self.get_current_id()
        self.fname.clear()
        self.lname.clear()
        query.bindValue(":fn", fn)
        query.bindValue(":ln", ln)
        query.bindValue(":grp", group)
        query.bindValue(":gen", gender)
        query.bindValue(":dob", date)
        try:
            query.exec_()
            self.db.commit()
        except:
            self.db.rollback()
        self.refresh_table()

    def refresh_table(self):
        self.model.setQuery("SELECT * FROM PARTICIPANT")

    def delete_btn_clicked(self):
            query = QtSql.QSqlQuery()
            db_id = self.get_current_id()
            sql = "DELETE FROM PARTICIPANT WHERE id = '%d'" % (db_id)
            try:
                query.exec_(sql)
                self.db.commit()
            except:
                self.db.rollback()
            self.refresh_table()


    def get_current_id(self):
        if self.tableView.currentIndex():
            #index = self.tableView.selectedIndexes()[0].row() <<--You must use this for multiselect
            index = self.tableView.currentIndex().row()
            db_id = self.model.record(index).value("id")
            return db_id


    def addMember(self):
        '''
        some action to indicate which button has been clicked
        '''
        #admw = AddMemberWidget.getCurrentInstance()
        #admw.show()
        #admw.raise_()



def refresh():
    Ui_MembersWindow.header = ['Id', 'First Name', 'Last Name', 'Group']
    Ui_MembersWindow.data_list = dbAll("SELECT * FROM PARTICIPANT")
    if len(Ui_MembersWindow.data_list) == 0 or Ui_MembersWindow.data_list is None:
        Ui_MembersWindow.header = [(" ",),]
        Ui_MembersWindow.data_list = [("No Participants Available",),]



class ControlMembersWindow(QMainWindow):

    currentInstance = None

    @classmethod
    def getCurrentInstance(cls):
        if cls.currentInstance is None:
            currentInstance = ControlMembersWindow()
            print("I was here")
            return currentInstance
        return cls.currentInstance

    def __init__(self, parent=None):
        super(ControlMembersWindow, self).__init__(parent)
        self.ui =  Ui_MembersWindow()
        self.ui.setupUi(self)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    mySW = ControlMembersWindow()
    mySW.show()
    sys.exit(app.exec_())

