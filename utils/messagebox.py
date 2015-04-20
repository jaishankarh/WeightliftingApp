
from PySide.QtGui import *

class CriticalMessage:

    def showMessage(self, msg):
        msgBox = QMessageBox()
        msgBox.setText(msg)
        msgBox.setStandardButtons()
        msgBox.exec_()