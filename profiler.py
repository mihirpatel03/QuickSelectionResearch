import random
import default
import cProfile
import pstats
import io
import pandas as pd
import time


def createTestArray(maxVal, numItems):
    # given the max possible value of an element, and the total number of elements the array should have,
    # generates an unsorted array of random, distinct values that meet these speciications.

    testArray = random.sample(range(0, maxVal), numItems)
    return testArray


if __name__ == "__main__":

    choices = ["default", "dynamic"]
    choicesDict = dict()

    numRuns = 1
    currentSize = 16000000
    maxVal = 100000000
    totalOperations = [[], []]

    for i in range(numRuns):

        input_array = createTestArray(maxVal, currentSize)
        kth = random.randint(1, len(input_array)-1)

        testArrays = []
        testArrays.append(input_array)
        for i in range(1, len(choices)):
            testArrays.append(input_array.copy())

        pr = cProfile.Profile()

        for i in range(len(choices)):
            # print(testArrays[i])

            start = time.time()
            pr.enable()

            val = default.qs(testArrays[i], kth, 0, len(
                testArrays[i])-1, choices[i])

            pr.disable()
            print(time.time()-start)

            result = io.StringIO()
            pstats.Stats(pr, stream=result).strip_dirs().sort_stats(
                pstats.SortKey.CALLS).print_stats()
            result = result.getvalue()
            # chop the string into a csv-like buffer
            result = 'ncalls'+result.split('ncalls')[-1]
            result = '\n'.join([','.join(line.rstrip().split(None, 5))
                                for line in result.split('\n')])
            # save it to disk

            with open(choices[i]+'.csv', 'w') as f:
                # f=open(result.rsplit('.')[0]+'.csv','w')
                f.write(result)
                f.close()

            df = pd.read_csv(choices[i]+'.csv')
            # gets only the column related to the number of times methods are called
            totalOperations[i].append(int(df.ncalls[0]))
            # print(testArrays[i])

    for i in range(len(choices)):
        ops = int(sum(totalOperations[i])/len(totalOperations[i]))
        print("for an array size of " + str(currentSize) + ", " +
              choices[i] + " takes on average " + str(ops) + " operations.")
