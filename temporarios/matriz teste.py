matriz = []
linhas = int(input())
colunas = int(input())
x = 0
for i in range(linhas):
    lista = []
    while len(lista)<colunas:
        lista.append(x)
        x+=1
    matriz.append(lista)
contador = 0
for linha in matriz:
    while contador < colunas:
        print(str(linha[contador]).rjust(len(str(linhas*colunas)),"0"), end=" ")
        contador +=1
    contador =0
    print()
