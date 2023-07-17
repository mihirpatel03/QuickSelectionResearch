
import random
import time
from default import Default
from dynamic import Dynamic
from floydRivest import FloydRivest

# if you want to check quickSelect's correctness by sorting the list and accessing its kth element, set this to true.
# Works for smaller values but too time consuming for larger values, so commented out when calculating the runtimes
verifyResults = False


def createTestArray(maxVal, numItems):
    # given the max possible value of an element, and the total number of elements the array should have,
    # generates an unsorted array of random, distinct values that meet these speciications.

    testArray = random.sample(range(0, maxVal), numItems)
    return testArray


def avg(input_list):
    return sum(input_list)/len(input_list)


if __name__ == "__main__":

    max_value, array_size, numRuns = 100000000, 500000, 5
    defaultTimes, dynamicTimes, fraTimes = [], [], []
    defaultOps, dynamicOps, fraOps = [], [], []
    for i in range(numRuns):
        inp = createTestArray(max_value, array_size)
        kth = random.randint(1, len(inp)-1)

        default = Default(inp[:])
        start = time.time()
        defaultResult = default.qs(kth, 0, len(inp)-1)
        defaultTimes.append(time.time()-start)
        defaultOps.append(default.partitionIterations)

        dynamic = Dynamic(inp[:])
        start = time.time()
        dynamicResult = dynamic.qs(kth, 0, len(inp)-1)
        dynamicTimes.append(time.time()-start)
        dynamicOps.append(dynamic.partitionIterations)

        floydRivest = FloydRivest(inp)
        start = time.time()
        fraResult = floydRivest.select(kth-1, 0, len(inp)-1)
        fraTimes.append(time.time()-start)

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
