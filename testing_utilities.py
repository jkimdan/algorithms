from sorting_algos import  *
import math

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

# creates a semi sorted list based on mess factor
def make_sorta_sorted(n, mess_factor):
    rng = np.random.default_rng()
    A = sorted(rng.integers(1,1000,n))
    percent = int((mess_factor * n) // 2)
    for i in range(percent):
        j_1, j_2 = rng.integers(0,n,2)
        A[j_1], A[j_2] = A[j_2], A[j_1]
    return A

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

def compare_worst(*algos, max_size=400, trials=100):
    worst_times = [[] for _ in algos]
    x_axis = list(range(10, max_size+1, 10))
    for idx, algo in enumerate(algos): 
        for i in range(10, max_size+1, 10):
            times = []
            for j in range(trials):
                rand_nums = np.random.randint(1000, size=i)
                t1_start = perf_counter()
                algo(list(rand_nums))
                t1_stop = perf_counter()
                times.append(t1_stop-t1_start)

            worst_times[idx].append(max(times))

    fig, ax = plt.subplots()
    for i, algo in enumerate(algos):
        ax.plot(x_axis, worst_times[i], label = f"{algo.__name__}")
    ax.set_title(f"Worst-Case comparison, trials={trials}")
    ax.set_xlabel("List size")
    ax.set_ylabel("Runtime in seconds")
    ax.legend()
    plt.show()

def compare_average(*algos, max_size=400, trials=100):
    average_times = [[] for _ in algos]
    x_axis = list(range(10, max_size+1, 10))
    for idx, algo in enumerate(algos): 
        for i in range(10, max_size+1, 10):
            times = []
            for j in range(trials):
                rand_nums = np.random.randint(1000, size=i)
                #sorta_sorted = make_sorta_sorted(i, 0.1)
                t1_start = perf_counter()
                algo(list(rand_nums))
                #algo(list(sorta_sorted))
                t1_stop = perf_counter()
                times.append(t1_stop-t1_start)

            average_times[idx].append(np.mean(times))

    fig, ax = plt.subplots()
    for i, algo in enumerate(algos):
        ax.plot(x_axis, average_times[i], label = f"{algo.__name__}")
    ax.set_title(f"Average runtime comparison, trials={trials}")
    ax.set_xlabel("List size")
    ax.set_ylabel("Runtime in seconds")
    ax.legend()
    plt.show()

def compare_best(*algos, max_size=400, trials=100):
    best_times = [[] for _ in algos]
    x_axis = list(range(10, max_size+1, 10))
    for idx, algo in enumerate(algos): 
        for i in range(10, max_size+1, 10):
            times = []
            for j in range(trials):
                sorta_sorted = make_sorta_sorted(i, 0.2)
                t1_start = perf_counter()
                algo(sorta_sorted)
                t1_stop = perf_counter()
                times.append(t1_stop-t1_start)

            best_times[idx].append(min(times))

    fig, ax = plt.subplots()
    for i, algo in enumerate(algos):
        ax.plot(x_axis, best_times[i], label = f"{algo.__name__}")
    ax.set_title(f"Best runtime comparison")
    ax.set_xlabel("List size")
    ax.set_ylabel("Runtime in seconds")
    ax.legend()
    plt.show()

def compare_with_theory(algo, theo, max_size=500, resolution=1):
    average_times = []
    x_axis = list(range(10, max_size+1, 10))
    theo_vals = [theo(n) for n in x_axis]
    for i in range(10, max_size+1, 10):
        trial_times = []
        for j in range(resolution):
            rand_nums = np.random.randint(1000,size=i)
            start = perf_counter()
            algo(list(rand_nums))
            stop = perf_counter()
            trial_times.append(stop - start)
        average_times.append(np.mean(trial_times))

    fix, ax = plt.subplots(1,2,figsize=(10,4)) 
    ax[0].set_title(f"{str(algo.__name__)} runtimes")
    ax[0].set_xlabel("Array size")
    ax[0].set_ylabel("Runtime in seconds")
    ax[0].plot(x_axis, average_times)
    ax[1].set_title("Theoretical big-O function:")
    ax[1].set_xlabel(f"Input size n")
    ax[1].plot(x_axis, theo_vals)
    plt.tight_layout()
    plt.show()
    
if __name__ == "__main__": 
    pass