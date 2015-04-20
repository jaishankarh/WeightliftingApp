
__author__ = 'jaishankar'

import threading
import sys
import operator

from PySide.QtCore import *
from PySide.QtGui import *
from database_api import *

class AddMemberWidget(QWidget):
    '''This widget displays the form to add a participant to the database'''

    currentInstance = None

    def __init__(self):
        self.title = "Add Member"
        QWidget.__init__(self)

        self.setMinimumSize(400,400)
        self.setWindowTitle(self.title)

        self.layout = QVBoxLayout()

        self.formLayout = QFormLayout()


        self.fnamelbl = QLabel("First Name: ")
        self.fname = QLineEdit()
        self.fname.setPlaceholderText("eg. 'Akash' or 'Prithiv'")
        self.fname.setMinimumWidth(250)
        self.formLayout.addRow(self.fnamelbl,self.fname)
        self.lnamelbl = QLabel("Last Name: ")
        self.lname = QLineEdit()
        self.lname.setPlaceholderText("eg. 'Kandoi' or 'Sassisegarane'")
        self.lname.setMinimumWidth(250)
        self.formLayout.addRow(self.lnamelbl,self.lname)
        #self.salutation_lbl.move(5,5)

        #self.salutation.move(110,5)

        self.grouplbl = QLabel("Group: ")
        #self.salutation_lbl.move(5,5)
        self.groups = ['D', 'C','B1', 'B2', 'A1', 'A2', 'A3']

        self.group = QComboBox()
        self.group.addItems(self.groups)

        self.group.setMinimumWidth(250)
        self.formLayout.addRow(self.grouplbl,self.group)






        self.layout.addLayout(self.formLayout)

        self.layout.addStretch(1)

        self.buttonBox = QHBoxLayout()

        self.buttonBox.addStretch(1)


        self.addButton = QPushButton('&Add Member')

        #self.greetButton.move(250,80)
        self.buttonBox.addWidget(self.addButton)

        self.layout.addLayout(self.buttonBox)

        self.setLayout(self.layout)

        self.addButton.clicked.connect(self.addMember)

        #self.move(5,60)
    @Slot()
    def addMember(self):
        '''Show the greeting using the combobox and text box'''
        query = "INSERT INTO PARTICIPANT(fname, lname, grp) VALUES('%s', '%s', '%s')" %(self.fname.text(),self.lname.text(),self.groups[self.group.currentIndex()])
        #print(query)
        dbQuery(query)
        msgBox = QMessageBox()
        msgBox.setText('Member %s %s has been created successfully as part of group %s' %(self.fname.text(),self.lname.text(),self.groups[self.group.currentIndex()]))
        #msgBox.setText(query)
        msgBox.exec_()
        AddMemberWidget.currentInstance = None
        self.close()




    @classmethod
    def getCurrentInstance(cls):

        if cls.currentInstance is None:
            cls.currentInstance = AddMemberWidget()
            return cls.currentInstance
        return cls.currentInstance


class ListMemberWidget(QWidget):
    currentInstance = None
    def __init__(self, *args):
        QWidget.__init__(self, *args)
        # setGeometry(x_pos, y_pos, width, height)
        self.setGeometry(300, 200, 570, 450)
        self.setWindowTitle("Participants")
        header = ['Id', 'First Name', 'Last Name', 'Group']
        data_list = dbAll("SELECT * FROM PARTICIPANT")
        if len(data_list) == 0 or data_list is None:
            header = [(" ",),]
            data_list = [("No Participants Available",),]
        table_model = MyTableModel(self, data_list, header)
        table_view = QTableView()
        table_view.setModel(table_model)
        # set font
        font = QFont("Courier New", 14)
        table_view.setFont(font)
        # set column width to fit contents (set font first!)
        table_view.resizeColumnsToContents()
        # enable sorting
        table_view.setSortingEnabled(True)
        layout = QVBoxLayout(self)
        layout.addWidget(table_view)
        self.setLayout(layout)

    @classmethod
    def getCurrentInstance(cls):

        if cls.currentInstance is None:
            cls.currentInstance = ListMemberWidget()
            return cls.currentInstance
        return cls.currentInstance

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

