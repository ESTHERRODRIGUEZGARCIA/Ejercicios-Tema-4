''' La Gran Muralla (China) Parte de la Gran Muralla China. ...
Petra (Jordania) La fachada principal de Petra (Jordania)EM. ...
El Coliseo (Italia) El Coliseo de Roma (Italia)EM. ...
Chichen Itza (México) El Chichen Itza en México. ...
Machu Picchu (Perú) ...
El Cristo Redentor (Brasil) ...
Taj Mahal (India)
'''

from grafo import Grafo

grafo = Grafo("LAS 7 MARAVILLAS DEL MUNDO")
grafo.agregar("La Gran Muralla")
grafo.agregar("Petra")
grafo.agregar("El Coliseo")
grafo.agregar("Chichen Itza")
grafo.agregar("EL Cristo Redentor")
grafo.agregar("Taj Mahal")

grafo.preorden()
grafo.inorden()
grafo.postorden()

busqueda = input("Busca algo en el grafo: ")
nodo = grafo.buscar(busqueda)
if nodo is None:
    print(f"{busqueda} no existe. ")
else:
    print(f"{busqueda} sí existe. ")