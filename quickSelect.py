import random


def qs(arr, k, l, r, pc):
    # given an array, a value k, and left and right indices, will return the kth smallest value
    # in that array between those two indices

    # the largest/smallest element in an array of length 1 (i.e. l==r), is that element itself
    if r == l:
        return arr[l]
    # partition the array around the randomly chose pivot

    p = eval(pc)(arr, k, l, r)

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
        return qs(arr, k, l, p-1, pc)

    # CASE 3: recur on the right side. e.g., if we were looking for the 5th smallest element in an array
    # of size 8, and the pivot was at index 3 (3 elements to its left), we are now looking for the 1st
    # smallest element in the right subarray, of length 4.
    else:
        print("now recurring on a subarray of length " + str(r-(p+1)))
        return qs(arr, k-left_length-1, p+1, r, pc)


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


def default(arr, k, l, r):
    # print(l, r)
    pivotChoice = int(random.randint(l, r))
    return partition(arr, pivotChoice, l, r)


# def probabilistic(arr, k, l, r):
#     lowBound = 1/4.0
#     highBound = 3/4.0

#     pivotChoice = int(random.randint(l, r))
#     #can duplicate outside
#     test_arr = arr.copy()
#     p = partition(arr, pivotChoice, l, r)

#     # need to randomize pivot selection
#     while p < int(lowBound*(r-l))+l or p > int(highBound*(r-l))+l:
#         pivotChoice = int(random.randint(l, r))
#         arr = test_arr
#         p = partition(arr, pivotChoice, l, r)

#     return p


def deterministic():
    return


def dynamic(arr, k, l, r):
    if (r-l) > 3:
        numSample = 3
        sampleDict = dict()

        # dictionary where the keys are values within the array, values are the corresponding indices
        while len(sampleDict) < numSample:
            pivotChoice = int(random.randint(l, r))
            if arr[pivotChoice] not in sampleDict:
                sampleDict[arr[pivotChoice]] = pivotChoice
        assert (len(sampleDict) == 3)
        sortedDict = sorted(sampleDict.copy())

        percentage = k/float(r-l)
        if percentage < .4:
            return partition(arr, sampleDict[sortedDict[0]], l, r)
        elif percentage > .6:
            return partition(arr, sampleDict[sortedDict[2]], l, r)
        else:
            return partition(arr, sampleDict[sortedDict[1]], l, r)
    else:
        # print(l, r)
        pivotChoice = int(random.randint(l, r))
        return partition(arr, pivotChoice, l, r)
