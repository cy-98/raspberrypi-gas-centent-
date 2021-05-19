from tkinter import *
from window import Window
from sidebar import LoadSidebar
from navigator import LoadNavigator
from canvas import LoadCanvas
from hooks.useThread import useThread
from hooks.useStore import useStore
from _thread import start_new_thread

window, size = Window()

sidebar   = LoadSidebar(window, size)
navigator = LoadNavigator(window, size)
canvas, charts, renderCharts = LoadCanvas(window, size)

def updateCharts( exitHandler ):
    # TODO:
    return None


def up( exitHandler ):
    #TODO:
    return None

# useThread(updateCharts)
# useThread(up)

window.mainloop()
