import csv
import random
import time
import math


def quickSelect(arr, k, l, r):
    # the largest/smallest element in an array of
    # length 1 (i.e. l==r), is that element itself
    if l == r:
        return arr[l]
    # partition the array around the pivot (by default the
    # pivot is the rightmost element in the array) should still
    # work for other pivot choices, such as l, or (l+r)//2
    p = partition(arr, r, l, r)
    # length of the (sub)array from left to pivot after partition
    left_length = p-l
    # e.g., if there are 3 elements to the left of the pivot, and
    # we are looking for the 4th smallest element, then the pivot
    # is itself the 4th smallest element
    if (left_length+1 == k):
        return arr[p]
    # e.g., if there are 3 elements to the left of the pivot
    # and we are looking for the second smallest element, we
    # know it must be in that subarray to the left of the pivot
    elif left_length+1 > k:
        return quickSelect(arr, k, l, p-1)
    # otherwise, the kth smallest element is in the right
    # subarray. If we were looking for the 5th smallest element
    # in an array of size 8, and the pivot was at index 3
    # (3 elements to its left), we are now looking for the 1st
    # smallest element in the right subarray, of length 4.
    else:
        return quickSelect(arr, k-left_length-1, p+1, r)


def partition(arr, pivot_idx, l, r):
    # store the value of the pivot
    pivot_val = arr[pivot_idx]
    # now move the pivot to the leftmost spot in the (sub)array
    arr[pivot_idx], arr[l] = arr[l], arr[pivot_idx]
    # starting index is one more than the reserved pivot spot
    idx = l+1
    for i in range(idx, r+1):
        # if we encounter a value smaller than the pivot
        if arr[i] < pivot_val:
            # swap it with the current pivot location
            # (so it is now left of the pivot location)
            arr[i], arr[idx] = arr[idx], arr[i]
            # increment the pivot location
            idx += 1
    # decrement the index (which should have been out of bounds)
    idx = idx-1
    # swap the pivot to the location it should be post-partition
    arr[l], arr[idx] = arr[idx], arr[l]
    # return the pivot's location
    return idx


# unsorted = [22, 17, 11, 8, 21, 9, 7, 10, 12, 13]
# kth = 5
# print(quickSelect(unsorted, kth, 0, len(unsorted)-1))

# 100k to 10M size lists, random input testing.

def createTestArray(maxVal, numItems):
    testArray = random.sample(range(0, maxVal), numItems)
    return testArray


def get_time_taken_by_quick_select(input_list):
    times = []
    last_idx = len(input_list)-1
    kth = random.randint(0, last_idx)
    for i in range(10):
        print("here")
        start = time.time()
        quickSelect(input_list, kth, 0, last_idx)
        elapsed_time_lc = (time.time() - start)
        times.append(elapsed_time_lc)

    # return average time
    return sum(times)/len(times)


MAX = 100000000
minItems = 100000
maxItems = 10000000
time_dict = dict()

for i in range(0, 10):
    list_size = int(random.randint(minItems, maxItems))
    input_list = createTestArray(MAX, list_size)
    time_taken = get_time_taken_by_quick_select(input_list)
    time_dict[list_size] = time_taken

print(time_dict)
# # save data to a CSV file, based on an example from
# # https://www.tutorialspoint.com/How-to-save-a-Python-Dictionary-to-CSV-file
# with open('complexity.csv', 'w') as f:
#     for key in time_dict.keys():
#         f.write("%s,%s\n" % (key, time_dict[key]))
