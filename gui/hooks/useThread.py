from _thread import start_new_thread


threads = []
id = 0


def threadDecorator(fn, id, exitHandler):
    while True:
        if threads[id] == False:
            break
        fn(exitHandler)


def exitThread(id):
    def handler(callback=None):
        threads[id] = False
        if callback:
            callback()

    return handler


def useThread(fn):
    # example:
    #   exitHandler = useThread(fn)
    #   do something...
    #   exit()

    # not use while True in fn
    # just pass once step function body
    global id

    threads.append(True)
    exitHandler = exitThread(id)
    start_new_thread(threadDecorator, (fn, id, exitHandler))

    id = id + 1

    return exitHandler
