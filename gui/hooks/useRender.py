from gui.hooks.useStore import useStore
from util import last


canvas = None
charts = None


def useRender(initcanvas=canvas, initcharts=charts):
    # useRender can update charts's UI
    # every module can use at some moments
    # it runs on another thread
    global canvas
    global charts

    store, _ = useStore()

    if initcanvas and initcharts:
        canvas = initcanvas
        charts = initcharts

    xdata = store['xdata']
    ydata = store['ydata']

    charts.clear()
    # charts.set_ylim(200)
    charts.plot(xdata, ydata)
    canvas.draw()
