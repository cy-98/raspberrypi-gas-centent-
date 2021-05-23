import json
import requests as r
from hooks.useThread import useThread
from hooks.useStore import useStore
from hooks.useRender import useRender
from time import sleep

# region
FETCH_P = 0
FETCH_V = 1


baseUrl = 'http://localhost:3000'
pressureRoute = '/pressure'
ratioRoute = '/ratio'
clearRoute = '/clear'

# endregion

# region
stop = None
save = None


def bindFetch(route):
    def handler():
        res = r.get(baseUrl + route)
        if res:
            return json.loads(res.content.decode(encoding='utf8'))
        else:
            return None
    return handler
# endregion

# region


def last(arr, index=1):
    return arr[len(arr) - index]

# endregion


def startFetch(type):
    global stop
    global save

    f = None
    store, setStore = useStore()
    setStore('type', type)
    if type is FETCH_P:
        f = bindFetch(pressureRoute)
    if type is FETCH_V:
        f = bindFetch(ratioRoute)

    # start new thread to fetch data

    def start():
        while(True):
            content = f()
            xdata = content['xdata']
            ydata = content['ydata']

            setStore('xdata', xdata)
            setStore('ydata', ydata)

            if len(xdata) % 2:
                useRender()
            # if k < 0.001:   # 计算斜率
            #     break
            if len(xdata) > 500:
                break
        useRender()

    return start
