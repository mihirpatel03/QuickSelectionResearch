import random


class Default:
    def __init__(self, input_array, findConstant):
        self.partitionIterations = 0  # counting variable for total partition iterations
        # boolean for if we should be tracking the reduction constant
        self.findConstant = findConstant
        self.constantsList = []  # if so, the list that will accumulate the reduction sizes
        self.arr = input_array  # input array we should run qs on

    def qs(self, k, l, r):
        # if only one element, return that element
        if r == l:
            return self.arr[l]
        # randomly choose an element as the pivot
        pivotChoice = int(random.randint(l, r))
        # partition the array around that element
        p = self.partition(pivotChoice, l, r)
        left_length = p-l

        # if number of items to the left of the pivot = k, the pivot is the kth order statistic
        if (left_length+1 == k):
            return self.arr[p]
        # if greater than k, then the kth order statistic is to the left of the pivot
        elif left_length+1 > k:
            # track the reduction constant
            if self.findConstant:
                constant = (p-1-l)/(r-l)
                self.constantsList.append(constant)
            # recurse on the left subarray
            return self.qs(k, l, p-1)
        # otherwise the kth order statistic is to the right of the pivot
        else:
            # track the reduction constant
            if self.findConstant:
                constant = (r-p-1)/(r-l)
                self.constantsList.append(constant)
            # recurse on the right subarray
            return self.qs(k-left_length-1, p+1, r)

    def partition(self, pivot_idx, l, r):
        # given a value as pivot, rearrange the array such that all values less than
        # the pivot are to the left of the pivot, all greater values to the right
        pivot_val = self.arr[pivot_idx]
        # swap the leftmost value and our pivot
        self.arr[pivot_idx], self.arr[l] = self.arr[l], self.arr[pivot_idx]
        idx = l+1
        for i in range(idx, r+1):
            # increment total partition iterations
            self.partitionIterations += 1
            # if a value is less than the pivot value
            if self.arr[i] < pivot_val:
                # swap the value with the current element at idx (variable tracking the pivot location at the end)
                self.arr[i], self.arr[idx] = self.arr[idx], self.arr[i]
                idx += 1
        idx = idx-1
        # swap the pivot value back to where it should be (tracked by variable idx)
        self.arr[l], self.arr[idx] = self.arr[idx], self.arr[l]
        # return the pivot's index after partitioning
        return idx
