from command import addCommand
from tkinter import *


CELSIUS_LABEL = '摄氏度'


def validate( v ):
    def mustFloat():
        try:
            # validate
            v.get()
        except TclError:
            # msg box
            print('input error')

    return mustFloat


def RegisterCelsius( root ):
    _value = DoubleVar()

    widgets = Frame(root)
    label   = Label(widgets, text=CELSIUS_LABEL)
    scanf   = Entry(widgets, textvariable=_value)

    label.pack(side=LEFT)
    scanf.pack(side=LEFT)
    widgets.pack(side=LEFT, padx=10, pady=10)
    addCommand(widgets, text="确定", event=validate(_value))

    return _value
