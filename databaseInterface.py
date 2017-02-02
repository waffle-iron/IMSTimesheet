#!/usr/bin/python3

import sqlite3
import os
class databaseInterface:
    '''Handles all database functions'''
    dbFile = "IMSTimesheet.db"
    conn = sqlite3.connect(dbFile)

    if os.path.isfile(dbFile):
    print("yes!")



"""
Put db in a folder
Check if database exists
print ("opened database succesfully");"""






