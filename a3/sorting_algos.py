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

# array A has n unique integers
def find_pairs_bf(A):
    pair_count = 0
    for val in A:
        for val2 in A: 
            if val ** 2 == val2:
                pair_count += 1
    return pair_count

def find_pairs_2pointer(A):
    sorted_nums = quicksort_test(A)
    pointer = 0
    pointer2 = 1
    count = 0
    while pointer2 < len(sorted_nums):
        sqr = sorted_nums[pointer] ** 2
        if sqr == sorted_nums[pointer2]:
            count += 1
            pointer += 1
        elif sqr < sorted_nums[pointer2]:
            pointer += 1
        else: 
            pointer2 += 1

    return count

def find_majority_bf(A):
    for i in A:
        count = 0
        for j in A:
            if i == j:
                count += 1
        if len(A) / 2 < count: 
            return i
    return -1

def count_majority(A, element):
    count = 0
    for val in A:
        if val == element:
            count += 1
    return count

def find_majority_dnc(A):
    # base case
    if len(A) == 1:
        return A[0]
    
    # find the majority of the left and right sides
    middle = len(A) // 2
    left = find_majority_dnc(A[:middle])
    right = find_majority_dnc(A[middle:])

    # if the left and the right side majority are the same,
    # then the majority is the found value
    if left == right:
        return left
    
    # if not, must determine which majority occurs more, meaning
    # the majority for the combined sides is the majority with more
    # occurrences. This occurs in O(n) time.
    left_count = count_majority(A, left)
    right_count = count_majority(A, right)

    if left_count > middle:
        return left
    elif right_count > middle:
        return right
    else: 
        return -1

if __name__ == "__main__":
    pass
