# IMSTimesheet
A simple time tracker program that is useds at the IMS department at CSUDH. Built using python3 and sqlite3.  

---
### Project Organization
constants.py - Program constants, such as colors and size.  
main.py - starts the program, calls the window  
app.py - defines the tkinter application window  

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

