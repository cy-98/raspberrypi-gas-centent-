from random import expovariate, randint, setstate
from tkinter.constants import FALSE, TRUE
from types import resolve_bases
from err import ErrorNetwork
from gui.calculate import calculate
from gui.hooks.useStore import useStore
from gui.hooks.useRender import useRender
from gui.const import *
from requests_toolbelt.multipart.encoder import MultipartEncoder
import requests as r
import json
import random


baseUrl = 'http://localhost:3000'
pressureRoute = '/pressure'
ratioRoute = '/ratio'
clearRoute = '/clear'
uploadRoute = '/upload'


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
        callback('计算结果： {}'.format(str(result)))
    return start
# endregion


def save():
    store.pop('xdata')
    store.pop('ydata')

    file = open('data', 'w+', encoding='utf-8')

    writeString = json.dumps(store, ensure_ascii=False, separators=(',', ':'))
    file.write(writeString)
    file.close()

    setStore('xdata', [])
    setStore('ydata', [])


def clearUI(cb):
    def _clear():
        setStore('xdata', [])
        setStore('ydata', [])
        useRender()
        cb(WAITING)
    return _clear


def upload():
    filename = store['date'] + '+' + str(random.randint(1, 1000))
    headers = {}
    encoder = MultipartEncoder(
        fields={
            'file': (filename, open('data', 'rb'), 'text')
        },
        boundary='---------------------' + str(random.randint(1e28, 1e29 - 1))
    )
    headers['Content-Type'] = encoder.content_type
    response = r.post(baseUrl + uploadRoute, data=encoder, headers=headers)

    if response.status_code is not 200:
        ErrorNetwork(baseUrl)
    else:
        print('uploaded')
