from timeit import timeit


def funkcja(x):
    for _ in range(x):
        1 + 1


def funkcja2(x):
    for _ in range(x):
        pass


if __name__ == '__main__':
    setup = 'from __main__ import funkcja, funkcja2'

    code1 = 'funkcja(100_000)'
    code2 = 'funkcja2(100_000)'

    t1 = timeit(stmt=code1, setup=setup, number=1000)
    t2 = timeit(stmt=code2, setup=setup, number=1000)

    print(t1, t2, sep='\n')
