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


for some_random in RandomNumbers(5):
    print(some_random)

for some_random in RandomNumbers(10, 20, 50):
    print(some_random)
