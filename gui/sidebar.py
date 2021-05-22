from tkinter import *
import command

def LoadSidebar( window, size ):
    instance = Frame(window, bg="#f88")
    instance.pack(fill=Y, side=LEFT)
    command.addCommand(instance, '根据压力计算', None)
    command.addCommand(instance, '根据流速计算', None)
    command.addCommand(instance, '保存', None)
    command.addCommand(instance, '退出', None)
    return instance