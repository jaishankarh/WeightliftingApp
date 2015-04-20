__author__ = 'jaishankar'

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtSql import *
from PySide.QtCore import Signal
from utils.database_api import *
from datetime import date


class Member:
    def __init__(self):
        self.fname = ""
        self.lname = ""
        self.gender = ""
        self.group = ""
        self.dob = date()

    @classmethod
    def addNewMember(self,fname, lname, gen, grp, dob):
        query = "INSERT INTO MEMBER(fname, lname, grp) VALUES('%s', '%s', '%s')" %(self.fname.text(),self.lname.text(),self.groups[self.group.currentIndex()])
        dbQuery(query)
