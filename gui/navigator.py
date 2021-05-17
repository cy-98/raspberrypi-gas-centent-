from tkinter import *
from celcius import RegisterCelcius
from param import RegisterWidgets




BACKCOLOR = '#fff'
TITLE     = 'please input your content params'


def LoadNavigator(window, size):
    instance = Frame(window, bg=BACKCOLOR)
    label = Label(instance, text=TITLE, bg=BACKCOLOR)
    
    frames = []
    inputGroups = [RegisterCelcius, RegisterWidgets, RegisterWidgets, RegisterWidgets]
    
    for index in range(len(inputGroups)):
        container = None

        if index % 2 == 0:
            container = Frame(instance, bg=BACKCOLOR)
            frames.append(container)
        else:
            container = frames[len(frames) - 1] # get current frame to mount widget

        widget = inputGroups[index]
        value = widget(container)
        # celcius = RegisterCelcius(groupFrame)


    instance.pack(side=TOP)
    label.pack()
    for frame in frames:
        frame.pack()

    return instance
