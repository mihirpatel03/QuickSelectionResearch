def quickSelect(arr, k, l, r):
    # the largest/smallest element in an array of
    # length 1 (i.e. l==r), is that element itself.
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


unsorted = [22, 17, 11, 8, 21, 9, 7, 10, 12, 13]
kth = 5
print(quickSelect(unsorted, kth, 0, len(unsorted)-1))
