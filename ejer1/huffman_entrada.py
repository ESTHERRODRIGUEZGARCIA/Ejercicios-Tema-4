from ejer1.huffman_archivo import *

print("####################################")
print("##      Algoritmo de Huffman      ##")
print("####################################")

class Algoritmo:
    tabla = {"A": 0.2, "F": 0.17, "1": 0.13, "3": 0.21, "0": 0.05, "M": 0.09, "T": 0.15 }
    arbol = HuffmanTree(tabla)

    def letras_codificadas():
        arbol = HuffmanTree(Algoritmo.tabla)
        arbol.encode()

def lanzador():
    eleccion = int(input("QUé quiere realizar: "))
    if eleccion == 1:
        Algoritmo.letras_codificadas()
        lanzador()

   # my_string = input("\nIntroduzca una cadena de caracteres para realizar su compresion: \n")
    #len_string = len(my_string)

    #print("Su mensaje es: \n")
   # print(my_string)

if __name__ == "__main__":
    lanzador()