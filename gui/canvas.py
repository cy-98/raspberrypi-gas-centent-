from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
from hooks.useThread import useThread


# TODO: SAVE charts

# TODO: RENDER charts

# TODO: UPDATE charts

LINE_COLOR = '#000'

xdata = [1,2]
ydata = [4,3]

# TODO: fix scope problem
canvas = None
charts = None

def generateCanvas(root, width, height):
    dpi = 60
    figure = Figure(figsize=(width/dpi, height/dpi), dpi=dpi) # blank panel
    
    charts = figure.add_subplot(1, 1, 1)
    canvas = FigureCanvasTkAgg(figure, root)
 
    return canvas, charts


def renderCharts():
    charts.bar(xdata, ydata)
    canvas.draw()
    return


def updateCharts():
    xdata.append(1)
    ydata.append(1)
    charts.bar(xdata, ydata)
    canvas.draw()


def LoadCanvas(root, size):
    width = size['width'] * 3 / 4
    height = size['height'] / 2

    generateCanvas(root, width, height)
    renderCharts()
    useThread(updateCharts)
    canvas.get_tk_widget().pack()

    return canvas, charts

