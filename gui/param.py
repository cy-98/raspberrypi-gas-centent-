from tkinter import *
from validate import *
from command import addCommand




COMMAND_LABEL = '确定'
CELSIUS_LABEL = '摄氏度'
DENSITY_LABEL = '密度'
VOLUME_LABEL = '体积'
GRAVITY_LABEL = '重力加速度'
AREA_LABEL = '管道横截面积'


def RegisterWidgets( root ):
    _value = IntVar()

    widgets = Frame(root)
    label   = Label(widgets, text="other params")
    scanf   = Entry(widgets, textvariable=_value)

    label.pack(side=LEFT)
    scanf.pack(side=LEFT)
    widgets.pack(side=LEFT, padx=10, pady=10)
    addCommand(widgets, text="确定", event=validate(_value, VAR_INT_TYPE))

    return _value


def RegisterCelsius( root ):
    _value = DoubleVar()

    widgets = Frame(root)
    label   = Label(widgets, text=CELSIUS_LABEL)
    scanf   = Entry(widgets, textvariable=_value)

    label.pack(side=LEFT)
    scanf.pack(side=LEFT)
    widgets.pack(side=LEFT, padx=10, pady=10)
    addCommand(widgets, text=COMMAND_LABEL, event=validate(_value, VAR_DOUBLE_TYPE))

    return _value


def RegisterDensity( root ):
    _value = DoubleVar()

    widgets = Frame(root)
    label   = Label(widgets, text=DENSITY_LABEL)
    scanf   = Entry(widgets, textvariable=_value)

    label.pack(side=LEFT)
    scanf.pack(side=LEFT)
    widgets.pack(side=LEFT, padx=10, pady=10)
    addCommand(widgets, text=COMMAND_LABEL, event=validate(_value, VAR_STR_TYPE))

    return _value


def RegisterVolume( root ):
    _value = DoubleVar()

    widgets = Frame(root)
    label   = Label(widgets, text=VOLUME_LABEL)
    scanf   = Entry(widgets, textvariable=_value)

    label.pack(side=LEFT)
    scanf.pack(side=LEFT)
    widgets.pack(side=LEFT, padx=10, pady=10)
    addCommand(widgets, text="确定", event=validate(_value, VAR_DOUBLE_TYPE))

    return _value


def RegisterGravity( root ):
    _value = DoubleVar()

    widgets = Frame(root)
    label   = Label(widgets, text=GRAVITY_LABEL)
    scanf   = Entry(widgets, textvariable=_value)

    label.pack(side=LEFT)
    scanf.pack(side=LEFT)
    widgets.pack(side=LEFT, padx=10, pady=10)
    addCommand(widgets, text="确定", event=validate(_value, VAR_DOUBLE_TYPE))

    return _value


def RegisterArea( root ):
    _value = DoubleVar()

    widgets = Frame(root)
    label   = Label(widgets, text=AREA_LABEL)
    scanf   = Entry(widgets, textvariable=_value)

    label.pack(side=LEFT)
    scanf.pack(side=LEFT)
    widgets.pack(side=LEFT, padx=10, pady=10)
    addCommand(widgets, text="确定", event=validate(_value, VAR_DOUBLE_TYPE))

    return _value