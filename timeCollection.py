
import random
import time
from default import Default
from dynamic import Dynamic
from floydRivest import FloydRivest

# if you want to check quickSelect's (default, dynamic and F-R) correctness by sorting the list and accessing its kth element, set this to true.
# Works for smaller values but too time consuming for larger values, so commented out when calculating the runtimes
verifyResults = False


def sampleTestArray(maxVal, numItems):
    # generates an unsorted array of numItems length, with random and distinct elements
    testArray = random.sample(range(0, maxVal), numItems)
    return testArray


def avg(input_list):
    # returns average value of an array
    return sum(input_list)/len(input_list)


if __name__ == "__main__":
    max_value, array_size, numRuns = 64000000, 1000000, 5
    defaultTimes, dynamicTimes, fraTimes = [], [], []
    defaultOps, dynamicOps, fraOps = [], [], []
    for i in range(numRuns):
        print("starting run " + str(i+1) + " of " + str(numRuns))
        # generate random array and also random k
        inp = sampleTestArray(max_value, array_size)
        kth = random.randint(1, len(inp)-1)

        print("starting default")
        default = Default(inp[:], False)
        print("done copying list")
        # start timing default, then run
        start = time.time()
        defaultResult = default.qs(kth, 0, len(inp)-1)
        # stop timer, and append the partition iterations for that run
        defaultTimes.append(time.time()-start)
        defaultOps.append(default.partitionIterations)

        print("starting dynamic")
        dynamic = Dynamic(inp[:], [.4, .6], False)
        print("done copying list")
        start = time.time()
        dynamicResult = dynamic.qs(kth, 0, len(inp)-1)
        dynamicTimes.append(time.time()-start)
        dynamicOps.append(dynamic.partitionIterations)

        print("starting fra")
        floydRivest = FloydRivest(inp)
        start = time.time()
        fraResult = floydRivest.select(kth-1, 0, len(inp)-1)
        fraTimes.append(time.time()-start)

        # checking results
        if (verifyResults):
            sorted_array = sorted(inp)
            correctVal = sorted_array[kth-1]
            assert correctVal == defaultResult == dynamicResult == fraResult

    # printing outputs
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
