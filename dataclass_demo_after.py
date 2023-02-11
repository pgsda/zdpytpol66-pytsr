from dataclasses import dataclass

@dataclass
class Toyota():
    liczba_drzwi : int
    moc_silnika : int

    def jedz(self):
        print('jedzie Toyota')


t = Toyota(5, 150)
t.jedz()
print(t)
