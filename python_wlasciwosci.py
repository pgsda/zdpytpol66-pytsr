def f():
    def wewn():
        print('jestem wewn!')
    return wewn

w = f()
w()

##########

def g():
    print('jestem g')
    return 11

def wykonaj(co):
    print(co)

wykonaj(g)      # przekazanie referencji
wykonaj(g())    # przekazanie wartości
