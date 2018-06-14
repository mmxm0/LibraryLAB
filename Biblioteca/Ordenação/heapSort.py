def maxheapfy(A, i):
    tamanho = len(A)
    l = i + 1
    r = i + 2
    if l <= tamanho and A[l] > A[i]:
        maior = l
    else:
        maior = i
    if r <= tamanho and A[r] > A[maior]:
        maior = r
    if maior != i:
        A[i], A[maior] = A[maior], A[i]
        maxheapfy(A, maior)

def buildmaxheap(A):
    tamanho = len(A)
    for i in range(int(tamanho / 2)):
        maxheapfy(A, i)