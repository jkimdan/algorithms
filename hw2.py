def bubblesort(A):
    n = len(A)
    for i in range(n):
        swapped = False
        for j in range(0,n-i-1):
            if A[j] > A[j+1]:
                A[j],A[j+1] = A[j+1],A[j]
                swapped = True
            if swapped == False: break
    return A

def insertionsort(A):
    pass

def selectionsort(A):
    pass
