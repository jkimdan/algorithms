from sorting_algos import  *

if __name__ == "__main__": 
    compare_times(bubblesort, selectionsort, insertionsort, max_size=500)
    compare_worst(bubblesort, selectionsort, insertionsort, max_size=400, trials=100)
    compare_average(bubblesort, selectionsort, insertionsort, max_size=400, trials=100)
    compare_best(bubblesort, insertionsort, selectionsort, max_size=400, trials=100)   
    compare_with_theory(insertionsort, lambda n: n*n , resolution=10)