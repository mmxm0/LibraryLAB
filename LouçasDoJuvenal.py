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

    def inserirFim(self,dado):
        newno = No(dado)
        if self.isVazia():
            self._inicio = newno
            self._fim = newno
        else:
            self._inicio.setAnterior(newno)
            newno.setProximo(self._inicio)
            self._inicio = newno

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
            saida+=" ]"
        else:
            k = self._fim

            while k is not None:
                saida += (str(k.getDado()) + ", ")
                k = k.getAnterior()
        s = saida[:-2:]
        s +="]"
        print(s)


    def listar(self):
        saida = []
        if self.isVazia():
            saida = None
        else:
            k = self._inicio

            while k is not None:
                saida.append(str(k.getDado()))
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

    def push(self, dado):
        self.inserir(dado)

    def pop(self):
        return self.remover()

    def pushDown(self,dado):
        self.inserirFim(dado)


class Deck(Pilha):
    def __init__(self):
        Pilha.__init__(self)
        self._pilhaDCartas = None

    def iniciaDeck(self,lista):
        l = lista[::-1]
        deck = Pilha()
        for i in l:
            deck.push(i)
        self._pilhaDCartas = deck

    def voltarComeco(self):
        inicio = self._fim.getDado()
        self.pop()
        self.pushDown(inicio)

class Jogador:

    def __init__(self, pilha):
        self._deck = pilha

    def getDeck(self):
        return self._deck

    def novoDeck(self):
        d = Deck()
        d.iniciaDeck(self._deck)
        self._deck = d

    def devolveCarta(self):
        self._deck.voltarComeco()

    def pegaCarta(self):
       return self._deck.pop()


class Jogo():
    def __init__(self,lista,l):
        self.jogadores = lista #lista contendo objeto jogador
        self.mesa = l #pilha da casa (tb é um jogador)

    def rodada(self):
        cartaDaVez = self.mesa.pegaCarta()
        for j in self.jogadores:
            if j.pegaCarta() != cartaDaVez:
                pass


    #def rodada(self):
     #   for jogador in self.jogadores:
        #    if jogador.isVazia():
      #
       #     if jogador.getCarta().getDado() == self.casa.getCarta().getDado():



'''
class Deck(Pilha):

    def VoltarComeco(self):
        inicio = self._fim.getDado()
        self.pop()
        self.push(inicio)

    def PrimeiraCarta(self):
        return (self._inicio.getDado())


class Jogador:
    def __init__(self, nome, deck):
        self.nome = nome
        self.deck = deck


class Jogo(Jogador):
    def __init__(self, listajogadores, nome, deck):
        Jogador.__init__(self, nome, deck)
        self.jogadores = listajogadores
        self.ganhadores = []

    def getGanhadores(self):
        return self.ganhadores

    def melhorJogador(self):
        m = 10 ** 5
        for a in self.ganhadores:
            if int(a) <= m:
                m = a
        return m

    def jogar(self,Mesa):
        ganhadores = []
        for h in range(0, 1000):
            carta = Mesa.PrimeiraCarta()
            for h in self.jogadores:
                if h.deck.PrimeiraCarta() == carta:
                    h.deck.removerdoFim()
                else:
                    h.deck.VoltarComeco()
                if h.deck.isVazia():
                    ganhadores.append(h.nome)
            Mesa.VoltarComeco()
            if len(self.ganhadores) != 0:
                break
        else:
            return '0'
        if len(ganhadores) == 1:
            return str(ganhadores[0])
        else:
            return str(self.melhorJogador())

festas = int(input())
saida = []
for i in range(festas):
    deck_da_mesa = input().split()
    jogadores = []
    Mesa = Deck()
    for k in deck_da_mesa:
        Mesa.push(k)
    contador = 1
    for g in range(10 ** 5):
        deck = input().strip()
        if deck == '-1':
            break
        else:
            deck = deck.split(' ')
            deckJogador = Deck()
            for t in deck:
                deckJogador.push(t)
            jo = Jogador(contador, deckJogador)
            jogadores.append(jo)
            contador += 1
    saida.append(jogar(Mesa, jogadores))
saida = list(map(lambda a: a, saida))
output = ""
for i in saida:
    output += str(i) + "\n"
'''