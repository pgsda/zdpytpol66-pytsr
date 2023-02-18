from threading import Thread
from timeit import timeit


def f_liniowa(x):
    return x


def count_area_p(a, b, f, rl, tn):
    delta = 0.001
    area = 0
    while a < b:
        a += delta
        area += delta * f(a)
    rl[tn] = area


def run_integral_using_threads():
    NOT = 4

    delta = 2.5
    a = 0
    my_threads = []
    results = [None for i in range(NOT)]

    for i in range(NOT):
        my_threads.append(Thread(target=count_area_p,
                                 args=(a, a + delta, f_liniowa, results, i)))
        a += delta

    for t in my_threads:
        t.start()

    for t in my_threads:
        t.join()

    # print(sum(results))


setup = 'from __main__ import f_liniowa, count_area_p, run_integral_using_threads'
code = 'run_integral_using_threads()'

NOI = 1000

print(timeit(stmt=code, setup=setup, number=NOI))
