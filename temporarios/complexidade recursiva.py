entrada = input().split()
entrada.pop(0)
entrada.pop(-1)

for elemento in entrada:
    if elemento.isnumeric():
        index = entrada.index(elemento)
        entrada[index]= int(elemento)
print(entrada)
def complexidadeRecursiva(entrada, cont, soma):
    if entrada[cont]=="LOOP":
        soma += soma * entrada[cont+1]
        return complexidadeRecursiva(entrada,cont+1,soma)
    elif entrada[cont]=="OP":
        soma += entrada[cont+1]
        return complexidadeRecursiva(entrada,cont+1,soma)
    elif entrada[cont]=="FIM":
        return soma
    else:
        return  complexidadeRecursiva(entrada,cont+1,soma)

print(complexidadeRecursiva(entrada,0,1))
