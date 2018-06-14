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

entrada = input().split()
N = int(entrada[0])  # Numero de Paises 1<=N<=100
M = int(entrada[1])  # Numero de modalidades 1<=N<=100
paises = [0] * (N)
ouro = [0] * (N + 1)
prata = [0] * (N + 1)
bronze = [0] * (N + 1)
saida = ""
for j in range(N):
    paises[j] = j + 1

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

def teste(pivo):
    print("O país %s tem:\n - %s medalhas de OURO\n - %s medalhas de PRATA \n - %s medalhas de BRONZE" %
          (str(paises[paises.index(pivo)]), str(ouro[pivo]), str(prata[pivo]), str(bronze[pivo])))  # Teste

'''
copyOuro = ouro[::]
copyPrata = prata[::]
copyBronze = bronze[::]
copyBronze.pop(0)
copyPrata.pop(0)
copyOuro.pop(0)
while len(paises) > 0:
    copyOuro.sort()
    topOuro = copyOuro.pop(-1)
    if copyOuro.count(topOuro) == None:
        remover = ouro.index(topOuro)
    else:
        copyPrata.sort()
        topPrata = copyPrata.pop(-1)
        if copyPrata.count(topPrata) == None:
            remover = prata.index(topPrata)
        else:
            copyBronze.sort()
            topBronze = copyBronze.pop(-1)
            # if copyBronze.count(topBronze)==None:
            remover = bronze.index(topBronze)
    print(remover)
    saida += str(paises.pop(paises.index(remover))) + " "
print(saida)
'''#meuErroMinhaDor
