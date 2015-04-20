__author__ = 'jaishankar'

import threading
import sys
from PySide.QtCore import *
from PySide.QtGui import *

class Trainingthread(threading.Thread):
    def run(self):
        #trainapp = QApplication(sys.argv)
        train = MyTrainingWindow()
        train.show()
        #trainapp.exec_()


class TrainingCentralWidget(QWidget):
    '''
    a QWidget with a typical box layout
    '''
    def __init__(self):
        QWidget.__init__(self)
        self.button1 = QPushButton('Training', self)
        self.button1.setMinimumHeight(70)
        self.button1.setMinimumWidth(70)
        self.button2 = QPushButton('Competition', self)
        self.button2.setMinimumHeight(70)
        self.button2.setMinimumWidth(70)
        self.button3 = QPushButton('Backup', self)
        self.button3.setMinimumHeight(70)
        self.button3.setMinimumWidth(70)
        self.button4 = QPushButton('Print', self)
        self.button4.setMinimumHeight(70)
        self.button4.setMinimumWidth(70)

        hLayout1 = QHBoxLayout()

        hLayout2 = QHBoxLayout()

        vb_layout = QVBoxLayout()
        # add the widgets vertically in that order
        hLayout1.addWidget(self.button1)
        hLayout1.addWidget(self.button2)
        hLayout2.addWidget(self.button3)
        hLayout2.addWidget(self.button4)

        vb_layout.addLayout(hLayout1)
        vb_layout.addSpacing(5)
        vb_layout.addLayout(hLayout2)

        self.setLayout(vb_layout)




class MyTrainingWindow(QMainWindow):
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
        self.setWindowTitle('Training Window')
        # exit option for the menu bar File menu
        self.exit = QAction('Exit', self)
        # message for the status bar if mouse is over Exit
        self.exit.setStatusTip('Exit Training')
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
        widget = TrainingCentralWidget()
        # make it the central widget of QMainWindow
        self.setCentralWidget(widget)
        #self.label = widget.label
        # use lambda to pass a string argument to self.action
        action1 = lambda: self.action('button1')
        widget.button1.clicked.connect(action1)
        action2 = lambda: self.action('button2')
        widget.button2.clicked.connect(action2)
        action3 = lambda: self.action('button3')
        widget.button3.clicked.connect(action3)


    def action(self, s):
        '''
        some action to indicate which button has been clicked
        '''
        sf = '{} clicked'.format(s)
        self.label.setText(sf)