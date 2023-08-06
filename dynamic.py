import random


class Dynamic:
    def __init__(self, input_array, bounds, findConstant):
        self.bounds = bounds  # list of the bounds we should use as cutoffs
        self.partitionIterations = 0  # counting variable for total partition iterations
        # boolean for if we should be tracking the reduction constant
        self.findConstant = findConstant
        self.constantsList = []  # if so, the list that will accumulate the reduction sizes
        self.arr = input_array  # input array we should run qs on

    def qs(self, k, l, r):
        # return the only element if list size is 1
        if r == l:
            return self.arr[l]
        # choose a pivot using our dynamic strategy
        pivotChoice = self.dynamic(k, l, r)
        # partition around that pivot
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

    def dynamic(self, k, l, r):
        # given the value of k and left and right indices, will select a pivot
        # if we have more elements than the number of bounds, use dyanmic
        if (r-l) > len(self.bounds)+1:
            # randomly sample the amount of values necessary (1 more than number of bounds)
            sampleArray = random.sample(range(l, r), len(self.bounds)+1)
            sampleDict = {}
            # for each of the sampled indices...
            # the key in the dictionary will be that index's corresponding value
            # the value in the dictionary will be that index
            for i in range(len(sampleArray)):
                sampleDict[self.arr[sampleArray[i]]] = sampleArray[i]
            # sort the keys in the dictionary from least to greatest
            sortedDict = sorted(sampleDict.copy())
            # calculate the ratio of k/n
            percentage = k/float(r-l+1)
            # if the ratio is less than the a certain bound (or within a range after the first iteration)
            for i in range(len(self.bounds)):
                if percentage < self.bounds[i]:
                    # return the corresponding potential pivot index stored in the dictionary
                    return sampleDict[sortedDict[i]]
            # return the greatest pivot value if k/n is greater than all specified bounds
            return sampleDict[sortedDict[-1]]
        # else we do not have enough elements to use dynamic, so just return a random index for pivot
        else:
            return int(random.randint(l, r))
