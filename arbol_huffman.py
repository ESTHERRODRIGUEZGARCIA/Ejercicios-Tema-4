class nodoArbol():

    def __init__(self, info, frec, izq=None, der=None):
        self.info = info
        self.frec = frec
        self.izq = izq
        self.der = der

class Huffman():
    def __init__(self):
        self.lista = []
    
    def agregar(self, nodo):
        self.lista.append(nodo)
