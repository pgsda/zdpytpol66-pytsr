from threading import Thread
from multiprocessing import Process
from timeit import timeit


def testowo(a, b):
    s = 0
    for i in range(a, b):
        s += i


def w_threading(no_of_t):
    th = []
    a = 0
    b = 5_000_000_00
    delta = int(b / no_of_t)
    for _ in range(no_of_t):
        th.append(Thread(target=testowo, args=(a, a + delta)))
        a += delta

    for t in th:
        t.start()

    for t in th:
        t.join()


def w_processes(no_of_p):
    pr = []
    a = 0
    b = 5_000_000_00
    delta = int(b / no_of_p)
    for _ in range(no_of_p):
        pr.append(Process(target=testowo, args=(a, a + delta)))
        a += delta

    for p in pr:
        p.start()

    for p in pr:
        p.join()


if __name__ == '__main__':
    setup = 'from __main__ import w_processes, w_threading, testowo'
    number = 1

    print(timeit(stmt="w_threading(6)", setup=setup, number=number))
    print(timeit(stmt="w_processes(6)", setup=setup, number=number))
