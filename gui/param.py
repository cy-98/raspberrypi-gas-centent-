from tkinter import *



def validate(v):
    def mustbeInt():
        try:
            # validate
            v.get()
        except TclError:
            # msg box
            print('inputError')
    return mustbeInt


def RegisterWidgets(root):
    _value = IntVar()
    
    widgets = Frame(root)
    label   = Label(widgets, text="other params")
    scanf   = Entry(widgets, textvariable=_value)
    commit  = Button(widgets, text="ensure", command=validate(_value))
    
    label.pack(side=LEFT)
    scanf.pack(side=LEFT)
    commit.pack(side=LEFT)
    widgets.pack(side=LEFT, padx=10, pady=10)

    return _value