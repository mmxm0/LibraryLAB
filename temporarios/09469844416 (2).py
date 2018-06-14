'''def insertionSort(lista):
    for j in range(1,len(lista)):
        chave = lista[j]
        i = j-1
        while i>=0 and lista[i]>chave:
            lista[i+1] = lista[i]
            i -=1
        lista[i+1] = chave
    return (lista)'''

entrada = input().split(",")


fila = []
idades =[]
saida = []
for i in entrada:
    if i.isnumeric():
        idade = entrada[entrada.index(i)]
        idades.append(idade)

while len(idades)>0:
    maior_idade_atual = max(idades)
    indic_mairIdadeAtual = idades.index(maior_idade_atual)
    indice_entrada = entrada.index((maior_idade_atual))
    fila.append(entrada[indice_entrada-1])
    entrada.pop(indice_entrada)
    entrada.pop(indice_entrada-1)
    idades.pop(indic_mairIdadeAtual)

string = ""
for i in fila:
    string+=i+","
print(string[:-1:])
