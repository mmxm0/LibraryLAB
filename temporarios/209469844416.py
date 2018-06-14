def virada(n):
    cont = 0
    if n == 0 and entrada[1]!= min(entrada):
        npilha = entrada[::]
        x = len(npilha)
        while cont< x:
            entrada[cont] = npilha.pop(-1)
            cont+=1
        return n
    elif n == 1:
        npilha = entrada[n::]
        cont = n
        while cont<len(entrada):
            entrada[cont]=npilha.pop(-1)
            cont+=1
        return
    elif n == 0 and entrada[1]== min(entrada):
        npilha = entrada[n+1::]
        x = len(npilha)
        cont+=1
        while cont<=x:
            entrada[cont] = npilha.pop(-1)
            cont+=1
        return n+1

def Indicemaior():
    cont = 0
    for i in range(len(entrada) - 1, -1, -1):
        if entrada[i] != max(entrada):
            cont += 1
        else:
            return cont

entrada = input().split()
entrada = [int(x) for x in entrada]
mirror = entrada[::]
saida =[0]
mirror.sort()
while entrada != mirror:
    N = entrada.index(max(entrada))
    m = virada(N)
    saida.append(m+1)

for i in range(len(saida)-1,-1,-1):
    print(saida[i], end=" ")
