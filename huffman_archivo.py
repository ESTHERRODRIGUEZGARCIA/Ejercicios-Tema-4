class Node(object):
    def __init__(self, ch, freq, left=None, right=None):
        self.ch = ch
        self.freq = freq
        self.left = left
        self.right = right

    #Anulo función `__lt__()` para hacer que la clase `Nodo` funcione con la cola de prioridad de modo que el elemento de mayor prioridad tenga la frecuencia más baja

    def __lt__(self, other):
        return self.freq < other.freq

        