'''
Created on May 4, 2018

@author: marta.maria.x.melo
'''
linha1 = input().split()
planos = [None]*int(linha1[0])
dcPlanos = {0:[]}
coordenadasP = [None]*int(linha1[1])
#input lista de planos
for i in range(len(planos)):
    p = input().split()
    planos[i]= [int(x) for x in p]
    dcPlanos[i]=[]
print(planos)
#input lista de coordenadas
for j in range(len(coordenadasP)):
    c = input().split()
    coordenadasP[j] = [int(x) for x in c]
