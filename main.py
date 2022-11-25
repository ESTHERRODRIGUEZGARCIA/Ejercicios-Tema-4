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

grafo.relacionar(A, B, 1)