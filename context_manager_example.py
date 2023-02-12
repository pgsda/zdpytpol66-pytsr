class DBManager():
    def __init__(self, address, user, password):
        self.address = address
        self.user = user
        self.password = password

    def __enter__(self):
        print('Nawiązywanie połączenia...')
        self.connection = {'connected': True} # obiekt połączenia
                                              # udajemy, że dostaliśmy go z biblioteki obsługującej bazę
        print('Połączenie nawiązane!')
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection['connected'] = False  # udajemy, że zamykamy połączenie,
                                              # standardowo, wywołujemy zamknięcie poł. np. z biblioteki
        print("Połączenie zakończone!")


with DBManager('mysql://localhost:3200', 'piotr', 'sda123') as dbc:
    print(dbc)
    print('Skończyłem działać')

print('Za blokiem with')