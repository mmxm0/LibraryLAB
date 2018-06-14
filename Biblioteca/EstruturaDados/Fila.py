class No:
    def __init__(self, dados):
        self._anterior = None
        self._proximo = None
        self._dados = dados

    def getAnterior(self):
        return self._anterior

    def setAnterior(self, novoAnt):
        self._anterior = novoAnt

    def getProximo(self):
        return self._proximo

    def setProximo(self, novoProx):
        self._proximo = novoProx

    def getDados(self):
        return self._dados

    def setDados(self, novoDados):
        self._dados = novoDados

class ListaDuplamenteEncadeada():
    def __init__(self):
        self._inicio = None
        self._fim = None

    def isVazia(self):
        if self._inicio == None:
            return True
        else:
            return False

    def inserirNoFim(self, dado):
        novoNo = No(dado)
        if self.isVazia():
            self._inicio = novoNo
            self._fim = novoNo
        else:
            self._fim.setProximo(novoNo)
            novoNo.setAnterior(self._fim)
            self._fim = novoNo

    def removerDoInicio(self):
        if self.isVazia():
            return 'Lista Vazia'
        elif self._inicio == self._fim:
            dado = self._inicio
            self._inicio = None
            self._fim = None

        else:
            dado = self._inicio
            self._inicio.getProximo().setAnterior(None)
            self._inicio = self._inicio.getProximo()
        return dado

class Fila(ListaDuplamenteEncadeada):
    def remover(self):
        return self.removerDoInicio()

    def inserir(self, dado):
        return self.inserirNoFim(dado)

def transformaLinhaEmFila(linha):
    filaAtual = Fila()
    linha = linha.split()
    for i in linha:
        filaAtual.inserir(i)
    return filaAtual
