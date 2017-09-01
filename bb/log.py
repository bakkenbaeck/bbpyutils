from __future__ import print_function

import logging

from time import time

from functools import wraps

log = logging.getLogger(__name__)

class timer(object):

    """
    A multi-use timer class, use as context-manager, decorator, or iterator-wrapper

    (although tqdm is better for the last use)

    with timer('name'):
       ... do something slow ...

    @timer('name')
    def f():
       ... do something slow ...

    for x in timer('name', ... some iterable ...):
       ... do something ...

    """

    def __init__(self, name, itr=None):
        self.name = name
        self.itr = itr

    def __iter__(self):
        if self.itr is None: raise Exception("You can't iterate over a timer where no iterable was passed!")

        self.__enter__()

        for x in self.itr: yield x

        self.__exit__()

    def __enter__(self):
        self.t0 = time()

    def __exit__(self, type=None, value=None, traceback=None):
        log.info("%s took %.2fs"%(self.name, time()-self.t0))

    def __call__(self, f):

        @wraps(f)
        def _f(*args, **kwargs):
            self.__enter__()

            r = f(*args, **kwargs)

            self.__exit__()

            return r

        return _f


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    from time import sleep
    with timer('contextmanager test'):
        sleep(1)

    @timer('decorator test')
    def f():
        sleep(1)

    f()

    for x in timer('list test', range(3)):
        sleep(0.3)
