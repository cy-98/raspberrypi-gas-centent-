from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
from hooks.useStore import useStore

# TODO: save charts

# TODO: render charts

# TODO: update charts

LINE_COLOR = '#000'


# TODO: fix scope problem


def generateCanvas(root, width, height):
    dpi = 60
    figure = Figure(figsize=(width/dpi, height/dpi), dpi=dpi) # blank panel
    
    charts = figure.add_subplot(1, 1, 1)
    canvas = FigureCanvasTkAgg(figure, root)
 
    return canvas, charts


def renderCharts(canvas, charts):
    store, _ = useStore()
    xdata = store['xdata']
    ydata = store['ydata']

    charts.bar(xdata, ydata)
    canvas.draw()
    return


def LoadCanvas(root, size):
    width = size['width'] * 3 / 4
    height = size['height'] / 2

    canvas, charts = generateCanvas(root, width, height)
    renderCharts(canvas, charts)
    canvas.get_tk_widget().pack()
    return canvas, charts

