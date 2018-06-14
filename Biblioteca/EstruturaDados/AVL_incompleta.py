class Noh:
    def __init__(self, idnoh, valordado):
        self.__index = idnoh
        self.__dado = valordado
        self.__esquerdo = None
        self.__direito = None
        self.__pai = None
        self.__altura = 1

    def getIndex(self):
        return self.__index

    def getDado(self):
        return self.__dado

    def getEsquerdo(self):
        return self.__esquerdo

    def getDireito(self):
        return self.__direito

    def getPai(self):
        return self.__pai

    def getAltura(self):
        return self.__altura

    def setIndex(self, novoId):
        self.__index=novoId

    def setDado(self, novoDado):
        self.__dado = novoDado

    def setEsquerdo(self, novoEsq):
        self.__esquerdo = novoEsq

    def setDireito(self, novoDir):
        self.__direito = novoDir

    def setPai(self, novopai):
        self.__pai = novopai

    def setAltura(self):
        self.__altura +=1

    def __repr__(self):
        return "%i" % self.__index

class Arvore(Noh):
    def __init__(self):
        self.__raiz = None

    def altura(self, noh):
        h = noh.getAltura()
        h = 2 ** h - 1
        return h

    def percorrer(self, no):
        if no != None:
            self.percorrer(no.getEsquerdo())
            print(no.getIndex(), end=' ')
            self.percorrer(no.getDireito())
        else:
            pass

    def posOrdem(self, no):

        if no != None:
            self.posOrdem(no.getEsquerdo())
            self.posOrdem(no.getDireito())
            print(no.getIndex(), end=" ")

        else:
            pass

    def preOrdem(self, no):
        if no != None:
            print(no.getIndex(), end=" ")
            self.preOrdem(no.getEsquerdo())
            self.preOrdem(no.getDireito())
        else:
            pass

    def _repr_(self):
        print('[', end='')
        self.percorrer(self.__raiz)
        return ']'

    def adicionar(self, no):
        pivo = self.__raiz
        pai = None
        while pivo != None:
            pai = pivo
            if no.getIndex() < pivo.getIndex():
                pivo = pivo.getEsquerdo()
            else:
                pivo = pivo.getDireito()
        no.setPai(pai)
        if pai is None:
            self.__raiz = no
        else:
            if no.getIndex() < pai.getIndex():
                pai.setEsquerdo(no)
            else:
                pai.setDireito(no)

    def pesquisa(self, chave):
        no = self.__raiz
        while no is not None and chave != no.getIndex():
            noanterior = no
            if chave < no.getIndex():
                no = no.getEsquerdo()
            else:
                no = no.getDireito()
        return no

    def pesquisaC(self, chave):
        no = self.__raiz
        while no is not None and chave != no.getIndex():
            if chave < no.getIndex():
                no = no.getEsquerdo()
            else:
                no = no.getDireito()
        return self.antecessor(no)

    def remove(self, key):
        z = self.pesquisa(key)
        if (z == None):
            print('Elemento não pertence a árvore.')
            return z

        if z.getEsquerdo() == None or z.getDireito() == None:
            y = z
        else:
            y = self.sucessor(z)

        if (y.getEsquerdo() != None):
            x = y.getEsquerdo()
        else:
            x = y.getDireito()

        if (x != None):
            x.setPai(y.getPai())

        if (y.getPai() == None):
            self.__raiz = x
        else:
            if (y == y.getPai().getEsquerdo()):
                y.getPai().setEsquerdo(x)
            else:
                y.getPai().setDireito(x)

        if (y != z):
            z.setIndex(y.getIndex())
            z.setDado(y.getDado())

        return y

    def sucessor(self, x):
        if x == None:
            return None
        if x.getDireito() != None:
            return self.minimo(x.getDireito())
        else:
            y = x.getPai()
            while y != None and x == y.getDireito():
                x = y
                y = y.getPai()
            return y

    def minimo(self, x):
        while x.getEsquerdo() != None:
            x = x.getEsquerdo()
        return x

    def maximo(self, x):
        while x.getDireito() != None:
            x = x.getDireito()
        return x
    def antecessor(self, x):
        if x == None:
            return None
        if x.getEsquerdo() != None:
            return self.maximo(x.getEsquerdo())
        else:
            y = x.getPai()
            while y != None and x == y.getEsquerdo():
                x = y
                y = y.getPai()
            return y


arvore = Arvore()
entrada = input().split()

listanode = []

for i in range(len(entrada)):
    if entrada[i] == "I":
        no = Noh(int(entrada[i+1]),int(entrada[i+1]))
        arvore.adicionar(no)
        listanode.append(no)

    if entrada[i] == "Q":
        print(arvore.pesquisaC(int(entrada[i+1])),end="; ")
    if entrada[i] == "R":
        arvore.remove(int(entrada[i+1]))
    if entrada[i] == "IN":
        arvore.percorrer(listanode[0])
        print(end="; ")
    if entrada[i] == "POST":
        arvore.posOrdem(listanode[0])
        print(end="; ")
    if entrada[i] == "PRE":
        arvore.preOrdem(listanode[0])
        print(end="; ")