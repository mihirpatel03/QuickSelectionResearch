import csv
import random
import time


def quickSelect(arr, k, l, r):
    # given an array, a value k, and left and right indices, will return the kth smallest value
    # in that array between those two indices

    # the largest/smallest element in an array of length 1 (i.e. l==r), is that element itself
    if r == l:
        return arr[l]
    # partition the array around the pivot (by default the pivot is the rightmost element in the array)
    # should still work for other pivot choices, such as l, or (l+r)//2
    p = partition(arr, (l+r)//2, l, r)
    # length of the (sub)array from left to pivot after partition
    left_length = p-l

    # CASE 1: return the pivot itself. e.g., if there are 3 elements to the left of the pivot, and we
    # are looking for the 4th smallest element, then the pivot is itself the 4th smallest element
    if (left_length+1 == k):
        return arr[p]

    # CASE 2: recur on the left side. e.g., if there are 3 elements to the left of the pivot and we are
    # looking for the second smallest element, we know it must be in that subarray to the left of the pivot
    elif left_length+1 > k:
        print("now recurring on a subarray of length " + str(p-1-l))
        return quickSelect(arr, k, l, p-1)

    # CASE 3: recur on the right side. e.g., if we were looking for the 5th smallest element in an array
    # of size 8, and the pivot was at index 3 (3 elements to its left), we are now looking for the 1st
    # smallest element in the right subarray, of length 4.
    else:
        print("now recurring on a subarray of length " + str(r-(p+1)))
        return quickSelect(arr, k-left_length-1, p+1, r)


def partition(arr, pivot_idx, l, r):
    # given an array, the index of the chosen pivot, and left and right indices, will put all values less
    # than the pivot in between the left index and the pivot, and all values greater than the pivot in
    # between the pivot and the right index, returning the new index of the pivot after this partitioning

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


def createTestArray(maxVal, numItems):
    # given the max possible value of an element, and the total number of elements the array should have,
    # generates an unsorted array of random, distinct values that meet these speciications.

    testArray = random.sample(range(0, maxVal), numItems)
    return testArray


def timeTaken(input_array, current_point, total_points):
    # given an array, will return the average time it takes to run quickselect on that array (with random k)

    times = []
    last_idx = len(input_array)-1
    # randomizing the number we are looking for
    kth = random.randint(0, last_idx)
    # average of numRuns number of runs
    numRuns = 10
    for i in range(numRuns):
        start = time.time()
        # running quickSelect
        quickSelect(input_array, kth, 0, last_idx)
        elapsed_time = (time.time() - start)
        times.append(elapsed_time)
        print("\n done with " + str(i+1) +
              " run(s) out of " + str(numRuns) + " for data point " + str(current_point+1) + " out of " + str(total_points) + "\n")

    # return average time
    return sum(times)/len(times)


def main():  # main body code
    # max value of an element in our arrays (10 million)
    max_value = 10000000
    # minimum 100k items in an array
    minItems = 100000
    # maximum 10 million items in an array
    maxItems = 10000000
    # dictionary that will store times
    time_dict = dict()

    # generates i data points (i array sizes between 10k and 100 million)
    # consider adding a way to get i distinct data points?
    numDataPoints = 40
    for i in range(0, numDataPoints):
        # randomizing the size
        array_size = int(random.randint(minItems, maxItems))
        print("array size is " + str(array_size))
        # generating the random array
        input_array = createTestArray(max_value, array_size)
        # getting the average time it takes to run quick select on this array for random k
        print("beginning quickselect")
        avg_time_taken = timeTaken(input_array, i, numDataPoints)
        # storing that in the dictionary
        time_dict[array_size] = avg_time_taken

    print(time_dict)
    # save data to a CSV file
    with open('complexity.csv', 'w') as f:
        for key in time_dict.keys():
            f.write("%s,%s\n" % (key, time_dict[key]))


if __name__ == "__main__":
    main()
