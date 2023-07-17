import random
import io
import pandas as pd
from line_profiler import LineProfiler
from contextlib import redirect_stdout
import cProfile
import pstats


def createTestArray(maxVal, numItems):
    # given the max possible value of an element, and the total number of elements the array should have,
    # generates an unsorted array of random, distinct values that meet these speciications.

    testArray = random.sample(range(0, maxVal), numItems)
    return testArray


def printHits(input_result):
    linesList = input_result.split("\n")
    totalHits = 0
    for i in range(len(linesList)):
        if linesList[i] == "":
            continue
        if linesList[i][0].isalpha() or linesList[i][0] == "=":
            continue
        foundHits = False
        numHits = ""
        for j in range(7, len(linesList[i])):
            if linesList[i][j] == " ":
                if foundHits:
                    totalHits += int(numHits)
                    break
                else:
                    continue
            elif linesList[i][j] in '0123456789':
                foundHits = True
                numHits += linesList[i][j]
            elif linesList[i][j].isalpha():
                break
    # print(str(totalHits))
    return totalHits


def printTime(input_result):
    result_time = float(input_result.split("Total time: ")[1].split("s")[0])
    # print("quickselect runs in " + result_time + "seconds")
    return result_time


def getOutput(profiler):
    selectResult = io.StringIO()
    with redirect_stdout(selectResult):
        profiler.print_stats()
    return selectResult.getvalue()


def avg(input_list):
    return sum(input_list)/len(input_list)


if __name__ == "__main__":
    pass
    # lp = LineProfiler()
    # lp_wrapper = lp(test)
    # for i in range(5):
    #     test()
    # lp.print_stats()

    # pr = cProfile.Profile()
    # pr.enable()
    # x = createTestArray(100000000, 4000000)
    # pr.disable()

    # result = io.StringIO()
    # pstats.Stats(pr, stream=result).strip_dirs().print_stats()
    # print(result.getvalue())


# if __name__ == "__main__":

#     currentSize = 10000
#     maxVal = 10000000

#     dynamicOps = []
#     defaultOps = []
#     dynamicTimes = []
#     defaultTimes = []

#     numRuns = 1
#     for i in range(numRuns):

#         input_array = createTestArray(maxVal, currentSize)
#         copy_array = copy.deepcopy(input_array)
#         kth = random.randint(1, len(input_array)-1)

#         dynamicProf = LineProfiler()
#         dynamicProf.add_function(dynamic.partition)
#         dynamicProf.add_function(dynamic.dynamic)
#         dynamicProfWrapper = dynamicProf(dynamic.qs)
#         dynamicProfWrapper(input_array, kth, 0, len(input_array)-1)
#         dynamicResult = getOutput(dynamicProf)
#         print(dynamicResult)

#         dynamicOps.append(printHits(dynamicResult))
#         dynamicTimes.append(printTime(dynamicResult))

#         defaultProf = LineProfiler()
#         defaultProf.add_function(default.partition)
#         defaultProfWrapper = defaultProf(default.qs)
#         defaultProfWrapper(copy_array, kth, 0, len(copy_array)-1)
#         defaultResult = getOutput(defaultProf)

#         defaultOps.append(printHits(defaultResult))
#         defaultTimes.append(printTime(defaultResult))

#     # print(str(avg(dynamicOps)))
#     # print(str(avg(dynamicTimes)))
#     # print(str(avg(defaultOps)))
#     # print(str(avg(defaultTimes)))
