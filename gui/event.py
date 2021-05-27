from random import expovariate, setstate
from tkinter.constants import FALSE, TRUE
from types import resolve_bases
from err import ErrorNetwork
from gui.calculate import calculate
from gui.hooks.useStore import useStore
from gui.hooks.useRender import useRender
from gui.const import *
import requests as r
import json


baseUrl = 'http://localhost:3000'
pressureRoute = '/pressure'
ratioRoute = '/ratio'
clearRoute = '/clear'


save = None


store, setStore = useStore()


# region


def bindFetch(route):
    def handler():
        try:
            res = r.get(baseUrl + route)
            if res:
                return json.loads(res.content.decode(encoding='utf8'))
            else:
                return None
        except:
            ErrorNetwork(baseUrl)
    return handler
# endregion

# region


def startFetch(type, callback):
    global stop
    global save

    f = None

    if type is FETCH_P:
        f = bindFetch(pressureRoute)
    if type is FETCH_V:
        f = bindFetch(ratioRoute)

    def start():
        callback(CALCULATING)
        setStore('type', type)
        while(True):
            content = f()
            xdata = content['xdata']
            ydata = content['ydata']

            setStore('xdata', xdata)
            setStore('ydata', ydata)

            if len(xdata) % 2:
                useRender()
            # TODO：
            if len(xdata) > 500:
                break
        useRender()

        # 计算数据
        result = calculate()
        setStore(MEASURE_RESULT, result)
        callback(str(result))
    return start
# endregion


def save():
    setStore('xdata', [])
    setStore('ydata', [])

    file = open('data', 'a+', encoding='utf-8')

    writeString = json.dumps(store, ensure_ascii=False,
                             indent=4, separators=(',', ':'))
    file.write(writeString + ',')


def clearUI():
    setStore('xdata', [])
    setStore('ydata', [])
    useRender()
