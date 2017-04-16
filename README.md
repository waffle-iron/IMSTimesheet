[![Stories in Ready](https://badge.waffle.io/bradtaniguchi/IMSTimesheet.png?label=ready&title=Ready)](https://waffle.io/bradtaniguchi/IMSTimesheet)
# IMSTimesheet
A simple time tracker program that is used at the IMS department at CSUDH. Built using python3 and sqlite3.

---
### Project Organization
constants.py - Program constants, such as colors and size.  
main.py - starts the program, calls the window  
io.py - handles file reads-writes
databaseInterface - handles connecting to the sqlite3 database.db

---
### Installation and usage

Be sure your computer has git, python3 and python3-tkinter package installed.
Installation instructions are different for each platform. (google it :D)  

Install using git with the commands:  
`git clone https://github/bradtaniguchi/IMSTimesheet`  
Then run the following command to run:
`python3 main.py`  
NOTE: If you have only 1 verion of python installed, you may use just python

Use the rebuild.py script to delete the database, and create a new one.
Obviously the deletes all data so be careful!

---
### Development Resources

Here is an article for a basic tkinter app.  
http://usingpython.com/making-widgets-look-nice/  

---
### Project Steps
1. Create primary UI, hardcode user values, research time handling
2. Impliment sqlite3 database, with time handling
3. Impliment config text file, and write to file capabilities
4. Create Admin UI, yearly timesheet printouts.

----
### Database columns
1. autoincrement (int)
2. name (string)
3. clockIn (datetime)
4. clockOut (datetime)
5. valid entry (boolean) - used to identify invalid clockOut dates

