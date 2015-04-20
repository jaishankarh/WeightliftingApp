__author__ = 'jaishankar'
import database_api
import os
from database_api import dbAll
from database_api import dbQuery
from database_api import dbRow
from database_api import dbMany



#if not os.path.exists('config.inc'):


database_api.readConfig("config.inc")
#print database_api.configParameters
conn = database_api.dbInit()
dbQuery('CREATE TABLE IF NOT EXISTS PARTICIPANT(id INTEGER PRIMARY KEY AUTOINCREMENT, fname VARCHAR(30), lname VARCHAR(30), grp VARCHAR(2))')
dbQuery("CREATE TABLE IF NOT EXISTS LIFTS(id INTEGER PRIMARY KEY AUTOINCREMENT, liftType VARCHAR(30), liftName VARCHAR(30))")
dbQuery("CREATE TABLE IF NOT EXISTS COEFFICIENTS(id INTEGER PRIMARY KEY AUTOINCREMENT, liftid INTEGER, value REAL, FOREIGN KEY(liftid) REFERENCES LIFTS(id) ON DELETE CASCADE)")

