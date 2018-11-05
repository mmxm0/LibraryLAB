import random
from time import time

from Biblioteca.Ordenação.bubbleSort import bubblesort


def quicksort(x):
    if len (x) <= 1:
        return x
    menor, igual, maior = [], [], []
    p = x[0]
    for i in x:
        if i < p:
            menor.append(i)
        elif i == p:
            igual.append(i)
        else:
            maior.append(i)
    return quicksort(menor) + igual + quicksort(maior)

lista = []
for i in range(10):
    lista.append(random.randint(0,10))
tempIni = time()
lista2 = lista[::]
print("ANTES do QuickSort: %s"%lista)
lista = quicksort(lista)
print("DEPOIS do QuickSort: %s"%lista)
tempFin = time()
print("tempo de execução total aprox. para esse algoritmo: %f"%(tempFin-tempIni))
tempIni = time()
print("ANTES do BubbleSort: %s"%lista2)
lista2 = bubblesort(lista2)
print("ANTES do BubbleSort: %s"%lista2)
tempFin = time()
print("tempo de execução total aprox. para esse Algoritmo: %f"%(tempFin-tempIni))