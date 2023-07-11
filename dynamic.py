import random


def qs(arr, k, l, r):
    if r == l:
        return arr[l]
    pivotChoice = dynamic(arr, k, l, r)
    p = partition(arr, pivotChoice, l, r)
    left_length = p-l
    if (left_length+1 == k):
        return arr[p]
    elif left_length+1 > k:
        return qs(arr, k, l, p-1)
    else:
        return qs(arr, k-left_length-1, p+1, r)


def partition(arr, pivot_idx, l, r):
    pivot_val = arr[pivot_idx]
    arr[pivot_idx], arr[l] = arr[l], arr[pivot_idx]
    idx = l+1
    for i in range(idx, r+1):
        if arr[i] < pivot_val:
            arr[i], arr[idx] = arr[idx], arr[i]
            idx += 1
    idx = idx-1
    arr[l], arr[idx] = arr[idx], arr[l]
    return idx


def dynamic(arr, k, l, r):
    if (r-l) > 3:
        numSample, lowerBound, upperBound = 3, .4, .6
        sampleArray = random.sample(range(l, r), numSample)
        sampleDict = {}
        for i in range(len(sampleArray)):
            sampleDict[arr[sampleArray[i]]] = sampleArray[i]
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
