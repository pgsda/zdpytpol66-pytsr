from abc import ABC, abstractmethod

MIN_LICZBA_DRZWI = 2
MAX_LICZBA_DRZWI = 5
MAX_LICZBA_CYLINDROW = 5


class Samochod(ABC):
    def __init__(self, liczba_drzwi, moc_silnika):
        self.liczba_drzwi = liczba_drzwi
        self.moc_silnika = moc_silnika

    @abstractmethod
    def jedz(self):
        pass

    @classmethod
    def produkuj_samochod(cls, specyfikacja):
        ld, ms = specyfikacja.split()
        return cls(ld, ms)


class BMW(Samochod):
    def jedz(self):
        print('jedzie BMW')


class Toyota(Samochod):
    def jedz(self):
        print('jedzie Toyota')

    @staticmethod
    def czy_mozliwa_liczba_drzwi(liczba):
        return MIN_LICZBA_DRZWI <= liczba <= MAX_LICZBA_DRZWI


print(Toyota.czy_mozliwa_liczba_drzwi(50))

t1 = Toyota(5, 150)
t1.jedz()

t2 = Toyota.produkuj_samochod("2 390")
print(type(t2))
t2.jedz()

b = BMW.produkuj_samochod("4 180")
print(type(b))
b.jedz()
