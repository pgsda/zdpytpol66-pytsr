class IncorrectDebt(Exception):
    pass


def zmien_saldo(saldo_poczatkowe, kwota, max_zadl):
    sk = saldo_poczatkowe + kwota
    if sk < -max_zadl:
        raise IncorrectDebt(f'Kwota {sk} przekracza maksymalne zadłużenie {max_zadl}')
    return sk


try:
    saldo_po_operacji = zmien_saldo(100, -200, 50)
    print(saldo_po_operacji)
except IncorrectDebt:
    print('Nie masz środków')
