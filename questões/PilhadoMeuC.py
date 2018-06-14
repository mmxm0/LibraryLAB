class No():

    def __init__(self, dados=None):
        self.__dado = dados
        self.__anterior = None
        self.__proximo = None

    def getProximo(self):
        return self.__proximo

    def setProximo(self, no):
        self.__proximo = no

    def getAnterior(self):
        return self.__anterior

    def setAnterior(self, no):
        self.__anterior = no

    def getDado(self):
        return self.__dado


class ListaEncadeada():
    def __init__(self):
        self._inicio = None
        self._fim = None
        self._len = None
        self.dadoExcluido = None

    def getInicio(self):
        return self._inicio

    def getFim(self):
        return self._fim

   # def setInicio(self, no):
    #    self._inicio = no

    #def setFim(self, no):
     #   self._fim = no
    def getDadoExcluido(self):
        return self.dadoExcluido
    def isVazia(self):
        if self._inicio == None:
            return True
        else:
            return False

    def InserirnoFim(self, dado):
        newno = No(dado)
        if self.isVazia():
            self._inicio = newno
            self._fim = newno
        else:
            self._fim.setProximo(newno)
            newno.setAnterior(self._fim)
            self._fim = newno

    def pesquisar(self, dado):
        if self.isVazia():
            print("Erro, Lista Vazia")
        else:
            nov = No(dado)
            i = self._inicio
            while nov.getDado() != i.getDado():
                i = i.getProximo()
                if i == None:
                    break
            else:
                return i

    def remover(self):
        if self.isVazia():
            r = "ERRO, LISTA VAZIA"

        else:
            if self._inicio == self._fim:
                r = self._fim.getDado()
                self._inicio = None
                self._fim = None

            else:

                e = self._fim
                r = self._fim.getDado()
                self.dadoExcluido = e.getDado()
                novoFim = e.getAnterior()
                self._fim = novoFim
                novoFim.setProximo(None)
        print(r)


    def listarPilha(self):
        if self.isVazia():
            print("Lista vazia")
        else:
            k = self._fim
            saida = "["
            while k != None:
                saida += (str(k.getDado()) + ", ")
                k = k.getAnterior()
            s = saida[:-2:]
            s +="]"
            print(s)

    def listar(self):

        if self.isVazia():
            print("Lista vazia")
        else:
            k = self._inicio
            saida = "["
            while k != None:
                saida += (str(k.getDado()) + ", ")
                k = k.getProximo()
            s = saida[:-2:]
            s+="]"
            print(s)

    def getLen(self):
        if self.isVazia():
            return 0
        else:
            k = self._inicio
            tamanho = 0
            while k != None:
                tamanho+=1
                k = k.getProximo()
            return tamanho


class Pilha(ListaEncadeada):
    def push(self,dado):
        self.InserirnoFim(dado)
    def pop(self):
        self.remover()

p = Pilha()
p.push(1)
p.push("B")
p.push("C")
p.pop()
