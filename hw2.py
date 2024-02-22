import numpy as np
import matplotlib.pyplot as plt
from time import perf_counter

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

# c. all of these algorithms are worst case O(n^2) because they are making element-to-element comparisons
# d. all of these algorithms are in place, they do not create extra memory.
def compare_times(*algos, max_size=400):
    all_times = []
    x_axis = list(range(10, max_size+1, 10))
    for algo in algos:
        algo_times = []
        for i in range(10, max_size+1, 10): 
            rand_nums = np.random.randint(1000, size=i)
            t1_start = perf_counter()
            algo(list(rand_nums))
            t1_stop = perf_counter()
            algo_times.append(t1_stop - t1_start)
        all_times.append(algo_times)

    fig, ax = plt.subplots()
    for i, algo in enumerate(algos):
        ax.plot(x_axis, all_times[i], label = f"{algo.__name__}")
    ax.set_title("Runtimes comparison")
    ax.set_xlabel("List size")
    ax.set_ylabel("Runtime in seconds")
    ax.legend()
    plt.show()

compare_times(bubblesort,insertionsort,selectionsort,max_size=2000)