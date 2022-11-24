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

    def encode(self, texto):
        texto = list(texto)
        tabla = {"A": 0.2, "F": 0.17, "1": 0.13, "3": 0.21, "0": 0.05, "M": 0.09, "T": 0.15 }
        while len(texto) > 0:
            if texto[0] in tabla:
                print(tabla[texto[0]], end=" ")
                texto.pop(0)
    
    def decode(self, clave, raiz):
        pos = True
        while pos:
            if len(clave) > 0:
                pos = False
                if clave[0] == "1":
                    clave.pop(0)
                    if raiz.der.info is not None:
                        print(raiz.der.info, end=" ")
                    else:
                        pos = True
                        self.decode(clave, raiz.der)
                elif clave[0] == "0":
                    clave.pop(0)
                    if raiz.izq.info is not None:
                        print(raiz.izq.info, end=" ")
                    else:
                        pos = True
                        self.decode(clave, raiz.izq)
            else:
                pos = False
                    

            

