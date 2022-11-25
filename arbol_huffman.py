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



    def main():
        huffman = Huffman()
        raiz = nodoArbol(None, 1)
        raiz.izq = nodoArbol(None, 0.5)
        raiz.der = nodoArbol(None, 0.5)
        raiz.izq.izq = nodoArbol("A", 0.2)
        raiz.izq.der = nodoArbol("F", 0.17)
        raiz.der.izq = nodoArbol("1", 0.13)
        raiz.der.der = nodoArbol("3", 0.21)
        raiz.izq.izq.der = nodoArbol("0", 0.05)
        raiz.izq.izq.izq = nodoArbol("M", 0.09)
        raiz.izq.der.izq = nodoArbol("T", 0.15)
        print("1. Encode")
        print("2. Decode")
        print("3. Salir")
        while True:
            eleccion = int(input("Qué quiere realizar: "))
            if eleccion == 1:
                texto = input("Introduzca el texto a codificar: ")
                huffman.encode(texto)
            elif eleccion == 2:
                clave = input("Introduzca la clave a decodificar: ")
                clave = list(clave)
                huffman.decode(clave, raiz)
            elif eleccion == 3:
                break
            else:
                print("Error, no se ha encontrado la opción")


if __name__ == "__main__":
    texto = 'AF130MT'
    Huffman.main()
    