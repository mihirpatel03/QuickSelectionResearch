import random


class Dynamic:
    def __init__(self, input_array, lo, hi):
        self.partitionIterations = 0
        self.findConstant = True
        self.constantsList = []
        self.arr = input_array
        self.lowerBound = lo
        self.upperBound = hi

    def qs(self, k, l, r):
        if r == l:
            return self.arr[l]
        pivotChoice = self.dynamic(k, l, r)
        p = self.partition(pivotChoice, l, r)
        left_length = p-l
        if (left_length+1 == k):
            return self.arr[p]
        elif left_length+1 > k:
            if self.findConstant:
                constant = (p-1-l)/(r-l)
                # percent = constant*100
                # print("now recurring on a subarray that is " +
                #       str(percent) + "% of the original array's size")
                self.constantsList.append(constant)
            return self.qs(k, l, p-1)
        else:
            if self.findConstant:
                constant = (r-p-1)/(r-l)
                # percent = constant*100
                # print("now recurring on a subarray that is " +
                #       str(percent) + "% of the original array's size")
                self.constantsList.append(constant)
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
            numSample = 3
            sampleArray = random.sample(range(l, r), numSample)
            sampleDict = {}
            for i in range(len(sampleArray)):
                sampleDict[self.arr[sampleArray[i]]] = sampleArray[i]
            sortedDict = sorted(sampleDict.copy())
            percentage = k/float(r-l)
            if percentage < self.lowerBound:
                return sampleDict[sortedDict[1]]
            elif percentage > self.upperBound:
                return sampleDict[sortedDict[2]]
            else:
                return sampleDict[sortedDict[1]]
        else:
            return int(random.randint(l, r))
