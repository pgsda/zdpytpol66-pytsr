def zmien_saldo(saldo_poczatkowe, kwota, max_zadl):
    sk = saldo_poczatkowe + kwota
    if sk < -max_zadl:
        raise ValueError(f'Kwota {sk} przekracza maksymalne zadłużenie {max_zadl}')
    return sk


try:
    saldo_po_operacji = zmien_saldo(100, -150, 50)
    print(saldo_po_operacji)
except ValueError:
    print('Nie masz środków')
