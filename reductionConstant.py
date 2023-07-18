
import random
from default import Default
from dynamic import Dynamic
from floydRivest import FloydRivest


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

    max_value, array_size, numRuns = 10000000, 1000000, 25
    defaultConstant, dynamicConstant, dynamic1Constant = [], [], []
    for i in range(numRuns):
        print("starting run " + str(i) + " of " + str(numRuns))
        inp = sampleTestArray(max_value, array_size)
        kth = random.randint(1, len(inp)-1)

        default = Default(inp[:])
        default.qs(kth, 0, len(inp)-1)
        defaultConstant += default.constantsList

        dynamic = Dynamic(inp, .4, .6)
        dynamic.qs(kth, 0, len(inp)-1)
        dynamicConstant += dynamic.constantsList

        dynamic1 = Dynamic(inp, .16, .83)
        dynamic1.qs(kth, 0, len(inp)-1)
        dynamic1Constant += dynamic1.constantsList

    dynamicC = sum(dynamicConstant)/len(dynamicConstant)
    print("for bounds .4, .6, dynamic constant is " + str(dynamicC))

    dynamic1C = sum(dynamic1Constant)/len(dynamic1Constant)
    print("for bounds .16, .83, dynamic constant is " + str(dynamic1C))

    defaultC = sum(defaultConstant)/len(defaultConstant)
    print("default constant is " + str(defaultC))
