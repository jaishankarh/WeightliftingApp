__author__ = 'jaishankar'

import sys
import threading
from PySide.QtCore import *
from PySide.QtGui import *
from training import Trainingthread
from members import MyMembersWindow
from competition import *


class CentralWidget(QWidget):
    '''
    a QWidget with a typical box layout
    '''
    def __init__(self):
        QWidget.__init__(self)
        self.trainbutton = QPushButton('Training', self)
        self.trainbutton.setMinimumHeight(70)
        self.trainbutton.setMinimumWidth(70)
        self.compbutton = QPushButton('Competition', self)
        self.compbutton.setMinimumHeight(70)
        self.compbutton.setMinimumWidth(70)
        self.backbutton = QPushButton('Backup', self)
        self.backbutton.setMinimumHeight(70)
        self.backbutton.setMinimumWidth(70)
        self.printbutton = QPushButton('Print', self)
        self.printbutton.setMinimumHeight(70)
        self.printbutton.setMinimumWidth(70)
        self.memberbutton = QPushButton('Members', self)
        self.memberbutton.setMinimumHeight(70)
        self.memberbutton.setMinimumWidth(70)


        hLayout1 = QHBoxLayout()

        hLayout2 = QHBoxLayout()

        vb_layout = QVBoxLayout()
        # add the widgets vertically in that order
        hLayout1.addWidget(self.trainbutton)
        hLayout1.addWidget(self.compbutton)
        hLayout2.addWidget(self.backbutton)
        hLayout2.addWidget(self.printbutton)
        hLayout2.addWidget(self.memberbutton)

        vb_layout.addLayout(hLayout1)
        vb_layout.addSpacing(5)
        vb_layout.addLayout(hLayout2)

        self.setLayout(vb_layout)


class MyWindow(QMainWindow):
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
        self.setWindowTitle('Exploring QMainWindow')
        # exit option for the menu bar File menu
        self.exit = QAction('Exit', self)
        # message for the status bar if mouse is over Exit
        self.exit.setStatusTip('Exit program')
        # newer connect style (PySide/PyQT 4.5 and higher)
        self.exit.triggered.connect(app.quit)
        # create the menu bar
        menubar = self.menuBar()
        file = menubar.addMenu('&File')
        # now add self.exit
        file.addAction(self.exit)
        # create the status bar
        self.statusBar()
        # QWidget or its instance needed for box layout
        widget = CentralWidget()
        # make it the central widget of QMainWindow
        self.setCentralWidget(widget)
        #self.label = widget.label
        # use lambda to pass a string argument to self.action
        #action1 = lambda: self.action('trainbutton')
        widget.trainbutton.clicked.connect(self.action1)
        widget.memberbutton.clicked.connect(self.openMemberWindow)
        widget.compbutton.clicked.connect(self.openCompWindow)
        # action2 = lambda: self.action('compbutton')
        # widget.compbutton.clicked.connect(action2)
        # action3 = lambda: self.action('backbutton')
        # widget.backbutton.clicked.connect(action3)


    def action1(self):
        '''
        some action to indicate which button has been clicked
        '''
    def openMemberWindow(self):
        memWin = MyMembersWindow.getCurrentInstance()
        print(memWin)
        memWin.show()
        memWin.raise_()

    def openCompWindow(self):
        compWin = CompetitionWindow.getCurrentInstance()
        print(compWin)
        compWin.show()
        compWin.raise_()


app = QApplication(sys.argv)
win = MyWindow()
win.show()
app.exec_()

