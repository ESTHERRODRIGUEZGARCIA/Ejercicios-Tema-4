from ejer3.nodo3 import Nodo
class NodoArbol:
    def __init__(self, info):
        self.info = info
        self.izquierda = None
        self.derecha = None

    def __str__(self):
        return str(self.info)

class Grafo:
    arreglo = []
    def __init__(self, info):
        self.raiz = Nodo(info)

    def arbol_vacio(raiz):
        return raiz is None

    def __agregar_recursivo(self, nodo, info):
        if info < nodo.info:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(info)
            else:
                self.__agregar_recursivo(nodo.izquierda, info)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(info)
            else:
                self.__agregar_recursivo(nodo.derecha, info)


    def __buscar(self, nodo, busqueda):
        if nodo is None:
            return None
        if nodo.info == busqueda:
            return nodo
        elif busqueda < nodo.info:
               return self.__buscar(nodo.izquierda, busqueda)
        else:
            return self.__buscar(nodo.derecha, busqueda)

    def __inorden(self, nodo):
        if nodo is not None:
            self.__inorden(nodo.izquierda)
            print(nodo.info)
            self.__inorden(nodo.derecha)

        else:
            pass

    def __preorden(self, nodo):
        if nodo is not None:
            print(nodo.info)
            self.__preorden(nodo.izquierda)
            self.__preorden(nodo.derecha)

    def __postorden(self, nodo):
        if nodo is not None:
            self.__postorden(nodo.izquierda)
            self.__postorden(nodo.derecha)
            print(nodo.info)

# funciones públicas:

    def agregar(self, info):
        arreglo = self.__agregar_recursivo(self.raiz, info)

    def inorden(self):
        print("Imprimiendo árbol inorden: \n")
        self.__inorden(self.raiz)
        print("")

    def preorden(self):
        print("Imprimiendo árbol preorden: \n")
        self.__preorden(self.raiz)
        print("")

    def postorden(self):
        print("Imprimiendo árbol postorden: \n")
        self.__postorden(self.raiz)
        print("")

    def buscar(self, busqueda):
        return self.__buscar(self.raiz, busqueda)

''' def relacionar(self, vector1, vector2):
        arreglo = self.__relacionar(self.raiz, vector1, vector2)
        return arreglo

'''