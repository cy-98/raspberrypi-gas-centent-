from tkinter import *
from _thread import start_new_thread
from window import Window
from sidebar import LoadSidebar
from navigator import LoadNavigator




window, size = Window()

sidebar   = LoadSidebar(window, size)
navigator = LoadNavigator(window, size)


window.mainloop()
