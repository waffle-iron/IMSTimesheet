#!/usr/bin/python3

# This file deletes the database and rebuilds it using the database
# interface. This is to assist in development

from app.database.databaseInterface import delete_database
from app.database.databaseInterface import DatabaseInterface

delete_database()  # delete database
di = DatabaseInterface()
#di.check()  # check if exist, if it doesn't create it

