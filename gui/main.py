from gui.const import FETCH_P
from tkinter import *
from gui.hooks.useRender import useRender
from gui.hooks.useStore import setStore
from gui.window import Window
from gui.sidebar import LoadSidebar
from gui.navigator import LoadNavigator
from gui.canvas import LoadCanvas
from gui.command import addCommand
from gui.event import startFetch, save
from gui.const import FETCH_P, FETCH_V


COMPUTE_LABEL_P = '根据压力计算'
COMPUTE_LABEL_V = '根据流速计算'
STOP_LABEL = '停止'
SAVE_LABEL = '保存'
UPLOAD_LABEL = '上传'


def main():
    window, size = Window()
    sidebar = LoadSidebar(window)
    navigator = LoadNavigator(window, size)
    canvas, charts = LoadCanvas(window, size)

    addCommand(sidebar, COMPUTE_LABEL_P, startFetch(FETCH_P))
    addCommand(sidebar, COMPUTE_LABEL_V, startFetch(FETCH_V))
    addCommand(sidebar, SAVE_LABEL, save)
    addCommand(sidebar, UPLOAD_LABEL, None)

    window.mainloop()
