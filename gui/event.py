from random import setstate
from err import ErrorNetwork
from gui.calculate import calculate
import json
import requests as r
from gui.hooks.useThread import useThread
from gui.hooks.useStore import useStore
from gui.hooks.useRender import useRender
from time import sleep
from util import last
from gui.const import *


baseUrl = 'http://localhost:3000'
pressureRoute = '/pressure'
ratioRoute = '/ratio'
clearRoute = '/clear'


save = None

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


def startFetch(type):
    global stop
    global save

    f = None
    store, setStore = useStore()
    if type is FETCH_P:
        f = bindFetch(pressureRoute)
    if type is FETCH_V:
        f = bindFetch(ratioRoute)

    def start():
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

    return start
