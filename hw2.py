import numpy as np

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
    n = len(A)
    for i in range(n):
        for j in range(i-1, -1, -1):
            if A[j] > A[j+1]:
                A[j], A[j+1] = A[j+1], A[j]
            else: 
                break
    return A
        
def selectionsort(A):
    n = len(A)
    for j in range(n,1,-1):
        max_idx = 0
        for i in range(j):
            if A[i] > A[max_idx]:
                max_idx = i
        A[j-1], A[max_idx] = A[max_idx],A[j-1]
    return A

def is_sorted(A):
    for i in range(1, len(A)):
        if A[i-1] > A[i]:
            return False
    return True

def check_validity(func):
    for i in range(100, 401, 10):
        rand_nums = np.random.randint(5000, size=i)
        sorted_nums = func(rand_nums)
        if not is_sorted(sorted_nums):
            return False
    return True

print(check_validity(bubblesort))