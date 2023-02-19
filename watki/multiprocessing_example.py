from multiprocessing import Process, Array
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


def run_integral_using_multiprocessing():
    NOT = 4

    delta = 2.5
    a = 0
    my_processes = []
    results = Array('d', [0 for i in range(NOT)])

    for i in range(NOT):
        my_processes.append(Process(target=count_area_p,
                                 args=(a, a + delta, f_liniowa, results, i)))
        a += delta

    for t in my_processes:
        t.start()

    for t in my_processes:
        t.join()

    # print(sum(results))


if __name__ == '__main__':
    # run_integral_using_multiprocessing()

    setup = 'from __main__ import f_liniowa, count_area_p, run_integral_using_multiprocessing'
    code = 'run_integral_using_multiprocessing()'

    NOI = 10

    print(timeit(stmt=code, setup=setup, number=NOI))
