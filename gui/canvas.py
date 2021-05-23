from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from hooks.useRender import useRender

# TODO: save charts

# TODO: render charts

# TODO: update charts

LINE_COLOR = '#000'


def generateCanvas(root, width, height):
    dpi = 60
    figure = Figure(figsize=(width/dpi, height/dpi), dpi=dpi)  # blank panel

    charts = figure.add_subplot(1, 1, 1)
    canvas = FigureCanvasTkAgg(figure, root)

    return canvas, charts


def LoadCanvas(root, size):
    width = size['width'] * 3 / 4
    height = size['height'] / 2

    canvas, charts = generateCanvas(root, width, height)
    useRender(canvas, charts)
    canvas.get_tk_widget().pack()

    return canvas, charts
