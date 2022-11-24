'''
La Gran Muralla (China) Parte de la Gran Muralla China. ...
Petra (Jordania) La fachada principal de Petra (Jordania)EM. ...
El Coliseo (Italia) El Coliseo de Roma (Italia)EM. ...
Chichen Itza (México) El Chichen Itza en México. ...
Machu Picchu (Perú) ...
El Cristo Redentor (Brasil) ...
Taj Mahal (India)
'''

from grafo import Grafo

'''

'''

#a) VECTORES
grafo = Grafo("AA: LAS 7 MARAVILLAS DEL MUNDO: \n")
grafo.agregar("La Gran Muralla, China, Arquitectónica (7) \n")
grafo.agregar("Petra, Jordania, Arquitectónica (5) \n")
grafo.agregar("El Coliseo, Italia, Arquitectónica (4) \n")
grafo.agregar("Chichen Itza, México, Arquitectónica (1) \n")
grafo.agregar("Machu Picchu, Perú, Arquitectónica (2) \n")
grafo.agregar("EL Cristo Redentor, Brasil, Arquitectónica (3) \n")
grafo.agregar("Taj Mahal, India, Arquitectónica (6) \n")

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
grafo.relacionar("A", "B")