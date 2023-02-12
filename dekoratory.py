from datetime import datetime


def podaj_godzine(func):
    def wrapper(*args, **kwargs):
        print('GODZINA!')
        return func(*args, **kwargs)
    return wrapper


def podaj_godzine_przed_lub_po(przed_czy_po):       # 'przed', 'po'
    def dec(func):
        def wrapper(*args, **kwargs):
            if przed_czy_po == 'przed':
                print('GODZINA PRZED!')
            to_return = func(*args, **kwargs)
            if przed_czy_po == 'po':
                print('GODZINA PO!')
            return to_return
        return wrapper
    return dec


@podaj_godzine
def dzien_dobry():
    print('Dzień dobry!')


@podaj_godzine_przed_lub_po('po')
def dobry_wieczor():
    print('Dobry wieczór')


@podaj_godzine
def witam(kogo):
    print(f'Witam {kogo}')


witam(kogo='Piotra')
witam('Piotra')
dzien_dobry()
dobry_wieczor()
dzien_dobry()
dobry_wieczor()
