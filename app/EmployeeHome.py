from tkinter import *
import tkinter as tk
from tkinter import ttk
from datetime import datetime
import os
from .SuccessPopup import SuccessPopup
from .Constants import DateFormat
from .database.databaseInterface import DatabaseInterface
from .ioHandler import write_to_file


class EmployeeHome(ttk.Frame):
    def __init__(self, parent=None, controller=None):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.database = DatabaseInterface()
        self.grid()
        self.users = controller.users  #get the users from the Application
        self.create_widgets()


    def create_widgets(self):
        #self.parent.title("Employee Clock In System")
        self.employee_in_text = StringVar()
        self.employee_out_text = StringVar()
        #set value of the combobox
        self.employee_in = ttk.Combobox(self, state='readonly') 
        self.employee_in.config(values=self.users)
        self.employee_out = ttk.Combobox(self, state='readonly') 
        self.employee_out.config(values=self.get_logged_in_employees())

        #set default text in combo boxes
        self.employee_in.set('')
        self.employee_out.set('')

        #match the resizing of the window
        self.rowconfigure(0, weight=3)
        self.rowconfigure(1, weight=3)
        self.columnconfigure(0, weight=3)
        self.columnconfigure(1, weight=3)

        #instantiate all buttons
        self.clock_in_button =ttk.Button(self, text = 'Clock In', command=lambda : self.clock_in())
        self.clock_out_button =ttk.Button(self, text = 'Clock Out', command=lambda : self.clock_out())
        self.admin = ttk.Button(self, text = 'Administrator')  # not currently used
        self.printRecords = ttk.Button(self, text = 'Print Records', command=lambda: self.print_database())
        self.printSingleRecord = ttk.Button(self, text='Single record', command=lambda: self.print_database_user())

        #render them to the tkinter gui
        self.clock_in_button.grid(row=0, column=0, padx = 10, pady=10,ipadx = 10, ipady=10)
        self.clock_out_button.grid(row=1, column =0, padx = 10, pady=10, ipadx = 10, ipady=10)
        self.printRecords.grid(row=2, column=0, padx = 10, pady=10, ipadx = 10, ipady=10)
        self.printSingleRecord.grid(row=2, column=3, padx=10, pady=10, ipadx=10, ipady=10)
        self.employee_in.grid(row=0, column=3, padx=10, pady=10, ipadx=10, ipady=10)
        self.employee_out.grid(row=1, column=3, padx=10, pady=10, ipadx=10, ipady=10)
        
        #add click listeners
        #self.clock_in.configure(command=lambda: self.clock_in())
        #self.clock_out.bind('<Button-1>', self.clock_out)


    def get_logged_in_employees(self):
        '''
        Gets the employees that are clockedIn from the database.
        '''
        #database = DatabaseInterface()        
        users = self.database.get_users()
        return users

    def clock_in(self):
        name = str(self.employee_in.get())  # get username as string
        if name:  # if its not empty
            time = datetime.now().strftime(DateFormat.FORMAT)  #get time right now
            print("Clocking in user: " + name);
            print("current time: "  + time)
            self.employee_in.set('')
            #actually peform the clockin
            #database = DatabaseInterface()
    
            if self.database.punch_in(name, time):  #if we actually clocked in

                my_popup = SuccessPopup("Successful Clock in", \
                        "Successfully clocked in user: " + name)
                self.employee_out.config(values=self.get_logged_in_employees())
                my_popup.mainloop()
            else:  # the user is already clocked in
                my_popup = SuccessPopup("User Clocked In", "User "+name+" is already clocked in")
                my_popup.mainloop()

        else:
            my_popup = SuccessPopup("Error!" , \
                    "Enter a valid name!")
            my_popup.mainloop()

    def clock_out(self):
        print("Clocking out user: " + str(self.employee_out.get()));
        name = str(self.employee_out.get())
        if name:
            self.employee_out.set('')
            time = datetime.now().strftime(DateFormat.FORMAT)
            #database = DatabaseInterface()
            self.database.punch_out(name, time)
        

            my_popup = SuccessPopup("Successful Clockout", \
                    "Successfully clocked out user: " + name)
            self.employee_out.config(values=self.get_logged_in_employees())  #update list
            my_popup.mainloop()

    def print_database(self):
        print("Printing database..." + os.getcwd())
        users = self.database.get_report_month()
        write_to_file(users)
        my_popup = SuccessPopup("Printed Database", \
                "Printed database at path: " +os.getcwd())
        my_popup.mainloop()

    def print_database_user(self):
        name = self.employee_in.get().lower()  # get the user we want to get the data for
        if name:  # if name isn't empty

            self.employee_in.set("")

            print("Printing database for user: " + name + "...")
            users = self.database.get_report_user(name)
            write_to_file(users)

            my_popup = SuccessPopup("Printed Database for user:" + name, \
                "Printed database at path: " + os.getcwd())
            my_popup.mainloop()
        else :  # the name field is empty
            my_popup = SuccessPopup("Error", "No username in clockin field! Cant print!")
            my_popup.mainloop()
