from random import randint


class RandomNumbers():
    def __init__(self, how_many, min=0, max=1000):
        self.how_many = how_many
        self.min = min
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.how_many <= 0:
            raise StopIteration
        self.how_many -= 1
        return randint(self.min, self.max)


def random_numbers(how_many, min=0, max=1000):
    while how_many > 0:
        yield randint(min, max)
        how_many -= 1


for some_random in RandomNumbers(3):
    print(some_random)

for some_random in RandomNumbers(2, 20, 50):
    print(some_random)

for some_random in random_numbers(10, 0, 10):
    print(some_random)
