class No:
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

    def getInicio(self):
        return self._inicio

    def getFim(self):
        return self._fim

    def isVazia(self):
        if self._inicio is None:
            return True
        else:
            return False

    def inserir(self, dado):
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
                if i is None:
                    break
            else:
                return i

    def remover(self):
        if self.isVazia():
            saida = "ERRO, LISTA VAZIA"

        elif self._inicio == self._fim:
            saida = self._fim.getDado()
            self._inicio = None
            self._fim = None

        else:
            e = self._fim
            saida = e.getDado()
            novoFim = e.getAnterior()
            self._fim = novoFim
            novoFim.setProximo(None)
        return saida

    def listarPilha(self):
        saida = "["
        if self.isVazia():
            saida += " ]"
        else:
            k = self._fim

            while k is not None:
                saida += (str(k.getDado()) + ", ")
                k = k.getAnterior()
        s = saida[:-2:]
        s += "]"
        print(s)

    def listar(self):
        saida = ""
        if self.isVazia():
            saida = None
        else:
            k = self._inicio

            while k is not None:
                saida += str(k.getDado())
                k = k.getProximo()

        return saida

    def getLen(self):
        if self.isVazia():
            return 0
        else:
            k = self._inicio
            tamanho = 0
            while k is not None:
                tamanho += 1
                k = k.getProximo()
            return tamanho

class Pilha(ListaEncadeada):
    def empilha(self, dado):
        self.inserir(dado)

    def desempilha(self):
        return self.remover()

    def mostrarPilha(self):
        return self.listar()

saida = ""

while True:
    try:
        linhaDeElementos = input().split()
        pilha = Pilha()
        for elemento in linhaDeElementos[::-1]:
            if elemento != "+" and elemento != "-" and elemento != "*" and elemento != "/":
                pilha.empilha(int(elemento))
            if elemento == "+" or elemento == "-" or elemento == "*" or elemento == "/":
                if elemento == "+":
                    num1 = pilha.desempilha()
                    num2 = pilha.desempilha()
                    soma = num1 + num2
                    pilha.empilha(soma)
                elif elemento == "-":
                    num1 = pilha.desempilha()
                    num2 = pilha.desempilha()
                    subtracao = num1 - num2
                    pilha.empilha(subtracao)
                elif elemento == "*":
                    num1 = pilha.desempilha()
                    num2 = pilha.desempilha()
                    multiplicacao = num1 * num2
                    pilha.empilha(multiplicacao)
                elif elemento == "/":
                    num1 = pilha.desempilha()
                    num2 = pilha.desempilha()
                    divisao = num1 / num2
                    pilha.empilha(int(divisao))
        saida+=str(pilha.mostrarPilha())+"\n"
    except:
        break
print(saida[:-1:])