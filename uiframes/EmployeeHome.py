from tkinter import *
import tkinter as tk
from tkinter import ttk

from .SuccessPopup import SuccessPopup

class EmployeeHome(ttk.Frame):
    def __init__(self, parent=None, controller=None):
        tk.Frame.__init__(self, parent)
        self.parent = parent
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
        self.admin = ttk.Button(self, text = 'Administrator')
        self.printRecords = ttk.Button(self, text = 'Print Records')

        #render them to the tkinter gui
        self.clock_in_button.grid(row=0, column=0, padx = 10, pady=10,ipadx = 10, ipady=10)
        self.clock_out_button.grid(row=1, column =0, padx = 10, pady=10, ipadx = 10, ipady=10)
        self.printRecords.grid(row=2, column=0, padx = 10, pady=10, ipadx = 10, ipady=10)
        self.employee_in.grid(row=0, column=3, padx=10, pady=10, ipadx=10, ipady=10)
        self.employee_out.grid(row=1, column=3, padx=10, pady=10, ipadx=10, ipady=10)
        
        #add click listeners
        #self.clock_in.configure(command=lambda: self.clock_in())
        #self.clock_out.bind('<Button-1>', self.clock_out)


    def get_logged_in_employees(self):
        '''
        Gets the employees that are clockedIn from the database.
        '''
        return []; # for now return nothing

    def clock_in(self):
        print("Clocking in user: " + str(self.employee_in.get()));
        self.employee_in.set('')
        my_popup = SuccessPopup("Successful Clock in", \
                "Successfully clocked in user: " + str(self.employee_in.get()))
        my_popup.mainloop()

    def clock_out(self):
        print("Clocking out user: " + str(self.employee_out.get()));
        self.employee_out.set('')
        my_popup = SuccessPopup("Successful Clockout", \
                "Successfully clocked out user: " + str(self.employee_out.get()))
        my_popup.mainloop()
