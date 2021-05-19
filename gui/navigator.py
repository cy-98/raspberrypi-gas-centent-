from tkinter import *
from celcius import RegisterCelcius
from param import RegisterWidgets




BACKCOLOR = '#fff'
TITLE     = 'please input your content params'


def last(arr):
    return arr[len(arr) - 1]


def loadInputWidgets( root, widgets ):
    values = []
    frames = []

    for index in range(len(widgets)):
        frame = None

        if index % 2 == 0:
            frame = Frame(root, bg=BACKCOLOR)
            frames.append(frame)
        else:
            frame = last(frames)

        widget = widgets[index]
        value = widget(frame)
        values.append(value)
    return frames, values


def LoadNavigator( root, size ):
    form = Frame(root, bg=BACKCOLOR)
    label = Label(form, text=TITLE, bg=BACKCOLOR)
    
    inputGroups = [RegisterCelcius, RegisterWidgets, RegisterWidgets, RegisterWidgets]
    frames, values = loadInputWidgets(form, inputGroups) # TODO: values

    form.pack(side=TOP)
    label.pack()
    for frame in frames:
        frame.pack()

    return form
