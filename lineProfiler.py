import random
import default
import floydRivest
import io
import pandas as pd
import dynamic
from line_profiler import LineProfiler
from contextlib import redirect_stdout
import copy


def createTestArray(maxVal, numItems):
    # given the max possible value of an element, and the total number of elements the array should have,
    # generates an unsorted array of random, distinct values that meet these speciications.

    testArray = random.sample(range(0, maxVal), numItems)
    return testArray


if __name__ == "__main__":

    currentSize = 10
    maxVal = 100

    input_array = createTestArray(maxVal, currentSize)
    copy_array = copy.deepcopy(input_array)
    kth = random.randint(1, len(input_array)-1)

    dynamicProf = LineProfiler()
    dynamicProf.add_function(dynamic.partition)
    dynamicProf.add_function(dynamic.dynamic)
    dynamicProfWrapper = dynamicProf(dynamic.qs)
    dynamicProfWrapper(input_array, kth, 0, len(input_array)-1)

    dynamicResult = io.StringIO()
    with redirect_stdout(dynamicResult):
        dynamicProf.print_stats()
    dynamicResult = dynamicResult.getvalue()

    dynamicTime = dynamicResult.split("Total time: ")[1].split("s")[0]
    # print("dynamic cutoff quickselect runs in " + dynamicTime + " seconds")
    # print(dynamicResult.split("Line Contents")[1][10])
    for i in range(10, 40):
        print(dynamicResult[i])

    # defaultProf = LineProfiler()
    # defaultProf.add_function(default.partition)
    # defaultProfWrapper = defaultProf(default.qs)
    # defaultProfWrapper(copy_array, kth, 0, len(copy_array)-1)

    # defaultResult = io.StringIO()
    # with redirect_stdout(defaultResult):
    #     defaultProf.print_stats()
    # defaultResult = defaultResult.getvalue()

    # defaultTime = defaultResult.split("Total time: ")[1].split("s")[0]
    # print("default quickselect runs in " + defaultTime + " seconds")

    # print(dynamicResult)
    # print(defaultResult)
