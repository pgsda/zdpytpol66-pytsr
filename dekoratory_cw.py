from time import sleep, time


def pomiar_czasu(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        to_return = func(*args, **kwargs)
        t2 = time()
        print(f'Funkcja trwała: {t2 - t1}')
        return to_return
    return wrapper


@pomiar_czasu
def trwam_dwie_sekundy():
    sleep(2)


@pomiar_czasu
def trwam_tyle_ile_chcesz(ile):
    sleep(ile)
    return ile


trwam_dwie_sekundy()
trwalem = trwam_tyle_ile_chcesz(1)
print(f'Proste dodawanie: {trwalem + 10}')
