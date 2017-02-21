#!/usr/bin/env python3

# Vigeneareay Phriang
# Bradley Taniguchi
# 1/31/17
# Could be used for administrator

import tkinter as tk
from tkinter import ttk
from .Constants import Colors

class AdminFrame(ttk.Frame):
    def __init__(self, parent=None, controller=None):
        tk.Frame.__init__(self, parent)  # make the frame
        self.grid()  # use the grid layout manager
        self.configure(background=Colors.BLUE)
        self.create_widgets()  # call the create widget function

    def create_widgets(self):
        self.username_label = ttk.Label(self, text="Username", background=Colors.BLUE)
        self.username_entry = ttk.Entry(self, width=30)
        self.password_label = ttk.Label(self, text="Password", background=Colors.BLUE)
        self.password_entry = ttk.Entry(self, width=30)
        self.loginbutton = ttk.Button(self, text = "Submit", width=10)
        
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

