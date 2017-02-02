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

        #match the resizing
        self.rowconfigure(0, weight = 3)
        self.rowconfigure(1, weight = 3)
        self.columnconfigure(0, weight = 3)
        self.columnconfigure(1, weight = 3)

        self.clock_in =ttk.Button(self, text = 'Clock In')
        self.clock_out =ttk.Button(self, text = 'Clock Out')
        self.admin=ttk.Button(self, text = 'Administrator')
        self.printRecords=ttk.Button(self, text = 'Print Records')

        self.clock_in.grid(row=0, column=0, padx = 10, pady=10,ipadx = 25, ipady=25)
        self.clock_out.grid(row=1, column =0, padx = 10, pady=10, ipadx = 25, ipady=25)
        self.admin.grid(row=0, column=1, padx = 10, pady=10, ipadx = 25, ipady=25)
        self.printRecords.grid(row=1, column=1, padx = 10, pady=10, ipadx = 25, ipady=25)

        mb = Menubutton(self, text="condiments", relief=RAISED)
        mb.grid()
        mb.menu = Menu(mb, tearoff=0)
        mb["menu"] = mb.menu

        mayoVar = IntVar()
        ketchVar = IntVar()

        mb.menu.add_checkbutton(label="mayo",
                                variable=mayoVar)
        mb.menu.add_checkbutton(label="ketchup",
                                variable=ketchVar)


root = tk.Tk()


app1= EmployeeHome(master=root)
app1.mainloop()