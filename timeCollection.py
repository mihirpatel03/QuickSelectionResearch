
import random
import time
from default import Default
from dynamic import Dynamic
from floydRivest import FloydRivest

# if you want to check quickSelect's correctness by sorting the list and accessing its kth element, set this to true.
# Works for smaller values but too time consuming for larger values, so commented out when calculating the runtimes
verifyResults = False


def sampleTestArray(maxVal, numItems):
    # given the max possible value of an element, and the total number of elements the array should have,
    # generates an unsorted array of random, distinct values that meet these speciications.

    testArray = random.sample(range(0, maxVal), numItems)
    return testArray


def shuffleTestArray(maxVal, numItems):
    testArray = [i for i in range(maxVal)]
    print('generated array')
    random.shuffle(testArray)
    print("shuffled array")
    testArray = testArray[0:numItems]
    print("sliced array")
    return testArray


def avg(input_list):
    return sum(input_list)/len(input_list)


if __name__ == "__main__":

    max_value, array_size, numRuns = 100000000, 64000000, 1
    defaultTimes, dynamicTimes, fraTimes = [], [], []
    defaultOps, dynamicOps, fraOps = [], [], []
    for i in range(numRuns):
        print("starting run " + str(i) + " of " + str(numRuns))
        inp = sampleTestArray(max_value, array_size)
        kth = random.randint(1, len(inp)-1)

        print("starting default")
        x = inp[:]
        default = Default(x)
        print("done copying")
        start1 = time.time()
        defaultResult = default.qs(kth, 0, len(inp)-1)
        defaultTimes.append(time.time()-start1)
        defaultOps.append(default.partitionIterations)

        print("starting dynamic")
        y = inp[:]
        dynamic = Dynamic(y, .4, .6)
        print("done copying")
        start2 = time.time()
        dynamicResult = dynamic.qs(kth, 0, len(inp)-1)
        dynamicTimes.append(time.time()-start2)
        dynamicOps.append(dynamic.partitionIterations)

        print("starting fra")
        floydRivest = FloydRivest(inp)
        start3 = time.time()
        fraResult = floydRivest.select(kth-1, 0, len(inp)-1)
        fraTimes.append(time.time()-start3)

        if (verifyResults):
            sorted_array = sorted(inp)
            correctVal = sorted_array[kth-1]
            assert correctVal == defaultResult == dynamicResult == fraResult

    print("for list size " + str(array_size) + "...")
    print("\n TIMES \n")
    print("Default takes on average " + str(avg(defaultTimes)) +
          ", here are each of the times: ", defaultTimes)
    print("Dynamic takes on average " + str(avg(dynamicTimes)) +
          ", here are each of the times: ", dynamicTimes)
    print("Floyd-Rivest takes on average " + str(avg(fraTimes)) +
          ", here are each of the times: ", fraTimes)
    print("\n OPERATIONS \n")
    print("Default takes on average " + str(avg(defaultOps)) +
          ", here are each of the operations: ", defaultOps)
    print("Dynamic takes on average " + str(avg(dynamicOps)) +
          ", here are each of the operations: ", dynamicOps)
