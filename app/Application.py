#!/usr/bin/python3
# Bradley Taniguchi
# 2/2/17
# http://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter

import tkinter as tk
from tkinter import ttk

from .AdminFrame import AdminFrame  # import frames here
from .EmployeeHome import EmployeeHome
from .ioHandler import read_config

class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # add themes and other attribs to the Window
        self.style = tk.ttk.Style()  # use ttk themes
        self.style.theme_use("clam")
        self.minsize(width=200, height=200)
        self.title("IMSTimesheeet")
        self.users = read_config(verbose=True) # passed number of users.
        # handle multiple containers below
        container = tk.Frame(self) # hold all frames in this frame
        container.pack(side="top", fill="both", expand=True)
#        container.grid_configure(0, weight=1)
#        container.grid_columnconfigure(0, weight=1)

        self.frames={}
        frameObjects = [EmployeeHome, AdminFrame]  # add new frames here
        for F in frameObjects:
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("EmployeeHome")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()  # switch window
