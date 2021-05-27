from gui.hooks.useStore import useStore
from tkinter import *
from err import ErrorInputTypes

VAR_STR_TYPE = 'str'
VAR_INT_TYPE = 'int'
VAR_DOUBLE_TYPE = 'double'


def validate(v, type):
    def mustInt():
        try:
            # validate
            v.get()
        except TclError:
            # msg box
            ErrorInputTypes(VAR_INT_TYPE)
        return True

    if type is VAR_INT_TYPE:
        return mustInt

    def mustFloat():
        try:
            # validate
            v.get()
        except TclError:
            # msg box
            ErrorInputTypes(VAR_DOUBLE_TYPE)
        return True

    if type is VAR_DOUBLE_TYPE:
        return mustFloat

    def mustStr():
        try:
            v.get()
        except TclError:
            ErrorInputTypes(VAR_STR_TYPE)
        return True

    if type is VAR_STR_TYPE:
        return mustStr
