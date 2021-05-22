from tkinter import *
from validate import *
from command import addCommand
from hooks.useStore import useStore



COMMAND_LABEL = '确定'
CELSIUS_LABEL = '摄氏度'
DENSITY_LABEL = '密度'
VOLUME_LABEL = '体积'
GRAVITY_LABEL = '重力加速度'
AREA_LABEL = '管道横截面积'
OPERATOR_LABEL = '操作人员'
DATE_LABEL = '日期'


def setParam(key, value, dataType):
    rule = validate(value, dataType)
    def _set():
        store, setStore = useStore()
        if rule() is True:
            setStore(key, value.get())
    return _set


def addWidgets( root, label, value):
    widgets = Frame(root, bg='#fff')
    label   = Label(widgets, text=label, bg='#fff')
    scanf   = Entry(widgets, textvariable=value)

    label.pack(side=LEFT)
    scanf.pack(side=LEFT)
    widgets.pack(side=LEFT, padx=10, pady=10)
    return widgets



def RegisterCelsius( root ):
    _value = DoubleVar()
    widgets = addWidgets(root, CELSIUS_LABEL, _value)
    addCommand(widgets, text=COMMAND_LABEL, event=setParam(CELSIUS_LABEL, _value, VAR_DOUBLE_TYPE))
    return _value


def RegisterDensity( root ):
    _value = DoubleVar()
    widgets = addWidgets(root, DENSITY_LABEL, _value)
    addCommand(widgets, text=COMMAND_LABEL, event=setParam(DENSITY_LABEL, _value, VAR_STR_TYPE))

    return _value


def RegisterVolume( root ):
    _value = DoubleVar()
    widgets = addWidgets(root, VOLUME_LABEL, _value)
    addCommand(widgets, text="确定", event=setParam(VOLUME_LABEL, _value, VAR_DOUBLE_TYPE))
    return _value


def RegisterGravity( root ):
    _value = DoubleVar()
    widgets = addWidgets(root, GRAVITY_LABEL, _value)
    addCommand(widgets, text="确定", event=setParam(GRAVITY_LABEL, _value, VAR_DOUBLE_TYPE))
    return _value


def RegisterArea( root ):
    _value = DoubleVar()
    widgets = addWidgets(root, AREA_LABEL, _value)
    addCommand(widgets, text="确定", event=setParam(AREA_LABEL, _value, VAR_DOUBLE_TYPE))
    return _value


def RegisterOperator( root ):
    _value = DoubleVar()
    widgets = addWidgets(root, OPERATOR_LABEL, _value)
    addCommand(widgets, text="确定", event=setParam(OPERATOR_LABEL, _value, VAR_STR_TYPE))
    return _value
