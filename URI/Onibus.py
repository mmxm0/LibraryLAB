
# -*- coding: <ASCII> -*-
import numpy as nx

'''
Created on May 8, 2018

@author: marta.maria.x.melo
'''

class Aresta:
    def __init__(self, x=None, y=None, z=nx.inf):
        self.__start = x
        self.__end = y
        self.__peso = z
        self.__id = "%s %s" %(str(x),str(y))

    def getId(self):
        return self.__id

    def getStart(self):
        return self.__start

    def getEnd(self):
        return self.__end

    def getPeso(self):
        return self.__peso

    def setPeso(self, p):
        self.__peso = p

    def setEnd(self, e):
        self.__end = e

    def setStart(self, s):
        self.__start = s

    def __repr__(self):
        return "("+str(self.__start)+", "+str(self.__end)+", "+str(self.__peso)+")"


class Vertice:
    def __init__(self, nome=None):
        self.__v = nome
        self.__in = []
        self.__cor = None
        self.__distancia = None
        self.__predecessor = None
        self.__d = None
        self.__f = None

    def setD(self,d):
        self.__d  =d

    def setF(self,f):
        self.__f = f

    def getD(self):
        return self.__d

    def getF(self):
        return self.__f

    def getV(self):
        return self.__v

    def getIn(self):
        return self.__in

    def setV(self,nv):
       self.__v = nv

    def setIn(self,a):
        self.__in.append(a)

    def getDistancia(self):
        return self.__distancia

    def setDistancia(self,d):
        self.__distancia = d

    def getCor(self):
        return self.__cor

    def setCor(self,c):
        self.__cor = c

    def getPredecessor(self):
        return self.__predecessor

    def setPredecessor(self,p):
        self.__predecessor = p

    def __repr__(self):
        return str(self.__v)


class BinHeap(Vertice):#Aresta)
    def __init__(self):
        super().__init__()
        self.heapLista = [0]
        self.tamAtual = 0

    def percUp(self, i):  # i e o tamanho Atual

        while i // 2 > 0:
            if self.heapLista[i].getDistancia()< self.heapLista[i // 2].getDistancia():
                tmp = self.heapLista[i // 2]
                self.heapLista[i // 2] = self.heapLista[i]
                self.heapLista[i] = tmp
            i = i // 2

    def insert(self, k):
        self.heapLista.append(k)
        self.tamAtual += 1
        self.percUp(self.tamAtual)

    def percDown(self, i):
        while (i * 2) <= self.tamAtual:
            mc = self.minFilho(i)
            if self.heapLista[i].getDistancia() > self.heapLista[mc].getDistancia():
                    tmp = self.heapLista[i]
                    self.heapLista[i] = self.heapLista[mc]
                    self.heapLista[mc] = tmp
            i = mc

    def minFilho(self, i):
        if i * 2 + 1 > self.tamAtual:
            return i * 2
        else:
            if self.heapLista[i * 2].getDistancia() < self.heapLista[i * 2 + 1].getDistancia():
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        retval = self.heapLista[1]
        self.heapLista[1] = self.heapLista[self.tamAtual]
        self.tamAtual = self.tamAtual - 1
        self.heapLista.pop()
        self.percDown(1)
        return retval

    def buildHeap(self, alist):
        i = len(alist) // 2
        self.tamAtual = len(alist)
        self.heapLista = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1
        return self.heapLista


class Grafo():

    def __init__(self, arestas, vertices):
        self.__arestas = [Aresta(*edge) for edge in arestas]
        self.__a = {(e[0],e[1]):e[2] for e in arestas}
        self.__vertices = [Vertice(e)for e in range(vertices)]
        self.__list = self.adj()
        self.__matriz = self.setMatriz()



    def getRaiz(self):
        return self.__vertices[0]

    def getVerticeX(self,x):
        return self.__vertices[x]

    def getArestaX(self,tuplaAresta):
        t = (tuplaAresta[1],tuplaAresta[0])
        if tuplaAresta in self.__a:
            return self.__a[tuplaAresta]
        elif t in self.__a:
            return self.__a[t]
        return 0

    def adj(self):
        listaAdj ={}
        for i in self.__vertices:
            listaAdj[i] =[]
            for j in self.__arestas:
                if j.getStart() == i.getV(): #leque de saida
                    listaAdj[i].append(self.__vertices[j.getEnd()])
                    i.setIn(j)
                if j.getEnd() == i.getV() and self.__vertices[j.getStart()] not in listaAdj[i]: #leque de entrada
                    listaAdj[i].append(self.getVerticeX(j.getStart()))
                    i.setIn(j)
        dicAdj={} #para Grafos dirigidos
        '''for i in self.__vertices:
            dicAdj[i] =[]
            for j in self.__arestas:
                if j.getStart() == i.getV(): #leque de saida
                    dicAdj[i].append(self.__vertices[j.getEnd()-1])'''
        return listaAdj

    def setMatriz(self):
        matriz = []
        for l in range(len(self.__vertices)):
            linha = []
            for c in range(len(self.__vertices)):
                if l == c:
                    linha.append(0)
                elif (l, c) in self.__a:
                    linha.append(self.__a[(l, c)])
                else:
                    linha.append(float("Inf"))
            matriz.append(linha)
        return matriz

    def getMatriz(self):
        return self.__matriz

    def dijkstra(self,s):
        for v in self.__vertices:
            v.setDistancia(nx.inf)
            v.setPredecessor(None)
        s.setDistancia(0)
        S =[]
        Q = BinHeap()
        for i in self.__vertices:
            Q.insert(i)

        while len(Q.heapLista) > 1:
            u = Q.delMin()
            S.append(u)
            for v in self.__list[u]:
                w = self.getArestaX((u.getV(),v.getV()))
                if v.getDistancia() > u.getDistancia()+w:
                    v.setDistancia(u.getDistancia()+w)
                    v.setPredecessor(u)

        return S

    def printaDistancias(self,s):
        saida = self.dijkstra(s)
        soma =[]
        for i in saida:
            #print("A menor distancia de %s para %s is : %s"%(str(s),str(i),str(i.getDistancia())))
            soma.append(i.getDistancia())

        return soma

    def listaSomatorioDjikstra(self):
        saida=[]
        for vertice in self.__vertices:
            beta = self.printaDistancias(vertice)
            saida.append(beta)
            if sum(saida[0]) > sum(beta):
                saida[0] = beta
        return max(saida[0])

    def floydWarshall(self):
        dist = self.__matriz.copy()
        for k in range(len(self.__vertices)):
            for i in range(len(self.__vertices)):
                for j in range(len(self.__vertices)):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        return dist
entrada = input().split()
N = int(entrada[0])
M = int(entrada[1])
arestas = []
while M > 0:
    nlinha = input().split()
    arestas.append((int(nlinha[0]),int(nlinha[1]),int(nlinha[2])))
    M-=1
grafo = Grafo(arestas,N)
print(grafo.listaSomatorioDjikstra())