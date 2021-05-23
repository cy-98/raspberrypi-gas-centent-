from hooks.useRender import useRender
from hooks.useStore import setStore
from tkinter import *
from window import Window
from sidebar import LoadSidebar
from navigator import LoadNavigator
from canvas import LoadCanvas
from command import addCommand
from fetch import FETCH_P, FETCH_V, startFetch, stop, save
from _thread import start_new_thread




COMPUTE_LABEL_P = '根据压力计算'
COMPUTE_LABEL_V = '根据流速计算'
STOP_LABEL = '停止'
SAVE_LABEL = '保存'


window, size = Window()
sidebar = LoadSidebar(window)
navigator = LoadNavigator(window, size)
canvas, charts = LoadCanvas(window, size)


addCommand(sidebar, COMPUTE_LABEL_P, startFetch(FETCH_P))
addCommand(sidebar, COMPUTE_LABEL_V, startFetch(FETCH_V))
addCommand(sidebar, STOP_LABEL, stop)
addCommand(sidebar, SAVE_LABEL, save)


window.mainloop()
