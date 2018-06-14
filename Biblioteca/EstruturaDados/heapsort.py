class HeapSort:

    def __init__(self,array=[]):
        self.__array = array
        self.__comprimento = len(array)-1
        self.__leastParent = (self.__comprimento)//2

    def getArray(self):
        return self.__array

    def getComprimento(self):
        return self._comprimento

    def getLeastParent(self):
        return self.__leastParent

    def setArray(self,novoarray):
        self.__array = novoarray
        self.__comprimento = len(novoarray)-1
        self.__leastParent = (len(novoarray)-1)//2

    def heapSort(self):
        for i in range(self.__leastParent,-1,-1):
            self.moveDown(i, self.__comprimento)

        for j in range(self.__comprimento,0,-1):
            if self.__array[0]>self.__array[i]:
                self.swap(0,j-1)

    def moveDown(self, primeiro, ultimo):
        maior = 2* primeiro + 1
        while maior <= ultimo:
            if(maior<ultimo)and(self.__array[maior]<self.__array[maior+1]):
                maior+=1
            if self.__array[maior]>self.__array[primeiro]:
                self.swap(maior,primeiro)
            else:
                return
    def swap(self,x,y):
        tmp = self.__array[x]
        self.__array[x]=self.__array[y]
        self.__array[y]=tmp



lista = [4,1,0,56,32,49,48,3,9,2,17]
novoheap = HeapSort(lista)
novoheap.heapSort()
