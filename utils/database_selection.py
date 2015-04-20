__author__ = 'jaishankar'

import sys
from PySide.QtCore import *
from PySide.QtGui import *

app = QApplication(sys.argv)






class DatabaseSelectWindow(QWidget):
    '''This is an example which demonstrates the use of absolute positioning..'''
    def __init__(self):
        self.title = "Choose Database"
        QWidget.__init__(self)

        self.newDatabasename = ''
        self.filename = ''
        #self.setMinimumSize(400,400)
        self.setWindowTitle(self.title)


        self.layout = QVBoxLayout()


        self.choose_lbl = QLabel("It looks like you have not configured a database yet, please choose one of the options below.")
        #self.salutation_lbl.move(5,5)
        self.layout.addWidget(self.choose_lbl)

        self.layout.addStretch(1)

        self.buttonBox = QHBoxLayout()

        self.newButton = QPushButton('&New Database')

        self.buttonBox.addWidget(self.newButton)


        self.oldButton = QPushButton('&Saved Database')

        self.buttonBox.addWidget(self.oldButton)

        self.layout.addLayout(self.buttonBox)

        self.setLayout(self.layout)




        self.oldButton.clicked.connect(self.showFileBrowser)
        self.newButton.clicked.connect(self.showNewText)


        #self.move(5,60)
    @Slot()
    def showFileBrowser(self):
        self.filename = QFileDialog.getOpenFileName(self);


    @Slot()
    def showNewText(self):
        text, ok = QInputDialog.getText(self, 'New Database Name', 'Enter new name:')

        if ok:
            self.newDatabasename = str(text)

        #self.greeting.setText('%s %s,' %(self.salutations[self.salutation.currentIndex()],self.recipient.text()))




    def run(self):
        self.show()
        app.exec_()

qt_app = DatabaseSelectWindow()
qt_app.run()