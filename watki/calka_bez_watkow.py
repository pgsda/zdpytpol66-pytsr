from threading import Thread
from timeit import timeit


def f_liniowa(x):
    return x


def count_area(a, b, f):
    delta = 0.001
    area = 0
    while a < b:
        a += delta
        area += delta * f(a)
    return area


setup = 'from __main__ import f_liniowa, count_area'
code = 'count_area(0, 10, f_liniowa)'

NOI = 1000

print(timeit(stmt=code, setup=setup, number=NOI))
