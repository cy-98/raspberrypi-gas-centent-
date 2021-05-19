store = {
    'xdata': [1, 2],
    'ydata': [1, 2],
}


def setStore( key, value ) -> store:
    store[key] = value
    return store


def useStore() -> setStore:
    
    return store, setStore
