from random import randint
from time import time
from Biblioteca.EstruturaDados import Fila
def bubblesort(lista):
    for i in range(len(lista)-1):
        for j in range(len(lista)-1-i):
            if lista[j] > lista[j+i]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

