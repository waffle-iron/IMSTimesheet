#!/usr/bin/python3
# Rudy Leiva
# 1/31/17

import sqlite3
import os
class DatabaseInterface:
    '''Handles all database functions'''
    def __init__(self, dbFile="IMSTimesheet.db"):
        self.dbFile = dbFile 
        self.check()  # execute the check of the database

    def check(self):
        '''
        This checks to see if the database exists
        It if doesn't we create it
        '''
        if not os.path.isfile(self.dbFile):
            print("No Databse found")
            self.create_database()  # if it doesn't exist create it!
            #print("no!")
            #dbFile = open("IMSTimesheet.db", "w")
            #conn = sqlite3.connect(dbFile)
            #print("Opened database")

    
    def create_database(self):
        print("creating database...")
        conn = sqlite3.connect(self.dbFile)
        conn.execute('''CREATE TABLE TIME_SHEET
                     ( AutoIncrememnt INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                     Name TEXT NOT NULL,
                     DateIn TEXT NOT NULL,
                     DateOut TEXT NOT NULL,
                     ValidEntry INTEGER NULL );''')
        conn.close()

    def punch_in(self, Name, DateIn):
        self.check()
        conn = sqlite3.connect(self.dbFile)
        conn.execute("INSERT INTO TIME_SHEET (Name,DateIn) \
                     VALUES (?, ?)", (Name, DateIn));
        conn.close()

    def punch_out(self, Name, DateOut):
        self.check()
        conn = sqlite3.connect(self.dbFile)
        conn.execute("INSERT INTO TIME_SHEET (Name,DateIn) \
                    VALUES (?, ?)", (Name, DateOut));
        conn.close()

    def delete_database(self):
        print("deleting database")
        os.remove(self.dbFile)
        print("deleted Database!")


"""
TODO:
Need a function to get all users for a given month
Need a function to get all users for all time
"""






