
import random
from default import Default
from dynamic import Dynamic
from floydRivest import FloydRivest
from dualPivot import DualPivot


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

    max_value, array_size, numRuns = 10000000, 1000000, 1
    defaultConstant, dynamicConstant, dualConstant = [], [], []
    for i in range(numRuns):
        print("starting run " + str(i) + " of " + str(numRuns))
        inp = sampleTestArray(max_value, array_size)
        kth = random.randint(1, len(inp)-1)

        default = Default(inp[:], True)
        x = default.qs(kth, 0, len(inp)-1)
        defaultConstant += default.constantsList

        dynamic = Dynamic(inp[:], [.4, .6], True)
        y = dynamic.qs(kth, 0, len(inp)-1)
        dynamicConstant += dynamic.constantsList

        dualPivot = DualPivot(inp, True)
        z = dualPivot.qs(kth, 0, len(inp)-1)
        dualConstant += dualPivot.constantsList

        print(x, y, z)
        assert x == y == z

    dynamicC = sum(dynamicConstant)/len(dynamicConstant)
    print("for bounds .4, .6, dynamic constant is " + str(dynamicC))

    dualC = sum(dualConstant)/len(dualConstant)
    print("dual pivot constant is " + str(dualC))

    defaultC = sum(defaultConstant)/len(defaultConstant)
    print("default constant is " + str(defaultC))
