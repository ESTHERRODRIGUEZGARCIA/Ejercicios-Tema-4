import heapq
from heapq import heappop, heappush
class Node(object):
    def __init__(self, ch, freq, left=None, right=None):
        self.ch = ch
        self.freq = freq
        self.left = left
        self.right = right

    #Anulo función `__lt__()` para hacer que la clase `Nodo` funcione con la cola de prioridad de modo que el elemento de mayor prioridad tenga la frecuencia más baja

    def __lt__(self, other):
        return self.freq < other.freq



def leaf(root):
    return root.left is None and root.right is None

#creo árbol y almaceno los códigos de Huffman en un diccionario

def encode(root, s, huffman_code):
    if root is None:
        return None
    
    if leaf(root):
        huffman_code[root.ch] = s if len(s) > 0 else '1'

    encode(root.left, s + '0', huffman_code)
    encode(root.left, s + '1', huffman_code)

def decode(root, index, s):
    if root is None:
        return index
    
    if leaf(root):
        print(root.ch, end='')
        return index
    
    index = index + 1
    root = root.left if s[index] == '0' else root.right
    return decode(root, index, s)

    # Construye 'Huffman Tree' y decodifica el texto de entrada dado

def HuffmanTree(text):
    if len(text) == 0: # cadena vacía
        return None

    freq = {i: text.count(i) for i in set(text)} #freq de cada caracter + dic

    pq = [Node(k,v) for k, v in freq.items()]
    heapq.heapify(pq)

    while len(pq) != 1:
        # eliminar los nodos con la frq más baja de la cola
        left = heappop(pq)
        right = heappop(pq)
        # nuevo nodo interno con dos nodos hijos ( freq = f1+f2)
        total = left.freq + right.freq
        heappush(pq, Node(None, total, left, right))

    root = pq[0] #almacena el puntero a la raiz del árbol
    huffmanCode = {}
    encode(root, '', huffmanCode)

    print("EL código es: ", huffmanCode )
    print("El verdadero es: ")

    s = ''
    for c in text:
        s += huffmanCode.get(c)

    print("Texto codificado: ", s)
    print("texto descoodificado: ", end='')


    if leaf(root):
        while root.freq > 0:
            print(root.ch, end= ' ')
            root.freq = root.freq - 1
    else:
        index = -1
        while index < len(s) -1:
            index = decode(root, index, s)

if __name__ == '__main__':
    text = 'Probando texto'
    HuffmanTree(text)
