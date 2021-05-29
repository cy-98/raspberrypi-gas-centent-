from gui.addLabel import addLabel
from gui.const import FETCH_P, WAITING
from tkinter import *
from gui.hooks.useRender import useRender
from gui.hooks.useStore import setStore, useStore
from gui.window import Window
from gui.sidebar import LoadSidebar
from gui.navigator import LoadNavigator
from gui.canvas import LoadCanvas
from gui.command import addCommand
from gui.event import clearUI, startFetch, save, upload
from gui.const import FETCH_P, FETCH_V


COMPUTE_LABEL_P = '根据压力计算'
COMPUTE_LABEL_V = '根据流速计算'
CLEAR_LABEL = '清空'
SAVE_LABEL = '保存'
UPLOAD_LABEL = '上传'


def bindStatus(status):
    def update(r):
        status.set(r)
    return update


def main():
    window, size = Window()
    sidebar = LoadSidebar(window)
    navigator = LoadNavigator(window, size)
    canvas, charts = LoadCanvas(window, size)

    status = StringVar(value=WAITING)  # 程序状态 1. 未开始 2. 计算中 3. 结果
    updateStatus = bindStatus(status)

    addLabel(navigator, status)
    addCommand(sidebar, COMPUTE_LABEL_P, startFetch(FETCH_P, updateStatus))
    addCommand(sidebar, COMPUTE_LABEL_V, startFetch(FETCH_V, updateStatus))
    addCommand(sidebar, CLEAR_LABEL, clearUI(updateStatus))
    addCommand(sidebar, SAVE_LABEL, save)
    addCommand(sidebar, UPLOAD_LABEL, upload)

    window.mainloop()
