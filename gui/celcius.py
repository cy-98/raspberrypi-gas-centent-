from tkinter import *




def validate(v):
    def mustbeFloat():
        try:
            # validate
            v.get()
        except TclError:
            # msg box
            print('input error')

    return mustbeFloat


def RegisterCelcius(root):
    _value = DoubleVar()
    
    widgets = Frame(root)
    label   = Label(widgets, text="celcius")
    scanf   = Entry(widgets, textvariable=_value)
    commit  = Button(widgets, text="ensure", command=validate(_value))
    
    label.pack(side=LEFT)
    scanf.pack(side=LEFT)
    commit.pack(side=LEFT)
    widgets.pack(side=LEFT, padx=10, pady=10)

    return _value