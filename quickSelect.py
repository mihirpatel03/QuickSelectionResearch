import random


def qs(arr, k, l, r, pc):
    # given an array, a value k, and left and right indices, will return the kth smallest value
    # in that array between those two indices

    # the largest/smallest element in an array of length 1 (i.e. l==r), is that element itself
    if r == l:
        return arr[l]

    # call a pivot choosing method (these methods also perform the partition)
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
    # default quick select simply picks a random element (by way of its index), and then we partition
    pivotChoice = int(random.randint(l, r))
    return partition(arr, pivotChoice, l, r)


def dynamic(arr, k, l, r):
    # if the length of the current list is greater than 3, use the dynamic approach (otherwise just default)
    if (r-l) > 3:
        # number of elements we want for our sample
        numSample = 3
        # and the bounds we will use to pick which element we use
        lowerBound = .4
        upperBound = .6

        # dictionary to store these sampled values
        sampleDict = dict()

        # dictionary where the keys are the array's values, and values are the array's indices
        while len(sampleDict) < numSample:  # while we don't yet have numSample numbers
            # pick a random index
            pivotChoice = int(random.randint(l, r))
            # if that index's corresponding value is not yet a key in our dict
            if arr[pivotChoice] not in sampleDict:
                # make the value the key and the index the value
                sampleDict[arr[pivotChoice]] = pivotChoice
        # we should have 3 keys (array values) after this is done
        assert (len(sampleDict) == 3)
        # duplicate the dict and then sort it (now we have a list of sorted array values, and we can access their
        # corresponding indices using our dict)
        sortedDict = sorted(sampleDict.copy())

        # calculate the percentage/ratio of k to the length of the array
        percentage = k/float(r-l)
        # if below the lower bound, return the smallest sample
        if percentage < lowerBound:
            return partition(arr, sampleDict[sortedDict[0]], l, r)
        # if above the upper bound, return the largest sample
        elif percentage > upperBound:
            return partition(arr, sampleDict[sortedDict[2]], l, r)
        # otherwise we are in between the bounds, so return the middle sample
        else:
            return partition(arr, sampleDict[sortedDict[1]], l, r)
    # (we are below a length of 3, so do not need this method, just pick a random index)
    else:
        pivotChoice = int(random.randint(l, r))
        return partition(arr, pivotChoice, l, r)
