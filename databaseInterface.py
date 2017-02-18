#!/usr/bin/python3
# Rudy Leiva
# 1/31/17

import sqlite3
import os
class databaseInterface:
    '''Handles all database functions'''
    global dbFile
    dbFile = "IMSTimesheet.db"
    #conn = sqlite3.connect(dbFile)

    if not os.path.isfile(dbFile):
         print("no!")
         dbFile = open("IMSTimesheet.db", "w")
         conn = sqlite3.connect(dbFile)
         print("Opened datatbase")

         conn.execute('''CREATE TABLE TIME_SHEET
                      ( AutoIncrememnt INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                      Name TEXT NOT NULL,
                      DateIn TEXT NOT NULL,
                      DateOut TEXT NOT NULL,
                      ValidEntry INTEGER NULL );''')


    else:
        print("Yes!")
        print("Connection successful")

        def punchIn(self, Name, DateIn):
            conn = sqlite3.connect(dbFile)
            conn.execute("INSERT INTO TIME_SHEET (Name,DateIn) \
                        VALUES (" + Name + "," + DateIn + ")");

        def punchOut(self, Name, DateOut):
            conn = sqlite3.connect(dbFile)
            conn.execute("INSERT INTO TIME_SHEET (Name,DateIn) \
                        VALUES (" + Name + "," + DateOut + ")");


"""
Put db in a folder
Check if database exists
print ("opened database succesfully");"""






