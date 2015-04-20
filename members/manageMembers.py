__author__ = 'jaishankar'

from PySide.QtCore import *
from PySide.QtGui import *
from utils.database_api import *
import memberswindow
import sys

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
        query = "INSERT INTO MEMBER(fname, lname, grp) VALUES('%s', '%s', '%s')" %(self.fname.text(),self.lname.text(),self.groups[self.group.currentIndex()])
        #print(query)
        dbQuery(query)
        msgBox = QMessageBox()
        msgBox.setText('Member %s %s has been created successfully as part of group %s' %(self.fname.text(),self.lname.text(),self.groups[self.group.currentIndex()]))
        #msgBox.setText(query)
        msgBox.exec_()
        AddMemberWidget.currentInstance = None
        memberswindow.refresh()
        self.close()




    @classmethod
    def getCurrentInstance(cls):

        if cls.currentInstance is None:
            cls.currentInstance = AddMemberWidget()
            return cls.currentInstance
        return cls.currentInstance

