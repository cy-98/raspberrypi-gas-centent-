from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from tkinter import *




LINE_COLOR = '#000'


# clean charts

# render charts

# update charts

# analys options


def generateCanvas(root, width, height):
    canvas = Canvas(root, width=width, height=height)
    
    
    return canvas


def LoadCanvas(root, size):
    width = size['width'] * 3 / 4
    height = size['height'] / 2
    canvas = generateCanvas(root, width, height)
    
    
    canvas.pack()