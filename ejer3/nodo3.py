class Nodo:
    def __init__(self, info):
        self.info = info
        self.izquierda = None
        self.derecha = None

    def __str__(self):
        return str(self.info)


