'''
La Gran Muralla (China) Parte de la Gran Muralla China. ...
Petra (Jordania) La fachada principal de Petra (Jordania)EM. ...
El Coliseo (Italia) El Coliseo de Roma (Italia)EM. ...
Chichen Itza (México) El Chichen Itza en México. ...
Machu Picchu (Perú) ...
El Cristo Redentor (Brasil) ...
Taj Mahal (India)
'''

from ejer3.grafo import Grafo
from ejer3.grafo import NodoArbol

'''

'''
def agregar_vertices(grafo, lista):
    for i in range(len(lista)):
        grafo.agregar_vertice(lista[i])

def agregar_aristas(grafo, lista):
    for i in range(len(lista)):
        for j in range(len(lista)):
            if i != j:
                grafo.agregar_arista(lista[i], lista[j], 1)

def main(info):
    grafo = Grafo(info)
    lista = ["La Gran Muralla (China)", "Petra (Jordania)", "El Coliseo (Italia)", "Chichen Itza (México)", "Machu Picchu (Perú)", "El Cristo Redentor (Brasil)", "Taj Mahal (India)"]
    agregar_vertices(grafo, lista)
    agregar_aristas(grafo, lista)
    print(grafo)
    print(grafo.obtener_vertices())
    print(grafo.obtener_aristas())
    print(grafo.obtener_adyacentes("La Gran Muralla (China)"))
    print(grafo.obtener_adyacentes("El Cristo Redentor (Brasil)"))
    print(grafo.obtener_adyacentes("Taj Mahal (India)"))
    print(grafo.obtener_adyacentes("Chichen Itza (México)"))
    print(grafo.obtener_adyacentes("Machu Picchu (Perú)"))
    print(grafo.obtener_adyacentes("El Coliseo (Italia)"))
    print(grafo.obtener_adyacentes("Petra (Jordania)"))


#a) VECTORES
grafo = Grafo("AA: LAS 7 MARAVILLAS DEL MUNDO: \n")
A = grafo.agregar("La Gran Muralla, China, Arquitectónica (7) \n") 
B = grafo.agregar("Petra, Jordania, Arquitectónica (5) \n")
C = grafo.agregar("El Coliseo, Italia, Arquitectónica (4) \n")
D = grafo.agregar("Chichen Itza, México, Arquitectónica (1) \n")
E = grafo.agregar("Machu Picchu, Perú, Arquitectónica (2) \n")
F = grafo.agregar("EL Cristo Redentor, Brasil, Arquitectónica (3) \n")
G = grafo.agregar("Taj Mahal, India, Arquitectónica (6) \n")

grafo.preorden()
grafo.inorden()
grafo.postorden()

busqueda = input("Busca algo en el grafo: ")
nodo = grafo.buscar(busqueda)
if nodo is None:
    print(f"{busqueda} no existe. ")
else:
    print(f"{busqueda} sí existe. ")

#b)
# grafo: cada una debe estar relacionada con las otras seis de su tipo, para lo que se debe almacenar la distancia que las separa;

#grafo.relacionar(A, B, 1)


if __name__ == "__main__":
    main(info="AA: LAS 7 MARAVILLAS DEL MUNDO: \n")


