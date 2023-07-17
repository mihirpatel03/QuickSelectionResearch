import random


class Default:
    def __init__(self, input_array):
        self.partitionIterations = 0
        self.arr = input_array

    def qs(self, k, l, r):
        if r == l:
            return self.arr[l]
        pivotChoice = int(random.randint(l, r))
        p = self.partition(pivotChoice, l, r)
        left_length = p-l
        if (left_length+1 == k):
            return self.arr[p]
        elif left_length+1 > k:
            return self.qs(k, l, p-1)
        else:
            return self.qs(k-left_length-1, p+1, r)

    def partition(self, pivot_idx, l, r):
        pivot_val = self.arr[pivot_idx]
        self.arr[pivot_idx], self.arr[l] = self.arr[l], self.arr[pivot_idx]
        idx = l+1
        for i in range(idx, r+1):
            self.partitionIterations += 1
            if self.arr[i] < pivot_val:
                self.arr[i], self.arr[idx] = self.arr[idx], self.arr[i]
                idx += 1
        idx = idx-1
        self.arr[l], self.arr[idx] = self.arr[idx], self.arr[l]
        return idx
