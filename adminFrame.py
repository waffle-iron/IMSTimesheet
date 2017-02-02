#!/usr/bin/env python3

# Vigeneareay Phriang
# Bradley Taniguchi
# 1/31/17
# Could be used for administrator

import tkinter as tk
from tkinter import ttk

class AdminFrame(ttk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)  # make the frame
        self.master = master  # the master is the tkinter window manager
        self.grid()  # use the grid layout manager
        self.create_widgets()  # call the create widget function

    def create_widgets(self):
        self.master.title("Administrator Log In")
        self.username_label = ttk.Label(self, text="Username")
        self.username_entry = ttk.Entry(self, width=30)
        self.password_label = ttk.Label(self, text="Password")
        self.password_entry = ttk.Entry(self, width=30)
        self.loginbutton = ttk.Button(self, text = "Submit", width = 10)
        
        #apply special formatting
        self.password_entry.config(show = '*')


        # now we add the components to the grid
        # we wont use pack(), as grid is better for more complex layouts
        # but as of right now it will function the same as pack()
        self.username_label.grid()
        self.username_entry.grid()

        self.password_label.grid()
        self.password_entry.grid()
        
        self.loginbutton.grid()

# These are for quick testing of this file, 
root = tk.Tk() #  root is the window

# lets use a theme!
root.style = ttk.Style()
#('clam', 'alt', 'default', 'classic')
root.style.theme_use("clam")

root.minsize(width=400, height=400)
app = AdminFrame(master=root)
app.mainloop()
