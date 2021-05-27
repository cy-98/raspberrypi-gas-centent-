from tkinter import *


def Window():
    window = Tk()

    maxWidth, maxHeight = window.maxsize()
    width = min(1200, maxWidth)
    height = min(800, maxHeight)

    window['bg'] = '#fff'
    window.geometry("%dx%d" % (width, height))
    window.title('main')

    size = {
        'width': width,
        'height': height
    }

    return (window, size)
