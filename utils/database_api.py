__author__ = 'jaishankar'


#check if config file is present
#if not present then throw an error
#reading the config file intialise the database variables using pickle
#write the other functions that abstract the different functions of the database
#raise errors whenever the database functions don't work as expected

import sqlite3
import os
import pickle

configParameters = {}

class FileNotFoundException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
         return repr(self.value)

class EmptyFileException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
         return repr(self.value)

class EmptyQueryException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
         return repr(self.value)


class NoConfigParameterException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
         return repr(self.value)

def readConfig(fname):
    if type(fname) != type(""):
        raise TypeError
    if not os.path.exists(fname):
        print(os.getcwd())
        raise FileNotFoundException(fname)
    try:
        f = open(fname, 'r')
        p = pickle.Unpickler(f)
        global configParameters
        configParameters = p.load()
        if len(configParameters) == 0:
            raise EmptyFileException
    except (pickle.PickleError, pickle.UnpicklingError):
        return False
    except EOFError:
        raise EmptyFileException




def dbInit():
    if configParameters is None or len(configParameters)==0:
        #raise NoConfigParameterException('Config Parameters missing')
        readConfig("config.inc")
    conn = sqlite3.connect(configParameters['dbName'])
    return conn

def dbQuery(query):
    if query == "":
        raise EmptyQueryException
    conn = dbInit()
    c = conn.cursor()
    c.execute(query)
    conn.commit()
    c.close()

def dbRow(query):
    if query == "":
        raise EmptyQueryException
    conn = dbInit()
    c = conn.cursor()
    c.execute(query)
    #c.commit()
    result = c.fetchone()
    c.close()
    return result

def dbAll(query):
    if query == "":
        raise EmptyQueryException
    conn = dbInit()
    c = conn.cursor()
    c.execute(query)
    #c.commit()
    result = c.fetchall()
    c.close()
    return result

def dbMany(query,size=1):
    if query == "":
        raise EmptyQueryException
    conn = dbInit()
    c = conn.cursor()
    c.execute(query)
    #c.commit()
    result = c.fetchmany()
    c.close()
    return result






