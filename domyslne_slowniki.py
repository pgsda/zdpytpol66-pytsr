def funkcja(a=(), b=None):
    a = list(a)

    if b is None:
        b = {}

    a.append('1')
    b['licznik'] += 1
    print(a, b)


funkcja()
funkcja()
