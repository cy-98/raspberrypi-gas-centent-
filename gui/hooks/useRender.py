from hooks.useStore import useStore

canvas = None
charts = None


def last(arr):
    return arr[len(arr) - 1]


def useRender(initcanvas=canvas, initcharts=charts):
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
