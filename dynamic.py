import random


class Dynamic:
    def __init__(self, input_array):
        self.partitionIterations = 0
        self.arr = input_array

    def qs(self, k, l, r):
        if r == l:
            return self.arr[l]
        pivotChoice = self.dynamic(k, l, r)
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

    def dynamic(self, k, l, r):
        if (r-l) > 3:
            numSample, lowerBound, upperBound = 3, .4, .6
            sampleArray = random.sample(range(l, r), numSample)
            sampleDict = {}
            for i in range(len(sampleArray)):
                sampleDict[self.arr[sampleArray[i]]] = sampleArray[i]
            sortedDict = sorted(sampleDict.copy())
            percentage = k/float(r-l)
            if percentage < lowerBound:
                return sampleDict[sortedDict[0]]
            elif percentage > upperBound:
                return sampleDict[sortedDict[2]]
            else:
                return sampleDict[sortedDict[1]]
        else:
            return int(random.randint(l, r))
