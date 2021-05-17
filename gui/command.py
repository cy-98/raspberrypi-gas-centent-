from tkinter import *


def addCommand(root, text, event, fill=X):
    btn = Button(root, text=text, command=event)
    btn.pack(fill=fill)

