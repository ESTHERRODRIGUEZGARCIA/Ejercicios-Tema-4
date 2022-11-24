import csv
with open('pokemon.csv', 'r') as f:
    reader = csv.reader(f)
    lista = list(reader)

nombres = []
for i in range(len(lista)):
    nombres.append(lista[i][0])

print("\n\n##### NOMBRES #####\n\n")
print(nombres)


numeros = []
for i in range(len(lista)):
    numeros.append(lista[i][1])
print("\n\n##### NUM #####\n\n")
print(numeros)

tipo = []
for i in range(1, len(lista)):
    tipo.append(lista[i][2])

print("\n\n##### TIPOS #####\n\n")
print(tipo)
