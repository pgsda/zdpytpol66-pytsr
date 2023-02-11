from datetime import datetime


def podaj_godzine(func):
    print('dupa0')
    def wrapper():
        print('dupa1')
        func()
        print('dupa2')
    return wrapper


@podaj_godzine
def dzien_dobry():
    print('Dzień dobry!')


@podaj_godzine
def dobry_wieczor():
    print('Dobry wieczór')


dzien_dobry()
dobry_wieczor()
dzien_dobry()
dobry_wieczor()
