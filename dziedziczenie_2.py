class A:
    def metoda(self):
        print('A')

class B:
    def metoda(self):
        print('B')

class C(A, B):
    def __init__(self):
        A.metoda(self)
        B.metoda(self)

c = C()

c.metoda()
