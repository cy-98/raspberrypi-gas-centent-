from random import randint
import numpy as np


store = {
    'xdata': [i for i in range(100)],
    'ydata': [i - randint(0, i) for i in range(100)],
}


def setStore( key, value ) -> store:
    store[key] = value
    return store


def useStore() -> setStore:

    return store, setStore
