#matriz com listas
matriz = []
linhas = 4
colunas = 4
valor = 0
for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append("%.2d" %valor)
        valor +=1
    matriz.append(linha)

'''imprimir a matriz '''
contador = 0
for acessamatriz in matriz:
    while contador < colunas:
        print(acessamatriz[contador], end=" ")
        contador +=1
    print()
    contador = 0

print('\n\n\n')

#matriz com dicionario
dic = {}
linha = 4
coluna = 4
cont = 0
for posLinha in range(linha):
    for posColuna in range(coluna):
        x = "linha %i" %posLinha
        y = "coluna %i" %posColuna
        dic[posLinha, posColuna] = "%.2d" %cont
        cont +=1
        

''' imprimir a matriz dicionário style '''
cont = 0
for x in range(linha):
    for y in range(coluna):
        print(dic[x,y], end=" ")
        cont +=1
    cont = 0
    print()
