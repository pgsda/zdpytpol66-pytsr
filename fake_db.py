from time import sleep

class FakeDB:
    def __init__(self, address, user, password):
        self.address = address
        self.user = user
        self.password = password
        self.connection = {'socket': None, 'connection': False}
        self.db = []

    def connect(self):
        sleep(1)
        self.connection = {'socket': lambda: True, 'connection': True}
        return self

    def disconnect(self):
        sleep(1)
        self.connection = {'socket': None, 'connection': False}
        return self

    def add_to_db(self, s):
        if self.connection['connection']:
            self.db.append(s)
            return True
        return False

    def read_from_db(self, i):
        if self.connection['connection'] and 0 <= i < len(self.db):
            return self.db[i]
        return None

    def remove_from_db(self, i):
        if self.connection['connection'] and 0 <= i < len(self.db):
            del self.db[i]
            return True
        return False
