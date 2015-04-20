__author__ = 'jaishankar'

import threading
import sys
from PySide.QtCore import *
from PySide.QtGui import *
from manageMembers import *


class CompetitionCentralWidget(QWidget):
    '''
    a QWidget with a typical box layout
    '''
    def __init__(self):
        QWidget.__init__(self)
        self.addbutton = QPushButton('Add Participant', self)
        # self.addbutton.setMinimumHeight(70)
        # self.addbutton.setMinimumWidth(70)
        self.resbutton = QPushButton('Add Result', self)
        # self.resbutton.setMinimumHeight(70)
        # self.resbutton.setMinimumWidth(70)
        # self.members = dbAll("SELECT id, fname, lname FROM PARTICIPANT")
        # print(self.members)
        # self.data_list = self.members
        # self.header = ["Id", "First Name", "Surname"]
        # table_model = MyTableModel(self, self.data_list, self.header)
        # self.membersbox = QComboBox()
        # self.membersbox.setModel(table_model)
        #
        #
        # self.membersbox.setMinimumWidth(250)
        #self.formLayout.addRow(self.grouplbl,self.group)
        self.members = dbAll("SELECT id, fname, lname FROM PARTICIPANT")
        #self.membersbox = QLineEdit()
        self.membersbox = QComboBox()

        #self.membersbox.setPlaceholderText("Enter Name")
        print(self.members)
        completernames = []
        for member in self.members:
            self.membersbox.addItem("%s %s"%(member[1],member[2]), userData=member[0].__str__())
            completernames.append("%s %s"%(member[1],member[2]))
        self.membersbox.setEditable(True);

        completer = QCompleter(completernames)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        completer.setCompletionMode(QCompleter.PopupCompletion)
        self.membersbox.setCompleter(completer)

        hLayout1 = QHBoxLayout()

        vLayout1 = QVBoxLayout()

        vLayout2 = QVBoxLayout()
        # add the widgets vertically in that order
        vLayout1.addWidget(self.membersbox)
        vLayout1.addWidget(self.addbutton)


        vLayout2.addWidget(self.resbutton)

        hLayout1.addLayout(vLayout1)
        hLayout1.addLayout(vLayout2)


        hLayout1.addSpacing(5)

        self.setLayout(hLayout1)







class CompetitionWindow(QMainWindow):
    def __init__(self):

        QMainWindow.__init__(self)
        self.setGeometry(300, 100, 800, 400)
        self.setWindowTitle('Manage Members')
        self.exit = QAction('Exit', self)
        self.exit.setStatusTip('Exit Members')
        menubar = self.menuBar()
        file = menubar.addMenu('&File')
        file.addAction(self.exit)
        self.statusBar()

        widget = CompetitionCentralWidget()

        self.setCentralWidget(widget)

    currentInstance = None

    @classmethod
    def getCurrentInstance(cls):
        if cls.currentInstance is None:
            cls.currentInstance = CompetitionWindow()
            return cls.currentInstance
        return cls.currentInstance

