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

def partition(A, left_idx, right_idx):
# initial pivot target idx
    target_idx = left_idx
    # pivot value for comparison
    pivot_value = A[right_idx]
    # traverse the array and partition values 
    for i in range(left_idx, right_idx):
        if A[i] < pivot_value: 
            A[i], A[target_idx] = A[target_idx], A[i]
            target_idx += 1
    # place pivot into target position
    A[right_idx], A[target_idx] = A[target_idx], A[right_idx]
    return target_idx

def quicksort(A, left, right):
    # base case: continue until indices cross
    if left >= right:
        return A
    p = partition(A, left, right)
    # sort left side of p
    quicksort(A, left, p-1)
    #sort right side of p
    quicksort(A, p+1, right)

def quicksort_test(A):
    quicksort(A, 0, len(A) - 1)
    return A

def merge(A, B):
    if not A or not B:
        return A or B
    else:
        if A[0] >= B[0]:
            return B[0] + merge(A, B[1:])
        if A[0] < B[0]:
            return A[0] + merge(A[1:], B[1:])        

def mergesort(A):
    if len(A) > 1: 
        mid = len(A) // 2
        return merge(mergesort(A[:mid]), mergesort(A[mid:]))
    else:
        return A    

if __name__ == "__main__":
    pass
