from tkinter import *
from window import Window
from sidebar import LoadSidebar
from navigator import LoadNavigator
from canvas import LoadCanvas
from hooks.useThread import useThread
from hooks.useStore import useStore


window, size = Window()

sidebar   = LoadSidebar(window, size)
navigator = LoadNavigator(window, size)
canvas, charts, renderCharts = LoadCanvas(window, size)

def updateCharts(exitHandler):
    store, setStore = useStore()
    xdata = store['xdata']
    ydata = store['ydata']
    
    # xdata.append(1)
    # ydata.append(1)
    # setStore('xdata', [ i*2 for i in xdata ])
    # setStore('ydata', [ i*2 for i in ydata ])

    renderCharts(canvas, charts)

    # if (len(ydata) > 10):
    #     exitHandler()
    
# useThread(updateCharts)

window.mainloop()
