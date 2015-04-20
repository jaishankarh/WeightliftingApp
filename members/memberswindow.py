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
from utils.db_classes import*
import xlrd
#from members.manageMembers import AddMemberWidget

from utils.utils import *

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
        self.session = session


    def setupUi(self, MembersWindow):
        self.mem_win = MembersWindow
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
        self.add_from_file_btn = QPushButton(self.horizontalLayoutWidget)
        self.add_from_file_btn.setMinimumSize(QSize(0, 8))
        self.add_from_file_btn.setObjectName("add_from_file_btn")
        self.horizontalLayout.addWidget(self.add_from_file_btn)
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

        self.groups = ['D', 'C', 'B1', 'E', 'F', 'G', 'H',  'B2', 'A1', 'A2', 'A3','Other']
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
        self.add_from_file_btn.clicked.connect(self.add_from_file)

        self.header_data = ["id","First Name", "Last Name", "Group", "Gender", "D.O.B"]
        self.data = []

        for instance in self.session.query(Member):
            self.data.append((instance.id, instance.fname, instance.lname, instance.grp, instance.gender, instance.dob))

        self.model =  MyTableModel(MembersWindow, self.data, self.header_data)
        self.tableView.setModel(self.model)

        #self.tableView.hideColumn(0) #hide column 'id'
        # self.tableView.horizontalHeader().stretchLastSection()
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows) #select Row
        self.tableView.setSelectionMode(QAbstractItemView.MultiSelection) #enable multiselect
        self.tableView.setSortingEnabled(True)
        self.tableView.sortByColumn(0, Qt.AscendingOrder)
        #self.tableView.resizeColumnsToContents()
        header = self.tableView.horizontalHeader()
        header.setStretchLastSection(True)








    def retranslateUi(self, MembersWindow):
        MembersWindow.setWindowTitle(QApplication.translate("MembersWindow", "Members Window", None, QApplication.UnicodeUTF8))
        self.add_btn.setText(QApplication.translate("MembersWindow", "Add", None, QApplication.UnicodeUTF8))
        self.clear_btn.setText(QApplication.translate("MembersWindow", "Clear Fields", None, QApplication.UnicodeUTF8))
        self.refresh_btn.setText(QApplication.translate("MembersWindow", "Refresh", None, QApplication.UnicodeUTF8))
        self.update_btn.setText(QApplication.translate("MembersWindow", "Update", None, QApplication.UnicodeUTF8))
        self.add_from_file_btn.setText(QApplication.translate("MembersWindow", "Add From File", None, QApplication.UnicodeUTF8))
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
            db_id = self.data[ind][0]
            fname = self.data[ind][1]
            lname = self.data[ind][2]
            group = self.data[ind][3]
            gen = self.data[ind][4]
            dob = self.data[ind][5]
            self.fname.clear()
            self.lname.clear()
            self.fname.insert(fname)
            self.lname.insert(lname)
            self.group.setCurrentIndex(self.groups.index(group))
            self.gender.setCurrentIndex(self.genders.index(gen))
            self.dob.setDate(QDate.fromString(dob,"dd-MM-yyyy"))



    def update_btn_clicked(self):
        #query = QtSql.QSqlQuery()
        fn = self.fname.text()
        ln = self.lname.text()
        gender = self.gender.currentText()

        group = self.group.currentText()
        date = self.dob.date().toString("dd-MM-yyyy");
        db_id = self.get_current_id()

        try:
            tmp_mem = self.session.query(Member).filter(Member.id == db_id).first()
            tmp_mem.fname = fn
            tmp_mem.lname = ln
            tmp_mem.gender = gender
            tmp_mem.grp = group
            tmp_mem.dob = date
            self.session.merge(tmp_mem)
            self.session.commit()
        except:
            # Rollback in case there is any error
            print("There was an error")
            self.session.rollback()

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
        fn = self.fname.text()
        ln = self.lname.text()
        gender = self.gender.currentText()
        group = self.group.currentText()
        date = self.dob.date().toString("dd-MM-yyyy")
        temp_mem = Member(fname=fn, lname=ln, gender=gender, grp=group, dob=date)

        self.fname.clear()
        self.lname.clear()

        try:

            self.session.add(temp_mem)
            self.session.commit()
        except:
            self.session.rollback()
        self.refresh_table()

    def refresh_table(self):
        self.data = []
        for instance in self.session.query(Member):
            self.data.append((instance.id, instance.fname, instance.lname, instance.grp, instance.gender, instance.dob))

        self.model =  MyTableModel(self.mem_win, self.data, self.header_data)
        self.tableView.setModel(self.model)

    def delete_btn_clicked(self):
            query = QtSql.QSqlQuery()
            inds = self.tableView.selectionModel().selectedRows()
            print(inds)
            if inds:
                num_records = len(inds)
                ret = QMessageBox.critical(self.mem_win, "Confirm Delete", "Are you sure you want to delete " + str(num_records) + " records? Please note all related lifts performed by this member will also be deleted. This action cannot be undone.", QMessageBox.Ok|QMessageBox.Cancel)
                if ret == QMessageBox.Cancel:
                    return
                elif ret == QMessageBox.Ok:
                    progress = QProgressDialog("Deleting Records...", "Abort Delete", 0, num_records, self.mem_win)
                    counter = 0
                    for ind in inds:
                        progress.setValue(counter)
                        if progress.wasCanceled():
                            QMessageBox.information(self.mem_win, "Operation Cancelled", str(counter) + " records imported!", QMessageBox.Ok)
                            return
                        index = ind.row()
                        db_id = self.data[index][0]
                        print(db_id)
                        tmp_mem = self.session.query(Member).filter(Member.id == db_id).first()
                        print(tmp_mem)
                        try:
                            self.session.delete(tmp_mem)
                            self.session.commit()
                        except:
                            self.session.rollback()

                        counter += 1
                    progress.setValue(num_records)
                    self.refresh_table()
            else:
                QMessageBox.critical(self.mem_win, "No selection", "Please make a select at least one row to delete!", QMessageBox.Ok)



    def get_current_id(self):
        if self.tableView.currentIndex():
            #index = self.tableView.selectedIndexes()[0].row() <<--You must use this for multiselect
            index = self.tableView.currentIndex().row()
            db_id = self.data[index][0]
            return db_id


    def add_from_file(self):
        '''
        some action to indicate which button has been clicked
        '''
        filetoopen = QFileDialog.getOpenFileName(self.mem_win, 'Open file', os.getcwd())
        workbook = xlrd.open_workbook(filetoopen[0])
        worksheet = workbook.sheet_by_name('Sheet1')
        num_rows = worksheet.nrows - 1
        num_cells = worksheet.ncols -1
        curr_row = -1
        counter = 0
        progress = QProgressDialog("Importing Records...", "Abort Import", 0, num_rows, self.mem_win)
        while curr_row < num_rows:
            progress.setValue(curr_row)
            if progress.wasCanceled():
                QMessageBox.information(self.mem_win, "Operation Cancelled", str(counter) + " records imported!", QMessageBox.Ok)
                return
            curr_row += 1
            row = worksheet.row(curr_row)
            curr_cell = -1
            value_list = []
            while curr_cell < num_cells:
                curr_cell += 1
                # Cell Types: 0=Empty, 1=Text, 2=Number, 3=Date, 4=Boolean, 5=Error, 6=Blank
                cell_type = worksheet.cell_type(curr_row, curr_cell)
                cell_value = worksheet.cell_value(curr_row, curr_cell)
                print('	', cell_type, ':', cell_value)
                val = ""
                if curr_cell == 0:
                    val = cell_value.split(" ")
                    value_list.append(val[0])
                    if len(val) >1:
                        value_list.append(" ".join(val[1:]))
                    else:
                        value_list.append("")
                else:
                    value_list.append(cell_value)

            temp_mem = Member(fname=value_list[0], lname=value_list[1], gender=value_list[2], grp=value_list[3], dob="")

            try:
                self.session.add(temp_mem)
                self.session.commit()
                counter += 1;
            except:
                self.session.rollback()

            print(row)
        progress.setValue(num_rows)
        QMessageBox.information(self.mem_win, "Success", str(counter) + " records imported!", QMessageBox.Ok)
        self.refresh_table()
        #admw = AddMemberWidget.getCurrentInstance()
        #admw.show()
        #admw.raise_()









class ControlMembersWindow(QMainWindow):

    currentInstance = None

    @classmethod
    def getCurrentInstance(cls):
        if cls.currentInstance is None:
            cls.currentInstance = ControlMembersWindow()
            print("I was here")
            return cls.currentInstance
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

