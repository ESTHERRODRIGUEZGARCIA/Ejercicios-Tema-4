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



# mostrar todos los datos de un Pokémon a partir de su número y nombre –para este último, la búsqueda debe ser por proximidad, es decir si busco “bul” se deben mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos caracteres
def buscar_pokemon():
    pokemon = input("Ingrese el nombre del pokemon que desea buscar: ")
    for i in range(len(lista)):
        if pokemon in lista[i][1]:
            print(lista[i])
buscar_pokemon()

# mostrar todos los nombres de todos los Pokémons de un determinado tipo agua, fuego, planta y eléctrico;
def buscar_tipo():
    tipo = input("Ingrese el tipo de pokemon que desea buscar: ")
    for i in range(len(lista)):
        if tipo in lista[i][2]:
            print(lista[i][0])
buscar_tipo()

#realizar un listado en orden ascendente por número y nombre de Pokémon, y además un listado por nivel por nombre;
def ordenar_pokemon():
    lista.sort(key=lambda x: x[1])
    print(lista)
ordenar_pokemon()

#mostrar todos los Pokémons que son débiles frente a Jolteon, Lycanroc y Tyrantrum;
def debiles():
    debiles = ["Jolteon", "Lycanroc", "Tyrantrum"]
    for i in range(len(lista)):
        for j in range(len(debiles)):
            if debiles[j] in lista[i][3]:
                print(lista[i][0])
debiles()

# mostrar todos los tipos de Pokémons y cuántos hay de cada tipo.
def tipos():
    tipos = []
    for i in range(len(lista)):
        tipos.append(lista[i][2])
    print(tipos)
tipos()

def main2():
    print("1. Buscar pokemon")
    print("2. Buscar tipo")
    print("3. Ordenar pokemon")

    print("4. Debiles")
    print("5. Tipos")
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        buscar_pokemon()
    elif opcion == 2:
        buscar_tipo()
    elif opcion == 3:
        ordenar_pokemon()
    elif opcion == 4:
        debiles()
    elif opcion == 5:
        tipos()
    else:
        print("Opción incorrecta.")
main2()

if __name__ == "__main__":
    main2()
    