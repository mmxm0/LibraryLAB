class NodeTree:
    def __init__(self, key, data=None):
        self.__key = key
        self.__data = data
        self.__father = None
        self.__left = None
        self.__right = None

    def getKey(self):
        return self.__key

    def getData(self):
        return self.__data

    def getFather(self):
        return self.__father

    def getLeft(self):
        return self.__left

    def getRight(self):
        return self.__right

    def setKey(self, key):
        self.__key = key

    def setData(self, data):
        self.__data = data

    def setFather(self, node):
        self.__father = node

    def setLeft(self, node):
        self.__left = node

    def setRight(self, node):
        self.__right = node

    def __str__(self):
        return str(self.getData())

class BinaryTree:
    def __init__(self):
        self.__root = None
        self.__length = 0
        self.__txt = ''

    def getroot(self):
        return self.__root

    def __len__(self):
        return self.__length

    def __str__(self, root='DEFAULT'):
        if (root == 'DEFAULT'):
            self.__txt = ''
            root = self.__root
            if (root == None):
                return 'Árvore Vazia.'
        if (root != None):
            self.__str__(root.getLeft())
            self.__txt += str(root.getKey()) + ', '
            self.__str__(root.getRight())

        return '[' + self.__txt[:-2] + ']'

    def insert(self, key, data=None):
        node = NodeTree(key, data)

        if (self.__root == None):
            self.__root = node
            self.__length += 1
        else:
            x = self.__root
            y = None

            while x != None:
                if (key <= x.getKey()):
                    x, y = x.getLeft(), x
                elif (key > x.getKey()):
                    x, y = x.getRight(), x


            node.setFather(y)
            self.__length += 1
            if (key <= y.getKey()):
                y.setLeft(node)
            else:
                y.setRight(node)

    def search(self, key):
        root = self.__root

        while root != None and key != root.getKey():

            if (key < root.getKey()):
                root = root.getLeft()

            else:
                root = root.getRight()

        return root
    def delete(self, key):
        z = self.search(key)

        if (z == None):
            print('Elemento não pertence a árvore.')
            return z

        if z.getLeft() == None or z.getRight() == None:
            y = z
        else:
            y = self.search(self.successor(z))

        if (y.getLeft() != None):

            x = y.getLeft()
        else:
            x = y.getRight()

        if (x != None):
            x.setFather(y.getFather())

        if (y.getFather() == None):
            self.__root = x
        else:
            if (y == y.getFather().getLeft()):
                y.getFather().setLeft(x)
            else:
                y.getFather().setRight(x)

        if (y != z):
            z.setKey(y.getKey())
            z.setData(y.getData())

        self.__length -= 1
        return y

    def mini(self, root='DEFAULT'):
        if (root == 'DEFAULT'):
            root = self.__root
            if (root == None):
                return 'Árvore Vazia.'

        while 1:
            if (root.getLeft() != None):
                root = root.getLeft()
            else:
                return root.getKey()


    def maxi(self,key, root='DEFAULT'):
        if (root == 'DEFAULT'):
            root = self.__root

            if (root == None):
                return 0

        while 1:

            if (root.getRight() != None):
                y = root.getRight()
                if y.getKey() > root.getKey():
                    return root
                root = root.getRight()
            else:
                return root

    def successor(self, root='DEFAULT'):
        if (root == 'DEFAULT'):
            root = self.__root
            if (root == None):
                return 'Árvore Vazia.'

        if (root.getRight() != None):
            return self.mini(root.getRight())

        dad = root.getFather()
        while (dad != None):
            if (root == dad.getLeft()):
                break
            root = dad
            dad = dad.getFather()

        return dad

    def predecessor(self, root='DEFAULT'):
        if (root == 'DEFAULT'):
            root = self.__root
            if (root == None):
                return 'Árvore Vazia.'

        if (root.getLeft() != None):
            return self.maxi(root.getRight())

        dad = root.getFather()
        while (dad != None):
            if (root == dad.getRight()):
                break
            root = dad
            dad = dad.getFather()

        return dad

    def preordem(self, root, lista):
        if root != None:
            lista.append(str(root.getKey()))
            self.preordem((root.getLeft()), lista)
            self.preordem((root.getRight()), lista)
        return lista

    def inor(self, root, lista):
        if root != None:
            self.inor(root.getLeft(), lista)
            lista.append(str(root.getKey()))
            self.inor(root.getRight(), lista)
        return lista

    def posordem(self, root, lista):
        if root != None:
            self.posordem(root.getLeft(), lista)
            self.posordem(root.getRight(), lista)
            lista.append(str(root.getKey()))
        return lista



entrada = input().split(" ")    #input().split(" ")
tree = BinaryTree()
string = ""
for i in range(len(entrada)):
    if entrada[i] == "I":
        tree.insert(int(entrada[i+1]),int(entrada[i+1]))
    elif entrada[i] == "R":
        tree.delete(int(entrada[i+1]))
    elif entrada[i] == "Q":
        if tree.mini() == int(entrada[i+1]):
            string += "0; "

        string+= str(tree.search(int(entrada[i+1]))) + "; "

    elif entrada[i] == "PRE":
        if tree.getroot() == None:
            string += "0; "
        else:
            lista = []
            lista = tree.preordem(tree.getroot(),lista)
            for i in range(len(lista)):
                if i+1 == len(lista):
                    string += lista[i]
                else:
                    string += lista[i] + " "
            string += "; "

    elif entrada[i] == "IN":
        if tree.getroot() == None:
            string += "0; "
        else:
            lista = []
            lista = tree.inor(tree.getroot(),lista)
            for i in range(len(lista)):
                if i+1 == len(lista):
                    string += lista[i]
                else:
                    string += lista[i] + " "
            string += "; "

    elif entrada[i] == "POST":
        if tree.getroot() == None:
            string += "0; "
        else:
            lista = []
            lista = tree.posordem(tree.getroot(),lista)
            for i in range(len(lista)):
                if i+1 == len(lista):
                    string += lista[i]
                else:
                    string += lista[i] + " "
            string += "; "

print(string[:-2] + ';')

