from abc import ABC, abstractmethod
from math import pi


class Figura(ABC):
    def __init__(self, kolor):
        self.kolor = kolor

    @abstractmethod
    def pole(self):
        pass

    @abstractmethod
    def obw(self):
        pass


class Kwadrat(Figura):
    def __init__(self, bok, kolor):
        super().__init__(kolor)
        self.bok = bok

    def pole(self):
        return self.bok * self.bok

    def obw(self):
        return self.bok * 4


class Prostokat(Figura):
    def __init__(self, a, b, kolor):
        super().__init__(kolor)
        self.a = a
        self.b = b

    def pole(self):
        return self.a * self.b

    def obw(self):
        return self.a * 2 + self.b * 2


class Kolo(Figura):
    def __init__(self, r, kolor):
        super().__init__(kolor)
        self.r = r

    def pole(self):
        return pi * self.r * self.r

    def obw(self):
        return 2 * pi * self.r


kw = Kwadrat(10, 'niebieski')
print(kw.pole(), kw.obw(), kw.kolor)

pr = Prostokat(5, 6, 'czerwony')
print(pr.pole(), pr.obw(), pr.kolor)

ko = Kolo(8, 'zielony')
print(ko.pole(), ko.obw(), ko.kolor)
