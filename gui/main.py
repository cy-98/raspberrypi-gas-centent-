from tkinter import *
from _thread import start_new_thread
from window import Window
from sidebar import LoadSidebar
from navigator import LoadNavigator
from canvas import LoadCanvas
from hooks.useThread import useThread
from hooks.useStore import useStore
import time


window, size = Window()

sidebar   = LoadSidebar(window, size)
navigator = LoadNavigator(window, size)
canvas, charts = LoadCanvas(window, size)

def updateCharts(exitHandler):
    store, setStore = useStore()
    
    xdata = store['xdata']
    ydata = store['ydata']
    
    xdata.append(1)
    ydata.append(1)
    
    charts.bar(xdata, ydata)
    canvas.draw()
    if (len(ydata) > 10):
        exitHandler()
    
useThread(updateCharts)

window.mainloop()
