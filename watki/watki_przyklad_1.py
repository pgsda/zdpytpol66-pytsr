from threading import Thread


def iterate_print(iter, kim_jestem):
    # Funkcja wypisująca elementy listy
    for item in iter:
        print(f'{kim_jestem}: {item}')


if __name__ == '__main__':
    t1 = Thread(target=iterate_print, args=(range(1000), 't1'))
    t2 = Thread(target=iterate_print, args=(range(1000), 't2'))

    t1.start()
    t2.start()

    t1.join()
    print('T1 się zakończyło')
    t2.join()
    print('T2 się zakończyło')

    print('Zrobione')
