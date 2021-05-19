from tkinter import *
import command

def LoadSidebar(window, size) -> Frame:
    instance = Frame(window, bg="#f88")
    instance.pack(fill=Y, side=LEFT)
    command.addCommand(instance, 'asd', None)
    command.addCommand(instance, 'asasdad', None)
    return instance