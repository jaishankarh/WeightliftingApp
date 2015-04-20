# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manageMembers.ui'
#
# Created: Sun Jul 13 15:02:51 2014
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

#from PySide import QtCore, QtGui
import sys
import threading
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtSql import *
from PySide.QtCore import Signal
from utils.database_api import *
import operator
from members.manageMembers import AddMemberWidget

class Ui_MembersWindow(QMainWindow):
    currentInstance = None


    header = []
    data_list = []
    def __init__(self):
        # if you want a menubar or statusbar, you have to use
        # QMainWindow since QWidget does not have those
        QMainWindow.__init__(self)
        self.setupUi(self);

    def setupDb(self):
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        #self.db.setHostName("localhost")
        self.db.setDatabaseName("./wf.db")
        #self.db.setUserName("root")
        #self.db.setPassword("")
        ok = self.db.open()
        if not ok:
            QMessageBox.warning(self, "Error", "Invalid database!")
            return

    def setupUi(self, MembersWindow):
        MembersWindow.setObjectName("MembersWindow")
        MembersWindow.resize(800, 600)
        MembersWindow.setMinimumSize(QSize(0, 0))
        self.centralWidget = QWidget(MembersWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayoutWidget = QWidget(self.centralWidget)
        self.horizontalLayoutWidget.setGeometry(QRect(20, 0, 761, 101))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.add_butt = QPushButton(self.horizontalLayoutWidget)
        self.add_butt.setMinimumSize(QSize(0, 8))
        self.add_butt.setObjectName("add_butt")
        self.horizontalLayout.addWidget(self.add_butt)
        self.del_butt = QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.del_butt.sizePolicy().hasHeightForWidth())
        self.del_butt.setSizePolicy(sizePolicy)
        self.del_butt.setMinimumSize(QSize(0, 0))
        self.del_butt.setObjectName("del_butt")
        self.horizontalLayout.addWidget(self.del_butt)
        self.search_butt = QPushButton(self.horizontalLayoutWidget)
        self.search_butt.setObjectName("search_butt")
        self.horizontalLayout.addWidget(self.search_butt)
        self.update_butt = QPushButton(self.horizontalLayoutWidget)
        self.search_butt.setObjectName("search_butt")
        self.horizontalLayout.addWidget(self.search_butt)
        self.print_butt = QPushButton(self.horizontalLayoutWidget)
        self.print_butt.setMinimumSize(QSize(0, 8))
        self.print_butt.setObjectName("print_butt")
        self.horizontalLayout.addWidget(self.print_butt)
        refresh()
        table_model = MyTableModel(self, self.data_list, self.header)
        self.tableView = QTableView(self.centralWidget)
        self.tableView.setGeometry(QRect(20, 110, 761, 431))
        self.tableView.setObjectName("tableView")
        self.tableView.setModel(table_model)
        # set font
        font = QFont("Courier New", 14)
        self.tableView.setFont(font)
        # set column width to fit contents (set font first!)
        #self.tableView.resizeColumnsToContents()
        # enable sorting
        self.tableView.setSortingEnabled(True)
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

        self.retranslateUi(MembersWindow)
        QMetaObject.connectSlotsByName(MembersWindow)
        #self.refresh_btn.clicked.connect(self.refresh_btn_clicked)
        #self.add_butt.clicked.connect(self.insert_btn_clicked)
        #self.del_butt.clicked.connect(self.delete_btn_clicked)
        #self.clear_btn.clicked.connect(self.clear_btn_clicked)
        #self.update_btn.clicked.connect(self.update_btn_clicked)
        #self.add_butt.clicked.connect(self.addMember)



    def retranslateUi(self, MembersWindow):
        MembersWindow.setWindowTitle(QApplication.translate("MembersWindow", "MembersWindow", None, QApplication.UnicodeUTF8))
        self.add_butt.setText(QApplication.translate("MembersWindow", "Add", None, QApplication.UnicodeUTF8))
        self.del_butt.setText(QApplication.translate("MembersWindow", "Delete", None, QApplication.UnicodeUTF8))
        self.search_butt.setText(QApplication.translate("MembersWindow", "Search", None, QApplication.UnicodeUTF8))
        self.print_butt.setText(QApplication.translate("MembersWindow", "Print", None, QApplication.UnicodeUTF8))


    @classmethod
    def getCurrentInstance(cls):
        if cls.currentInstance is None:
            cls.currentInstance = Ui_MembersWindow()
            return cls.currentInstance
        return cls.currentInstance



    def addMember(self):
        '''
        some action to indicate which button has been clicked
        '''
        admw = AddMemberWidget.getCurrentInstance()
        admw.show()
        admw.raise_()



def refresh():
    Ui_MembersWindow.header = ['Id', 'First Name', 'Last Name', 'Group']
    Ui_MembersWindow.data_list = dbAll("SELECT * FROM PARTICIPANT")
    if len(Ui_MembersWindow.data_list) == 0 or Ui_MembersWindow.data_list is None:
        Ui_MembersWindow.header = [(" ",),]
        Ui_MembersWindow.data_list = [("No Participants Available",),]



class MyTableModel(QAbstractTableModel):
    def __init__(self, parent, mylist, header, *args):
        QAbstractTableModel.__init__(self, parent, *args)
        self.mylist = mylist
        self.header = header
    def rowCount(self, parent):
        return len(self.mylist)
    def columnCount(self, parent):
        return len(self.mylist[0])
    def data(self, index, role):
        if not index.isValid():
            return None
        elif role != Qt.DisplayRole:
            return None
        return self.mylist[index.row()][index.column()]
    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[col]
        return None
    def sort(self, col, order):
        """sort table by given column number col"""
        self.emit(SIGNAL("layoutAboutToBeChanged()"))
        self.mylist = sorted(self.mylist,
            key=operator.itemgetter(col))
        if order == Qt.DescendingOrder:
            self.mylist.reverse()
        self.emit(SIGNAL("layoutChanged()"))


