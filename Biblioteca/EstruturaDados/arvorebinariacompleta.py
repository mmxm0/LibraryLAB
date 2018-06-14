class Nodo:

    def __init__(self,data,index):
        self.__data = data
        self.__father =None
        self.__lson = None
        self.__rson = None
        self.__id = index
        self.__height = 1

    def getHeight(self):
        return self.__height
    def setHeight(self):
        self.__height +=1

    def getIndex(self):
        return self.__id

    def getData(self):
        return self.__data
    def setData(self,data):
        self.__data = data

    def getFahter(self):
        return self.__father
    def setFather(self,father):
        self.__father = father

    def getLson(self):
        return self.__lson
    def setLson(self,lson):
        self.__lson = lson

    def getRson(self):
        return self.__rson
    def setRson(self,rson):
        self.__rson = rson

class Tree:

    def __init__(self,altura):
        self.__root = None
        self.__data = [None]*((2**altura)-1)

    def getData(self):
        return self.__data

    def getRoot(self):
        return self.__root
    def setRoot(self,root):
        self.__root = root

    def info(self,nodo):
        return nodo.getData()

    def left(self,nodo):
        return nodo.getLSon()

    def right(self,nodo):
        return nodo.getRSon()

    def father(self,nodo):
        return nodo.getFahter()

    def isleft(self,data):
        if data.getFater().getLSon() == data:
            return True
        else:
            return False

    def isRight(self,data):
        if self.isleft(data):
            return False
        else:
            return True

    def getBrother(self,data):
        father = data.getFather()
        if father.getLSon() == data:
            return father.getRson()
        else:
            return father.getLSon()

    def insert(self,data,index):
        aux = True
        nodo = Nodo(data,index)
        if self.getRoot() == None:
            self.setRoot(nodo)
            self.getData()[0] = nodo

        else:

            pivo = self.getRoot()
            indexList = 0
            while aux:
                if nodo.getIndex() >= pivo.getIndex():
                    if pivo.getLson() == None:
                        pivo.setLson(nodo)
                        aux = False
                        indexList = 2 * indexList + 2
                        self.getData()[indexList] = nodo
                        nodo.setHeight()
                    else:
                        indexList = 2*indexList +2
                        pivo = pivo.getLson()
                        nodo.setHeight()

                else:
                    if pivo.getRson() ==None:
                        pivo.setRson(nodo)
                        indexList = 2 * indexList + 1
                        self.getData()[indexList] = nodo
                        nodo.setHeight()
                        aux = False
                    else:
                        indexList = 2*indexList +1
                        pivo = pivo.getRson()
                        nodo.setHeight()

            if indexList > len(self.__data):
                return 0

    def search(self,index):
        indexList = 0
        while True:

            if self.__data[indexList].getIndex() == index:
                return indexList,self.__data+[indexList],self.__data[indexList].getHeight()

            elif self.__data[indexList].getIndex() > index:
                indexList = 2*indexList +1

            elif self.__data[indexList].getIndex() <= index:
                indexList = 2 * indexList + 2

            if indexList+1 > len(self.__data):
                return [0]

    def __str__(self):
        stri = ""
        for i in self.__data:
            stri += i.getData() + " "

        return stri[:-1]





string = ""
entrada = input()
entrada = entrada.split("!!!")
tamanho = entrada.pop(0)
arvore = Tree(int(tamanho))
for i in range(len(entrada)):
    entrada[i] = entrada[i].replace("'","")
    entrada[i] = entrada[i].replace("[","")
    entrada[i] = entrada[i].replace("]","")
    entrada[i] = entrada[i].replace("‘","")
    entrada[i] = entrada[i].replace("’","")
    entrada[i] = entrada[i].split(" ")




string = ""
for i in entrada:
    if len(i) >1:
        arvore.insert(i[1],int(i[0]))

    else:
        valor = arvore.search(int(i[0]))
        if len(valor) != 1:
            string += str(valor[2]) + " " + str(valor[0]) + "!!!"

        else:
            string += str(valor[0]) + "!!!"





print(string[:-3])

