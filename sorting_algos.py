import numpy as np
import matplotlib.pyplot as plt
from time import perf_counter
from math import log, sqrt
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
    for i in range(1, n):
        key = A[i]
        j = i-1
        while j >=0 and key < A[j]:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
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

if __name__ == "__main__":
    pass
