items = [(3, 8), (95, 237), (98, 95), (95, 11)]

str_items = ['piotr', 'Bartek', 'Rafal', 'Alicja']

print(sorted(items))
print(sorted(items, key=lambda x: x[0] + x[1]))

print(sorted(str_items))
print(sorted(str_items, key=lambda x: x.lower()))
