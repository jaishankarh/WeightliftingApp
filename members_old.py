
__author__ = 'jaishankar'

import threading
import sys
from PySide.QtCore import *
from PySide.QtGui import *
from manageMembers import *


class MembersCentralWidget(QWidget):
    '''
    a QWidget with a typical box layout
    '''
    def __init__(self):
        QWidget.__init__(self)
        self.addbutton = QPushButton('Add', self)
        self.addbutton.setMinimumHeight(70)
        self.addbutton.setMinimumWidth(70)
        self.delbutton = QPushButton('Delete', self)
        self.delbutton.setMinimumHeight(70)
        self.delbutton.setMinimumWidth(70)
        self.listbutton = QPushButton('List', self)
        self.listbutton.setMinimumHeight(70)
        self.listbutton.setMinimumWidth(70)
        self.printbutton = QPushButton('Print', self)
        self.printbutton.setMinimumHeight(70)
        self.printbutton.setMinimumWidth(70)

        hLayout1 = QHBoxLayout()

        hLayout2 = QHBoxLayout()

        vb_layout = QVBoxLayout()
        # add the widgets vertically in that order
        hLayout1.addWidget(self.addbutton)
        hLayout1.addWidget(self.delbutton)
        hLayout2.addWidget(self.listbutton)
        hLayout2.addWidget(self.printbutton)

        vb_layout.addLayout(hLayout1)
        vb_layout.addSpacing(5)
        vb_layout.addLayout(hLayout2)

        self.setLayout(vb_layout)




class MyMembersWindow(QMainWindow):
    '''
    QMainWinodw does not allow box/grid layout, but you can
    make a QWidget instance the central widget to do so
    '''


    def __init__(self):

        # if you want a menubar or statusbar, you have to use
        # QMainWindow since QWidget does not have those
        QMainWindow.__init__(self)
        # setGeometry(x_pos, y_pos, width, height)
        # upper left corner coordinates (x_pos, y_pos)
        self.setGeometry(300, 100, 800, 400)
        self.setWindowTitle('Manage Members')
        # exit option for the menu bar File menu
        self.exit = QAction('Exit', self)
        # message for the status bar if mouse is over Exit
        self.exit.setStatusTip('Exit Members')
        # newer connect style (PySide/PyQT 4.5 and higher)
        #to take care of closed window.......................................
        #self.exit.triggered.connect(app.quit)
        # create the menu bar
        menubar = self.menuBar()
        file = menubar.addMenu('&File')
        # now add self.exit
        file.addAction(self.exit)
        # create the status bar
        self.statusBar()
        # QWidget or its instance needed for box layout
        widget = MembersCentralWidget()
        # make it the central widget of QMainWindow
        self.setCentralWidget(widget)
        #self.label = widget.label


        widget.addbutton.clicked.connect(self.addMember)
        widget.listbutton.clicked.connect(self.listMembers)


    currentInstance = None

    def addMember(self):
        '''
        some action to indicate which button has been clicked
        '''
        admw = AddMemberWidget.getCurrentInstance()
        admw.show()
        admw.raise_()

    def listMembers(self):
        '''
        some action to indicate which button has been clicked
        '''
        admw = ListMemberWidget.getCurrentInstance()
        admw.show()
        admw.raise_()

    @classmethod
    def getCurrentInstance(cls):

        if cls.currentInstance is None:
            cls.currentInstance = MyMembersWindow()
            return cls.currentInstance
        return cls.currentInstance
