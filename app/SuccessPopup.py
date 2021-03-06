#!/usr/bin/python3

from tkinter import ttk
import tkinter as tk

class SuccessPopup(tk.Toplevel):
    def __init__(self, title="title", text="Text"):
        '''
        Generic success popup window. Takes a title and text argument to 
        display.
        :param title: the title of the window
        :param text: the text to display within the window
        '''
        tk.Toplevel.__init__(self)
        self.title(title)
        self.minsize(300, 300)
        self.maxsize(300, 300)

        self.msg = tk.Message(self, text=text, padx=5, pady=5, width=250)
        self.button = ttk.Button(self, text="ok", command=self.exit)

        # center the popup in the window
        self.tk.eval('tk::PlaceWindow %s center' % self.winfo_pathname(self.winfo_id()))
        
        # handle placements
        self.msg.place(rely=0.1, relwidth=1.0)
        self.button.place(relx=0.5, rely=0.5, relwidth=1.0, anchor=tk.CENTER)

    def exit(self):
        '''
        Quits the popup window
        '''
        self.quit()
        self.destroy()

#new_window = SuccessPopup()

