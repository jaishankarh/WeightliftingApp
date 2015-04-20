# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Sun Jul  6 13:09:09 2014
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui
from members.memberswindow import ControlMembersWindow
from competition.competition_select import ControlCompetitionSelectWindow
from members.output import *
from printfn.print_select import *
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 30, 221, 421))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.training = QtGui.QPushButton(self.verticalLayoutWidget)
        self.training.setMinimumSize(QtCore.QSize(0, 35))
        self.training.setObjectName("training")
        self.verticalLayout.addWidget(self.training)
        self.competition = QtGui.QPushButton(self.verticalLayoutWidget)
        self.competition.setMinimumSize(QtCore.QSize(0, 35))
        self.competition.setObjectName("competition")
        self.verticalLayout.addWidget(self.competition)
        self.members = QtGui.QPushButton(self.verticalLayoutWidget)
        self.members.setMinimumSize(QtCore.QSize(0, 35))
        self.members.setObjectName("members")
        self.verticalLayout.addWidget(self.members)
        self.backup = QtGui.QPushButton(self.verticalLayoutWidget)
        self.backup.setMinimumSize(QtCore.QSize(0, 35))
        self.backup.setObjectName("backup")
        self.verticalLayout.addWidget(self.backup)
        self.printbutt = QtGui.QPushButton(self.verticalLayoutWidget)
        self.printbutt.setMinimumSize(QtCore.QSize(0, 35))
        self.printbutt.setObjectName("printbutt")
        self.verticalLayout.addWidget(self.printbutt)
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(470, 70, 241, 331))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.label.setPixmap(QtGui.QPixmap("resources/images/main.png"))
        self.label.setScaledContents(True);
        self.horizontalLayout.addWidget(self.label)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        #self.training.clicked.connect(self.action1)
        self.members.clicked.connect(self.openMemberWindow)
        self.printbutt.clicked.connect(self.openPrintWindow)
        self.competition.clicked.connect(self.openCompetitionWindow)
        #self.competition.clicked.connect(self.openCompWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.training.setText(QtGui.QApplication.translate("MainWindow", "Training", None, QtGui.QApplication.UnicodeUTF8))
        self.competition.setText(QtGui.QApplication.translate("MainWindow", "Competition", None, QtGui.QApplication.UnicodeUTF8))
        self.members.setText(QtGui.QApplication.translate("MainWindow", "Members", None, QtGui.QApplication.UnicodeUTF8))
        self.backup.setText(QtGui.QApplication.translate("MainWindow", "Backup", None, QtGui.QApplication.UnicodeUTF8))
        self.printbutt.setText(QtGui.QApplication.translate("MainWindow", "Print", None, QtGui.QApplication.UnicodeUTF8))
        #self.label.setText(QtGui.QApplication.translate("MainWindow", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))


    def openMemberWindow(self):
        self.memWin = ControlMembersWindow.getCurrentInstance()

        #memWin = Ui_MembersWindow()
        print(self.memWin)
        self.memWin.show()
        self.memWin.raise_()

    def openCompetitionWindow(self):
        self.compWin = ControlCompetitionSelectWindow.getCurrentInstance()

        #memWin = Ui_MembersWindow()
        print(self.compWin)
        self.compWin.show()
        self.compWin.raise_()

    def openPrintWindow(self):
        self.printWin = ControlPrintSelectWindow.getCurrentInstance()
        self.printWin.show()
        self.printWin.raise_()
    # def openCompWindow(self):
    #     compWin = CompetitionWindow.getCurrentInstance()
    #     print(compWin)
    #     compWin.show()
    #     compWin.raise_()



class ControlMainWindow(QtGui.QMainWindow):
  def __init__(self, parent=None):
    super(ControlMainWindow, self).__init__(parent)
    self.ui =  Ui_MainWindow()
    self.ui.setupUi(self)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    mySW = ControlMainWindow()
    mySW.show()
    sys.exit(app.exec_())