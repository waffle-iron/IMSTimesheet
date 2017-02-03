from tkinter import *
import tkinter as tk
from tkinter import ttk

class EmployeeHome(ttk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.master.title("Employee Clock In System")
        month = StringVar()
        #set value of the combobox
        self.month2 = ttk.Combobox(self, textvariable=month)
        self.month2.config(values=('Jan', 'Feb', "March"))
        self.combobox = ttk.Combobox(self, textvariable=month)
        self.combobox.config(values=('Jan', 'Feb', "March"))

        print(month.get())
        month.set('Jan')
        month.set('Not a month!')

        #match the resizing of the window
        self.rowconfigure(0, weight=3)
        self.rowconfigure(1, weight=3)
        self.columnconfigure(0, weight=3)
        self.columnconfigure(1, weight=3)

        #instantiate all buttons
        self.clock_in =ttk.Button(self, text = 'Clock In')
        self.clock_out =ttk.Button(self, text = 'Clock Out')
        self.admin=ttk.Button(self, text = 'Administrator')
        self.printRecords=ttk.Button(self, text = 'Print Records')

        #render them to the tkinter gui
        self.clock_in.grid(row=0, column=0, padx = 10, pady=10,ipadx = 10, ipady=10)
        self.clock_out.grid(row=1, column =0, padx = 10, pady=10, ipadx = 10, ipady=10)
        self.printRecords.grid(row=2, column=0, padx = 10, pady=10, ipadx = 10, ipady=10)
        self.combobox.grid(row=2, column=3, padx = 10, pady=10, ipadx = 10, ipady=10)
        self.combobox.grid(row=1, column=3, padx=10, pady=10, ipadx=10, ipady=10)
        self.month2.grid(row=0, column=3, padx=10, pady=10, ipadx=10, ipady=10)

root = tk.Tk()
app1= EmployeeHome(master=root)
app1.mainloop()