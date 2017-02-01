#!/usr/bin/env python3

#Could be used for administrator

from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Administrator Log In")

Label(root, text="Username").pack()
entry = ttk.Entry(root, width = 30)
entry.pack()
entry.get() #input

Label(root, text="Password").pack()
entry2 = ttk.Entry(root, width = 30)
entry2.pack()

loginbutton = ttk.Button(root, text = "Submit", width = 10)
loginbutton.pack()
loginbutton['text']
entry2.config(show = '*')
entry.get()

root.mainloop()
