from copy import deepcopy

slownik = {
    'a': {'w1': 1, 'w2': 2},
    'b': [1, 2, 3, 4],
    'c': 12,
    'd': 1876,
    'e': 'jestem stringiem'
}

# no copy
# s2 = slownik
#
# s2['a']['w1'] = 111
# s2['b'][0] = 111
# s2['c'] = 89
# s2['f'] = 222
#
# print(slownik)
# print(s2)

# copy
# s3 = slownik.copy()
#
# s3['a']['w1'] = 111
# s3['b'][0] = 0
# s3['c'] = 77
# s3['e'] = "siemanko"
#
# print(slownik)
# print(s3)

# deepcopy
s4 = deepcopy(slownik)
s4['a']['w1'] = 111
s4['b'][0] = 0
s4['c'] = 77
s4['e'] = "siemanko"

print(slownik)
print(s4)
