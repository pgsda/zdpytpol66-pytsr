from abc import ABC, abstractmethod


class Samochod(ABC):
    @abstractmethod
    def jedz(self):
        pass

    @abstractmethod
    def skrec(self):
        pass


class Mercedes(Samochod):
    def jedz(self):
        print('jadę!')

    def skrec(self):
        print('skręcam!')

    @abstractmethod
    def otworz_bagaznik(self):
        pass


class MA200(Mercedes):
    def otworz_bagaznik(self):
        print('otwieram')


class BMW(Samochod):
    def jedz(self):
        print('BRUUUUUUUUM!')

    def skrec(self):
        print('ZIUUUUUUUUU!')


ma200 = MA200()
ma200.jedz()
ma200.otworz_bagaznik()

b = BMW()
b.jedz()
