from contextlib import contextmanager


@contextmanager
def db_manager(address, user, password):
    print('Nawiązywanie połączenia...')
    connection = {'connected': True}  # obiekt połączenia
                                      # udajemy, że dostaliśmy go z biblioteki obsługującej bazę
    print('Połączenie nawiązane!')
    yield connection
    connection['connected'] = False   # udajemy, że zamykamy połączenie,
                                      # standardowo, wywołujemy zamknięcie poł. np. z biblioteki
    print("Połączenie zakończone!")


with db_manager('mysql://localhost:3200', 'piotr', 'sda123') as dbc:
    print(dbc)
    print('Skończyłem działać')

print('Za blokiem with')