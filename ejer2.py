import csv
with open('pokemon.csv', 'r') as f:
    reader = csv.reader(f)
    lista = list(reader)
    print(lista)
    print(lista[0])
    print(lista[1])
    print(lista[2])


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



# mostrar todos los datos de un Pokémon a partir de su número y nombre –para este último, la búsqueda debe ser por proximidad, es decir si busco “bul” se deben mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos caracteres
def buscar_pokemon():
    pokemon = input("Ingrese el nombre del pokemon que desea buscar: ")
    for i in range(len(lista)):
        if pokemon in lista[i][1]:
            print(lista[i])
buscar_pokemon()


