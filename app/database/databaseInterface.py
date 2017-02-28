#!/usr/bin/python3
# Rudy Leiva
# 1/31/17

import sqlite3
import os
from datetime import datetime


class DatabaseInterface:
    """
    Handles all database functions for the application. 
    Authors: 
        Rudy Leiva
        Bradley Taniguchi
    Todo: Add exception handling to all sql functions, and save the connections
        to prevent redundant opening and closing of connections. 
    """
    def __init__(self, dbFile="IMSTimesheet.db"):
        self.dbFile = dbFile
        self.check()  # execute the check of the database
        self.conn = sqlite3.connect(dbFile) # object database conn

       
    def __del__(self):
        """
        deconstructor method, used to close the database connection.
        """
        print("closing database conn")
        self.conn.close()


    def check(self):
        """
        This checks to see if the database exists
        It if doesn't we create it.
        If the database already exists we need to check the null date entires
        if theose entry dates are not todays date, we close them and label
        them invalid. (they didn't clock out for the day)
        """
        if not os.path.isfile(self.dbFile):
            print("No Database found")
            self.create_database()  # if it doesn't exist create it!
        else: 
            '''
            The database exists, so we need to check the latest entries
            if those entry dates are NOT todays date, and are still open
            we close them
            '''
            print("Database found, checking integrity..")
            time = datetime.now().strftime("%m-%d-%y %H:%M:%S")
            print("Current time: " + time)
            # First I need to get those clocked-in
            self.conn = sqlite3.connect(self.dbFile)
            users = self.conn.execute("SELECT * FROM \
            TIME_SHEET WHERE DateOut is NULL").fetchall()
            print("users loggedin " + str(users))
            
            #self.conn.execute("UPDATE TIME_SHEET SET \
            #        DateOut=?, ValidEntry=? WHERE \
            #        DateOut is NULL;", ('????', -1))


    def get_users(self):
        """
        Gets the users currently logged into the database.
        These are defined by not having the clockout column filled
        """
        return self.conn.execute("SELECT Name FROM TIME_SHEET WHERE \
                DateOut is NULL;").fetchall()

    def create_database(self):
        """
        Creates the database file using the database filename provided to the
        database object upon init.
        """
        print("creating database")
        conn = sqlite3.connect(self.dbFile) # note this is a LOCAL conneciton, just to create the database
        conn.execute('''CREATE TABLE TIME_SHEET
                         ( AutoIncrememnt INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                         Name TEXT NOT NULL,
                         DateIn TEXT NOT NULL,
                         DateOut TEXT,
                         ValidEntry INTEGER NULL );''')

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
        Returns: boolean value if the punch in was successful
        """
        self.check()
        #lets check to see if the user is already clocked in
        if(not self.check_user(Name)):
            print("User not clocked in, clocking in...")
            self.conn.execute("INSERT INTO TIME_SHEET (Name,DateIn) \
                        VALUES (?, ?);", (str(Name.lower()), DateIn))
            self.conn.commit()
            return True

        else: 
            #user is already clocked in!
            print("User is already clocked in")
            return False


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
        users = self.conn.execute("SELECT * FROM TIME_SHEET \
                WHERE Name='%s' AND \
                DateOut is NULL;" % Name.lower()).fetchall()
        return (len(users) >= 1)

    def punch_out(self, Name, DateOut, ValidEntry=1):
        """
        clocks-out a user with the given name, this function clocks out the
        LAST login time. The database should not be filled with more than 1
        Args:
            Name (str): Name of the user to clock out from the database
                we apply to lower case just incase
            DateOut (str): Date and time of the clockout to put.
            ValidEntry (int): If the entry is valid
                defaults to 1 for valid
        Todo: Fix this function, as it doesn't do whats intended
        """
        self.check()
        print("database check " + DateOut + " " + str(ValidEntry) + " " +Name)
        self.conn.execute("UPDATE TIME_SHEET SET \
                    DateOut=?, ValidEntry=? WHERE\
                    Name=? AND DateOut is NULL;", (DateOut, ValidEntry, Name))
        self.conn.commit()

def delete_database():
    """
    utility function to delete the database file.
    """
    if os.path.isfile('IMSTimesheet.db'):
        os.remove("IMSTimesheet.db")
        print("deleted Database!")


"""
TODO:
Need a function to get all users for a given month
Need a function to get all users for all time
"""






