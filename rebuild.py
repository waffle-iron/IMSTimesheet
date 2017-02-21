#!/usr/bin/python3

# This file deletes the database and rebuilds it using the database
# interface. This is to assist in development

from app.database.databaseInterface import DatabaseInterface

print("Deleting database")
di = DatabaseInterface()  # create the database object
# NOTE the above line creates the database
di.delete_database()  # delete database
di.check()  # check if exist, if it doesn't create it

