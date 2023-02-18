from threading import Thread
from functools import wraps
from concurrent.futures import Future


def threadmethod(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        def call(func, future, *args, **kwargs):
            ret = func(*args, **kwargs)
            future.set_result(ret)
        future = Future()
        Thread(target=call, args=(fn, future, *args, kwargs)).start()
        return future
    return wrapper
