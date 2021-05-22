from tkinter import *




VAR_STR_TYPE = 'str'
VAR_INT_TYPE = 'int'
VAR_DOUBLE_TYPE = 'double'


def ErrorDuringInput(s):
    print('input error: please ensure your variable has {} type'.format(s))


def validate( v, type ):
    def mustInt():
        try:
            # validate
            v.get()
        except TclError:
            # msg box
            ErrorDuringInput(VAR_INT_TYPE)
        return True


    if type is VAR_INT_TYPE:
        return mustInt


    def mustFloat():
        try:
            # validate
            v.get()
        except TclError:
            # msg box
            ErrorDuringInput(VAR_DOUBLE_TYPE)
        return True


    if type is VAR_DOUBLE_TYPE:
        return mustFloat

    def mustStr():
        try:
            v.get()
        except TclError:
            ErrorDuringInput(VAR_STR_TYPE)
        return True



    if type is VAR_STR_TYPE:
        return mustStr
