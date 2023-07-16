import random
import timeCollection


def qs(arr, k, l, r):
    if r == l:
        return arr[l]
    pivotChoice = int(random.randint(l, r))
    p = partition(arr, pivotChoice, l, r)
    left_length = p-l
    if (left_length+1 == k):
        return arr[p]
    elif left_length+1 > k:
        return qs(arr, k, l, p-1)
    else:
        return qs(arr, k-left_length-1, p+1, r)


def partition(arr, pivot_idx, l, r):
    pivot_val = arr[pivot_idx]
    arr[pivot_idx], arr[l] = arr[l], arr[pivot_idx]
    idx = l+1
    for i in range(idx, r+1):
        timeCollection.partitionIterations += 1
        if arr[i] < pivot_val:
            arr[i], arr[idx] = arr[idx], arr[i]
            idx += 1
    idx = idx-1
    arr[l], arr[idx] = arr[idx], arr[l]
    return idx
