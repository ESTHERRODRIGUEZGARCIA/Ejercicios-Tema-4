class Node(object):
    def __init__(self, ch, freq, left=None, right=None):
        self.ch = ch
        self.freq = freq
        self.left = left
        self.right = right

    #Anulo función `__lt__()` para hacer que la clase `Nodo` funcione con la cola de prioridad de modo que el elemento de mayor prioridad tenga la frecuencia más baja

    def __lt__(self, other):
        return self.freq < other.freq

    #creo árbol y almaceno los códigos de Huffman en un diccionario

def leaf(root):
    return root.left is None and root.right is None

def encode(root, s, huffman_code):
    if root is None:
        return None
    
    if leaf(root):
        huffman_code[root.ch] = s if len(s) > 0 else '1'

    encode(root.left, s + '0', huffman_code)
    encode(root.left, s + '1', huffman_code)

