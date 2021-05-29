from tkinter import *

from matplotlib import artist
from gui.validate import *
from gui.command import addCommand
from gui.hooks.useStore import useStore
from gui.const import (
    CELSIUS_LABEL,
    DENSITY_LABEL,
    VOLUME_LABEL,
    ATMOSPHERIC_LABEL,
    GRAVITY_LABEL,
    AREA_LABEL,
    OPERATOR_LABEL
)


ENSURE_LABEL = '确定'
store, _ = useStore()


def setParam(key, value, dataType):
    # validate the param is useful
    # store it's key and value in global
    rule = validate(value, dataType)

    def _set():
        store, setStore = useStore()
        if rule() is True:
            setStore(key, value.get())
    return _set


def addWidgets(root, label, value):
    # load UI: label input
    # label: string  -> parma name
    # value: value  -> param value ref

    widgets = Frame(root, bg='#fff')
    label = Label(widgets, text=label, bg='#fff')
    scanf = Entry(widgets, textvariable=value)

    label.pack(side=LEFT)
    scanf.pack(side=LEFT)
    widgets.pack(side=LEFT, padx=10, pady=10)
    return widgets


def RegisterCelsius(root):
    _value = DoubleVar(value=store[CELSIUS_LABEL])
    widgets = addWidgets(root, CELSIUS_LABEL, _value)

    event = setParam(CELSIUS_LABEL, _value, VAR_DOUBLE_TYPE)

    addCommand(widgets, text=ENSURE_LABEL, event=event)
    return _value


def RegisterDensity(root):
    _value = DoubleVar(value=store[DENSITY_LABEL])
    widgets = addWidgets(root, DENSITY_LABEL, _value)

    event = setParam(DENSITY_LABEL, _value, VAR_STR_TYPE)

    addCommand(widgets, text=ENSURE_LABEL, event=event)

    return _value


def RegisterVolume(root):
    _value = DoubleVar()
    widgets = addWidgets(root, VOLUME_LABEL, _value)

    event = setParam(VOLUME_LABEL, _value, VAR_DOUBLE_TYPE)

    addCommand(widgets, text=ENSURE_LABEL, event=event)
    return _value


def RegisterGravity(root):
    _value = DoubleVar(value=store[GRAVITY_LABEL])
    widgets = addWidgets(root, GRAVITY_LABEL, _value)

    event = setParam(GRAVITY_LABEL, _value, VAR_DOUBLE_TYPE)

    addCommand(widgets, text=ENSURE_LABEL, event=event)
    return _value


def RegisterArea(root):
    _value = DoubleVar(value=store[AREA_LABEL])
    widgets = addWidgets(root, AREA_LABEL, _value)

    event = setParam(AREA_LABEL, _value, VAR_DOUBLE_TYPE)

    addCommand(widgets, text=ENSURE_LABEL, event=event)
    return _value


def RegisterOperator(root):
    _value = DoubleVar()
    widgets = addWidgets(root, OPERATOR_LABEL, _value)

    event = setParam(OPERATOR_LABEL, _value, VAR_STR_TYPE)

    addCommand(widgets, text=ENSURE_LABEL, event=event)
    return _value


def RegisterAtmospheric(root):
    _value = DoubleVar(value=store[ATMOSPHERIC_LABEL])
    widgts = addWidgets(root, ATMOSPHERIC_LABEL, _value)

    event = setParam(ATMOSPHERIC_LABEL, _value, DoubleVar)

    addCommand(widgts, text=ENSURE_LABEL, event=event)
    return _value
