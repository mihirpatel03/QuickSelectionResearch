import random
import quickSelect
import cProfile
import re
import pstats


def createTestArray(maxVal, numItems):
    # given the max possible value of an element, and the total number of elements the array should have,
    # generates an unsorted array of random, distinct values that meet these speciications.

    testArray = random.sample(range(0, maxVal), numItems)
    return testArray


if __name__ == "__main__":

    input_array = createTestArray(320, 100)
    kth = random.randint(1, len(input_array)-1)

    with cProfile.Profile() as profile:
        val = quickSelect.qs(input_array, kth, 0,
                             len(input_array)-1, "default")

    results = pstats.Stats(profile)
    results.sort_stats(pstats.SortKey.CALLS)
    results.print_stats()
