class Pilha():
    def __init__(self):
        self.dados = []

    def empilha(self, elemento):
        self.dados.append(elemento)

    def desempilha(self):
        if not self.vazia():
            return self.dados.pop(-1)

    def vazia(self):
        return len(self.dados) == 0

    def mostrarPilha(self):
        return self.dados

listaDeResultados = []

while True:
    try:
        linhaDeElementos = input().split()
        pilha = Pilha()
        for elemento in linhaDeElementos[::-1]:
            if (elemento != "+" and elemento != "-" and elemento != "*" and elemento != "/"):
                pilha.empilha(int(elemento))
            if (elemento == "+" or elemento == "-" or elemento == "*" or elemento == "/"):
                if (elemento == "+"):
                    num1 = pilha.desempilha()
                    num2 = pilha.desempilha()
                    soma = num1 + num2
                    pilha.empilha(soma)
                elif (elemento == "-"):
                    num1 = pilha.desempilha()
                    num2 = pilha.desempilha()
                    subtracao = num1 - num2
                    pilha.empilha(subtracao)
                elif (elemento == "*"):
                    num1 = pilha.desempilha()
                    num2 = pilha.desempilha()
                    multiplicacao = num1 * num2
                    pilha.empilha(multiplicacao)
                elif (elemento == "/"):
                    num1 = pilha.desempilha()
                    num2 = pilha.desempilha()
                    divisao = num1 / num2
                    pilha.empilha(int(divisao))
        listaDeResultados.append(pilha.mostrarPilha())
    except:
        break

saida = ""
for listaResultado in listaDeResultados:
    for resultado in listaResultado:
        saida += str(resultado) + "\n"
print(saida)