import random
import quickSelect
import cProfile
import pstats
import io
import pandas as pd


def createTestArray(maxVal, numItems):
    # given the max possible value of an element, and the total number of elements the array should have,
    # generates an unsorted array of random, distinct values that meet these speciications.

    testArray = random.sample(range(0, maxVal), numItems)
    return testArray


if __name__ == "__main__":

    choices = ["default", "dynamic"]
    choicesDict = dict()

    input_array = createTestArray(32000000, 16000000)
    kth = random.randint(1, len(input_array)-1)

    pr = cProfile.Profile()

    input_array = createTestArray(32000, 1600)
    kth = random.randint(1, len(input_array)-1)

    for i in range(1, 2):

        pr.enable()

        val = quickSelect.qs(input_array, kth, 0,
                             len(input_array)-1, choices[i])

        pr.disable()

        result = io.StringIO()
        pstats.Stats(pr, stream=result).strip_dirs().sort_stats(
            pstats.SortKey.CALLS).print_stats()
        result = result.getvalue()
        # chop the string into a csv-like buffer
        result = 'ncalls'+result.split('ncalls')[-1]
        result = '\n'.join([','.join(line.rstrip().split(None, 5))
                            for line in result.split('\n')])
        # save it to disk

        with open('test.csv', 'w') as f:
            # f=open(result.rsplit('.')[0]+'.csv','w')
            f.write(result)
            f.close()

        df = pd.read_csv("test.csv")
        # gets only the column related to the number of times methods are called
        totalPartitionIterations = df.ncalls[0]
        choicesDict[choices[i]] = totalPartitionIterations

    print(choicesDict)
