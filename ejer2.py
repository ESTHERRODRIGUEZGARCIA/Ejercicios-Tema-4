import csv
with open('pokemon.csv', 'r') as f:
    reader = csv.reader(f)
    lista = list(reader)
    