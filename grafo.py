from nodo3 import Nodo

class Grafo:
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





