def a():
    print('jestem serem')

def b():
    print('jestem masłem')

def c():
    print('jestem chlebem baltonowskim')


if __name__ == '__main__':
    for funkcja in [a, b, c]:
        funkcja()
