from tkinter import *
import command


def LoadSidebar(window):
    instance = Frame(window, bg="#f88")
    instance.pack(fill=Y, side=LEFT)
    return instance
