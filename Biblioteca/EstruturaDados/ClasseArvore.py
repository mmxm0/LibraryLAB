class No:
      def __init__(self,chave,dado):
            self._chave = chave
            self._pai = None
            self._filhoEsquerdo = None
            self._filhoDireito = None
            self._dado = dado

      def getChave(self):
            return self._chave
      
      def getPai(self):
            return self._pai
      
      def getFilhoEsquerdo(self):
            return self._filhoEsquerdo
      
      def getFilhoDireito(self):
            return self._filhoDireito
      
      def setChave(self,chave):
            self._chave = chave
            
      def setPai(self,pai):
            self._pai = pai
            
      def setFilhoEsquerdo(self,esquerdo):
            self._filhoEsquerdo = esquerdo
            
      def setFilhoDireito(self,direito):
            self._filhoDireito = direito

      def getDado(self):
            return self._dado
            
      def setDado(self,dado):
            self._dado = dado
            
      def __str__(self):
            return  str(self._dado)

class ArvoreBinariaDeBusca:

      def __init__(self):
            self._raiz = None

      def _repr_(self):
            print('[', end='')
            self.emOrdem(self.__raiz)
            return ']'

      def getRaiz(self):
            return self._raiz

      def setRaiz(self,valor):
            self._raiz = valor

      def isVazia(self):
            return self._raiz is None
      
      def inserir(self,chave,dado):
            z = No(chave,dado)
            y = None
            x = self.getRaiz()
            while x != None:
                  y = x
                  if chave < x.getChave():
                        x = x.getFilhoEsquerdo()
                  else:
                        x = x.getFilhoDireito()
            z.setPai(y)
            if y == None:
                  self.setRaiz(z)
            else:
                  if chave < y.getChave():
                        y.setFilhoEsquerdo(z)
                  else:
                        y.setFilhoDireito(z)

      def pesquisar(self,x,chave):
            if x == None or chave == x.getChave():
                  return x
            if chave < x.getChave():
                  return self.pesquisar(x.getFilhoEsquerdo(),chave)
            else:
                  return self.pesquisar(x.getFilhoDireito(),chave)
            
      def minimo(self,x):
            while x.getFilhoEsquerdo() != None:
                  x = x.getFilhoEsquerdo()
            return x

      def maximo(self,x):
            while x.getFilhoDireito() != None:
                  x = x.getFilhoDireito()
            return x

      def sucessor(self,x):
            if x == None:
                  return None
            if x.getFilhoDireito() != None:
                  return self.minimo(x.getFilhoDireito())
            else:
                  y = x.getPai()
                  while y != None and x == y.getFilhoDireito():
                        x=y
                        y=y.getPai()
                  return y

      def antecessor(self,x):
            if x == None:
                  return None
            if x.getFilhoEsquerdo() != None:
                  return self.maximo(x.getFilhoEsquerdo())
            else:
                  y = x.getPai()
                  while y != None and x == y.getFilhoEsquerdo():
                        x=y
                        y=y.getPai()
                  return y
            
      def preOrdem(self, no):
        if no != None:
            print(no.getChave(), end=" ")
            self.preOrdem(no.getFilhoEsquerdo())
            self.preOrdem(no.getFilhoDireito())
        else:
            pass

      def emOrdem(self, no):
        if no != None:
            self.emOrdem(no.getFilhoEsquerdo())
            print(no.getChave(), end=' ')
            self.emOrdem(no.getFilhoDireito())
        else:
            pass

      def posOrdem(self, no):
        if no != None:
            self.posOrdem(no.getFilhoEsquerdo())
            self.posOrdem(no.getFilhoDireito())
            print(no.getChave(), end=" ")
        else:
            pass
      def remover(self,z):
            if z.getFilhoEsquerdo() == None or z.getFilhoDireito() == None:
                  y=z
            else:
                  y = self.sucessor(z)

            if y.getFilhoEsquerdo() != None:
                  x = y.getFilhoEsquerdo()
            else:
                  x = y.getFilhoDireito()

            if x != None:
                  x.setPai(y.getPai())

            if y.getPai == None:
                  self._raiz = x

            else:
                  if y == y.getPai().getFilhoEsquerdo():
                        y.getPai().setFilhoEsquerdo(x)
                  else:
                        y.getPai().setFilhoDireito(x)
            if y!=z:
                  z.setChave(y.getChave())
                  z.setDado(y.getDado())
            return y

arvore = ArvoreBinariaDeBusca()
entrada = input().split()
listanode = []

for i in range(len(entrada)):
    if entrada[i] == "I":
        arvore.inserir(int(entrada[i+1]),int(entrada[i+1]))
        no = No(int(entrada[i+1]),int(entrada[i+1]))
        listanode.append(no)

    if entrada[i] == "Q":
            arvore.pesquisar(arvore.getRaiz(),int(entrada[i+1]))

    if entrada[i] == "R":
            noremover = arvore.pesquisar(arvore.getRaiz(),int(entrada[i+1]))
            print(arvore.remover(noremover))
    if entrada[i] == "IN":
        arvore.emOrdem(listanode[0])
    if entrada[i] == "POST":
        arvore.posOrdem(listanode[0])
    if entrada[i] == "PRE":
        arvore.preOrdem(listanode[0])















                  
                  

                                      
