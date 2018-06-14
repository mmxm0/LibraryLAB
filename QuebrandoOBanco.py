entrada = input().split()
A = int(entrada[0])
B = int(entrada[1])
string = input()


def toList(string):
    l = [None] * len(string)
    for i in range(len(l)):
        l[i] = string[i]
    return l


def ponteiro(lista, a, b):
    ponteiros = []
    count = 0
    x = 0  # ponteiro de parada
    inicio = 0
    while count < b:
        """y = a - b + count
        xid = lista.index(min(lista[x:y:]))
        ponteiros.append(xid)
        print(lista[xid:y:], min(lista[xid:y:]))
        x = xid+1
        count += 1"""
        fim = a-b
        decimais = lista[fim+1::]
        numinteiro = lista[inicio:fim+1:]
        lista = menoString(numinteiro)+decimais


        count+=1

    return lista

def menoString(string):
    st = list(string)
    minimo = min(st)
    st.pop(st.index(minimo))
    return toString(st)

def remove(string, lponteiros):
    for i in lponteiros:
        string[i] = None

    return string


def toString(lista):
    string = ""
    for i in lista:
        if i is not None:
            string += str(i)

    return string



lponteiros = ponteiro(string, A, B)
print(lponteiros)
