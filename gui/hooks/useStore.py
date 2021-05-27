from gui.const import *
from random import randint

# global data store
# every module can use useStore to get (store. setStore)
store = {
    'xdata': [],
    'ydata': [],
    CELSIUS_LABEL: 25.0,
    VOLUME_LABEL: 0.0,
    DENSITY_LABEL: DEFAULT_DENSITY,
    GRAVITY_LABEL: 9.8,
    AREA_LABEL: 1,
    ATMOSPHERIC_LABEL: DEFAULT_ATOMSPHERIC,
    OPERATOR_LABEL: 'Fake'
}


def setStore(key, value) -> store:
    store[key] = value
    return store


def useStore():
    return store, setStore
