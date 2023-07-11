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
    maxVal = 1000

    input_array = createTestArray(maxVal, currentSize)
    copy_array = copy.deepcopy(input_array)
    kth = random.randint(1, len(input_array)-1)
    # print(input_array)
    # print(kth)

    lp = LineProfiler()
    lp.add_function(dynamic.partition)
    lp.add_function(dynamic.dynamic)
    lp_wrapper = lp(dynamic.qs)
    lp_wrapper(input_array, kth, 0, len(input_array)-1)

    result = io.StringIO()
    with redirect_stdout(result):
        lp.print_stats()
    result = result.getvalue()
    # result = 'Hits'+result.split('Hits')[-1]
    # result = '\n'.join([','.join(line.rstrip().split(None, 5))
    #                     for line in result.split('\n')])
    print(result)

    # dp = LineProfiler()
    # # lp.add_function(dynamic.partition)
    # # lp.add_function(dynamic.dynamic)
    # dp_wrapper = dp(default.qs)
    # dp_wrapper(copy_array, kth, 0, len(copy_array)-1)

    # result2 = io.StringIO()
    # with redirect_stdout(result2):
    #     dp.print_stats()
    # result2 = result2.getvalue()
    # # result = 'Hits'+result.split('Hits')[-1]
    # # result = '\n'.join([','.join(line.rstrip().split(None, 5))
    # #                     for line in result.split('\n')])
    # print(result2)
