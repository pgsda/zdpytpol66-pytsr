class Osoba:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek
        print('Tworzę nową osobę')

    def __str__(self):
        return f"{self.imie} ma {self.wiek} lat"


class Pracownik(Osoba):
    def __init__(self, imie, wiek, stawka, liczba_godzin):
        super().__init__(imie, wiek)
        self.stawka = stawka
        self.liczba_godzin = liczba_godzin

    def pokaz_finanse(self):
        return self.stawka * self.liczba_godzin


class Student(Osoba):
    def __init__(self, imie, wiek, stypendium):
        # self.imie = imie  ## TAK NIE ROBIMY!
        # self.wiek = wiek
        super().__init__(imie, wiek)
        self.stypendium = stypendium

    def pokaz_finanse(self):
        return self.stypendium


if __name__ == '__main__':
    s = Student('Piotr', 29, True)

    print(s)
