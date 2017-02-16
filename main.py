#!/usr/bin/python3

from tkinter import ttk
from tkinter import ttk
from uiframes.Application import Application
from uiframes.ioHandler import write_to_file
from uiframes.ioHandler import read_config


def main():
    '''
    using ioHanlder, we need to read the config files, then pass them to the
    application root.
    '''
    users = read_config(verbose=True)
    root = Application(users=users)
    root.mainloop()


if __name__ == '__main__':
    main()

