import csv

# reader
with open('dane.csv', 'r', encoding="UTF8") as f:
    reader = csv.reader(f)

    s = 0
    next(reader)
    for row in reader:
        s += float(row[-1])

    print(s)


# DictReader
with open('dane.csv', 'r', encoding="UTF8") as f:
    reader = csv.DictReader(f)

    s = 0
    for row in reader:
        s += float(row['cena całkowita'])

    print(s)


# dodaj nową sprzedaż do pliku
with open('dane.csv', 'a', encoding="UTF8") as f:
    writer = csv.writer(f)
    writer.writerow(['Banany', '3kg', 13.00, 39.00])
