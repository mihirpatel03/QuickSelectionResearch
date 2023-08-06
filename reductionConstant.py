
import random
from default import Default
from dynamic import Dynamic
from floydRivest import FloydRivest


def sampleTestArray(maxVal, numItems):
    # generates an unsorted array of numItems length, with random and distinct elements
    testArray = random.sample(range(0, maxVal), numItems)
    return testArray


def avg(input_list):
    # returns average value of an array
    return sum(input_list)/len(input_list)


if __name__ == "__main__":
    # initializing running values and also lists for summing reduction constants
    max_value, array_size, numRuns = 10000000, 1000000, 25
    defaultConstant, dynamicConstant, dynamic2Constant = [], [], []
    for i in range(numRuns):
        print("starting run " + str(i) + " of " + str(numRuns))
        # generate the random array and a random k value
        inp = sampleTestArray(max_value, array_size)
        kth = random.randint(1, len(inp)-1)

        # run default
        default = Default(inp[:], True)
        default.qs(kth, 0, len(inp)-1)
        # add the object's list of reduction sizes to our current list
        defaultConstant += default.constantsList

        # run dynamic with bounds .4, .6
        dynamic = Dynamic(inp[:], [.4, .6], True)
        dynamic.qs(kth, 0, len(inp)-1)
        dynamicConstant += dynamic.constantsList

        # run dynamic with bounds .2, .4, .6, .8
        dynamic2 = Dynamic(inp, [.2, .4, .6, .8], True)
        dynamic2.qs(kth, 0, len(inp)-1)
        dynamic2Constant += dynamic2.constantsList

    # print outputs
    print("for bounds .4, .6, dynamic constant is " + str(avg(dynamicConstant)))
    print("for bounds, .2, .4, .6, .8 pivot constant is " +
          str(avg(dynamic2Constant)))
    print("default constant is " + str(avg(defaultConstant)))
