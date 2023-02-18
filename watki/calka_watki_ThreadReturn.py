from timeit import timeit
from threading import Thread


def f_liniowa(x):
    return x


def count_area(a, b, f):
    delta = 0.001
    area = 0
    while a < b:
        a += delta
        area += delta * f(a)
    return area


class ThreadReturn(Thread):
    def __init__(self, target, args=()):
        self.target = target
        self.args = args
        self.kwargs = {}
        super().__init__()

    def run(self):
        self.result = self.target(*self.args, **self.kwargs)

    def join(self):
        super().join()
        return self.result


def run_integral_using_threads():
    NOT = 4

    delta = 2.5
    a = 0
    my_threads = []

    for i in range(NOT):
        # print(f'Uruchamiam wątek {i} z przedziałem {a}, {a + delta}')
        my_threads.append(ThreadReturn(target=count_area, args=(a, a + delta, f_liniowa)))
        a += delta

    for t in my_threads:
        t.start()

    s = 0

    for t in my_threads:
        w = t.join()
        # print(w)
        s += w

    # print(s)


setup = 'from __main__ import f_liniowa, count_area, ThreadReturn, run_integral_using_threads'
code = 'run_integral_using_threads()'

NOI = 1000

print(timeit(stmt=code, setup=setup, number=NOI))
