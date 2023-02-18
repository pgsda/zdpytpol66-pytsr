from fake_db import FakeDB


class dbManager():
    def __init__(self, address, user, password):
        self.db = FakeDB(address, user, password)

    def __enter__(self):
        return self.db.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.db.disconnect()


if __name__ == '__main__':
    with dbManager('address', 'user', 'password') as f:
        f.add_to_db('dzień dobry')
        f.add_to_db('cześć')
        print(f.read_from_db(0))
        print(f.read_from_db(1))
        f.remove_from_db(1)
        print(f.read_from_db(1))

