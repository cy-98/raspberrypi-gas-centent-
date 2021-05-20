from tkinter import *


def addCommand(root, text, event, fill=X, padx=0, pady=0):
    btn = Button(root, text=text, command=event)
    btn.pack(fill=fill, padx=padx, pady=pady)
