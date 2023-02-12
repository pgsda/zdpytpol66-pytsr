import re

tekst_do_wyszukania = input('Podaj fraze do znalezienia: ')

with open('lorem_ipsum.txt', 'r') as f:
    tekst_pliku = f.read()

    znalezione = re.finditer(tekst_do_wyszukania, tekst_pliku)

    for z in znalezione:
        print(f'Znaleziono od znaku: {z.span()[0]} do znaku: {z.span()[1]}')
