class Pais:
    nome = 1

    def __init__(self, ouro=0, prata=0, bronze=0):
        self.id = Pais.nome
        Pais.nome += 1
        self.qtddOuro = ouro
        self.qtddPrata = prata
        self.qtddBronze = bronze

    def __repr__(self):
        return str(self.id)

    def getOuro(self):
        return self.qtddOuro

    def getPrata(self):
        return self.qtddPrata

    def getBronze(self):
        return self.qtddBronze

    def getNome(self):
        return self.id

def quicksortOuro(x):
    if len(x) <= 1:
        return x
    menor, igual, maior = [], [], []
    p = x[0]
    for i in x:
        if i.getOuro() < p.getOuro():
            menor.append(i)
        elif i.getOuro() == p.getOuro():
            igual.append(i)

        else:
            maior.append(i)
    igual = quicksortPrata(igual)
    return quicksortOuro(maior) + igual + quicksortOuro(menor)

def quicksortPrata(x):
    if len(x) <= 1:
        return x
    menor, igual, maior = [], [], []
    p = x[0]
    for i in x:
        if i.getPrata() < p.getPrata():
            menor.append(i)
        elif i.getPrata() == p.getPrata():
            igual.append(i)
        else:
            maior.append(i)
    igual = quicksortBronze(igual)
    return quicksortPrata(maior) + igual + quicksortPrata(menor)

def quicksortBronze(x):
    if len(x) <= 1:
        return x
    menor, igual, maior = [], [], []
    p = x[0]
    for i in x:
        if i.getBronze() < p.getBronze():
            menor.append(i.getBronze())
        elif i.getBronze() == p.getBronze():
            igual.append(i)
        else:
            maior.append(i)
    igual = quicksortNome(igual)
    return quicksortBronze(maior) + igual + quicksortBronze(menor)


def quicksortNome(x):
    if len(x) <= 1:
        return x
    menor, igual, maior = [], [], []
    p = x[0]
    for i in x:
        if i.getNome() < p.getNome():
            menor.append(i)
        elif i.getNome() == p.getNome():
            igual.append(i)
        else:
            maior.append(i)
    return quicksortNome(menor) + igual + quicksortNome(maior)


entrada = input().split()
N = int(entrada[0])  # Numero de Paises 1<=N<=100
M = int(entrada[1])  # Numero de modalidades 1<=N<=100
paises = []
ouro = [0] * (N + 1)
prata = [0] * (N + 1)
bronze = [0] * (N + 1)
saida = ""

for i in range(M):  # preenchendo as listas
    entr = input().split()
    if ouro[int(entr[0])] != None:
        ouro[int(entr[0])] += 1
    else:
        ouro[int(entr[0])] = 1
    if prata[int(entr[1])] != None:
        prata[int(entr[1])] += 1
    else:
        prata[int(entr[1])] = 1
    if bronze[int(entr[2])] != None:
        bronze[int(entr[2])] += 1
    else:
        bronze[int(entr[2])] = 1

for p in range(1, N + 1):
    n = Pais(ouro[p], prata[p], bronze[p])
    paises.append(n)

paises = quicksortOuro(paises)

for m in paises:
    saida += str(m.getNome()) + " "

print(saida)
