#!/usr/bin/python3
# Rudy Leiva
# 1/31/17

import sqlite3
import os
class DatabaseInterface:
    """
    Handles all database functions for the application. 
    Authors: 
        Rudy Leiva
        Bradley Taniguchi
    """
    def __init__(self, dbFile="IMSTimesheet.db"):
        self.dbFile = dbFile 
        self.check()  # execute the check of the database

    def check(self):
        """
        This checks to see if the database exists
        It if doesn't we create it
        """
        if not os.path.isfile(self.dbFile):
            print("No Databse found")
            self.create_database()  # if it doesn't exist create it!
            #print("no!")
            #dbFile = open("IMSTimesheet.db", "w")
            #conn = sqlite3.connect(dbFile)
            #print("Opened database")

    
    def create_database(self):
        """
        Creates the database file using the database filename provided to the
        database object upon init.
        """
        print("creating database...")
        conn = sqlite3.connect(self.dbFile)
        conn.execute('''CREATE TABLE TIME_SHEET
                     ( AutoIncrememnt INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                     Name TEXT NOT NULL,
                     DateIn TEXT NOT NULL,
                     DateOut TEXT,
                     ValidEntry INTEGER NULL );''')
        conn.close()

    def punch_in(self, Name, DateIn):
        """
        Function to clock-in a user at the given time, with the given name.
        Leaves the DateOut as null
        Args:
            Name (str): name of the user to save, this is part of the 
                primary key, so the name cannot change!
            DateIn (str): string representation of the date, be sure the
                format is determined beforehand, as the clockout does not logic
                to check the date format.
        """
        self.check()
        conn = sqlite3.connect(self.dbFile)
        conn.execute("INSERT INTO TIME_SHEET (Name,DateIn) \
                     VALUES (?, ?)", (Name.lower(), DateIn));
        conn.close()
    def check_user(self, Name):
        """
        Checks if the Name is already clocked in according to the system.
        Args: 
            Name (string): name of the user we want to check
        Returns:
            bool: If the length of the number of users returned with the given
                name, where their clock out times is null is GREATER than 1.
        """
        self.check()
        conn = sqlite3.connect(self.dbFile)
        users = conn.execute("SELECT * FROM TIME_SHEET \
                WHERE Name=? AND \
                DateOut is NULL", Name.lower()).fetchall()
        conn.close()
        return (len(users) >= 1)

    def punch_out(self, Name):
        """
        clocks-out a user with the given name, this function clocks out the
        LAST login time. The database should not be filled with more than 1
        Args:
            Name (str): Name of the user to clock out from the database
                we apply to lower case just incase
        Todo: Fix this function, as it doesn't do whats intended
        """
        self.check()
        conn = sqlite3.connect(self.dbFile)
#        conn.execute("INSERT INTO TIME_SHEET (Name,DateIn) \
#                    VALUES (?, ?)", (Name.lower(), DateOut));
        conn.close()

    def delete_database(self):
        """
        utility function to delete the database file.
        """
        print("deleting database")
        os.remove(self.dbFile)
        print("deleted Database!")


"""
TODO:
Need a function to get all users for a given month
Need a function to get all users for all time
"""






