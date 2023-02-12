items = [1, 2, 3, 4, 5]

# FOR
squared = []

for i in items:
    squared.append(i ** 2)

print(squared)

# MAP + ZWYKLA FUNKCJA
def podnies_do_kwadratu(x):
    return x ** 2

squared_by_map = list(map(podnies_do_kwadratu, items))

print(squared_by_map)

# MAP + LAMBDA
squared_by_map_and_lambda = list(map(lambda x: x ** 2, items))

print(squared_by_map_and_lambda)

# FILTER + LAMBDA
evens = list(filter(lambda x: x % 2 == 0, items))
print(evens)

# REDUCE + LAMBDA
from functools import reduce

sum_of_items = reduce(lambda x, y: x + y, items)

print(sum_of_items)

# REDUCE + LAMBDA, słowniki
dicts = [{"waga": 11, "ob": 13}, {"waga": 15}, {"waga": 358}, {"waga": 897}]

sum_of_w1 = reduce(lambda x, y: x + y['waga'], dicts, 0)
sum_of_w2 = reduce(lambda x, y: {'waga': x['waga'] + y['waga']}, dicts)

print(sum_of_w1, sum_of_w2)
