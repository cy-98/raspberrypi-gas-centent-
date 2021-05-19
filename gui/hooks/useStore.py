store = {
    'xdata': [],
    'ydata': []
}


def setStore(key, value) -> store:
    store[key] = value
    return store


def useStore() -> setStore:
    
    return store, setStore
