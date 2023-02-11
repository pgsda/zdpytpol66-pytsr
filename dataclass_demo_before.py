class Toyota():
    def __init__(self, liczba_drzwi, moc_silnika):
        self.liczba_drzwi = liczba_drzwi
        self.moc_silnika = moc_silnika

    def jedz(self):
        print('jedzie Toyota')

    def __repr__(self):
        return f'Liczba drzwi: {self.liczba_drzwi}, Moc silnika: {self.moc_silnika}'


t = Toyota(5, 150)
t.jedz()
print(t)
