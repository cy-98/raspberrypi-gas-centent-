from tkinter import *
from param import *





BACKCOLOR = '#fff'
TITLE     = '请输入计算参数'


def last(arr):
    return arr[len(arr) - 1]


def loadInputWidgets( root, widgets ):
    frames = []

    for index in range(len(widgets)):
        frame = None

        if index % 2 == 0:
            frame = Frame(root, bg=BACKCOLOR)
            frames.append(frame)
        else:
            frame = last(frames)

        widget = widgets[index]
        widget(frame)

    return frames


def LoadNavigator( root, size ):
    form = Frame(root, bg=BACKCOLOR)
    label = Label(form, text=TITLE, bg=BACKCOLOR)

    inputGroups = [RegisterCelsius, RegisterVolume, RegisterDensity, RegisterGravity, RegisterArea]
    frames = loadInputWidgets(form, inputGroups)
    form.pack(side=TOP)
    label.pack()
    for frame in frames:
        frame.pack()

    return form
