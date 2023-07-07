import csv
import random
import time
import quickSelect


def createTestArray(maxVal, numItems):
    # given the max possible value of an element, and the total number of elements the array should have,
    # generates an unsorted array of random, distinct values that meet these speciications.

    testArray = random.sample(range(0, maxVal), numItems)
    return testArray


def timeTaken(input_array, k, choice, correctK):
    # given an array, will return the average time it takes to run quickselect on that array (with random k)

    start = time.time()
    # running quickSelect
    result = quickSelect.qs(input_array, k, 0, len(input_array)-1, choice)
    assert correctK == result
    elapsed_time = (time.time() - start)
    return elapsed_time


def main():  # main body code
    # max value of an element in our arrays (10 million)
    max_value = 64000000

    # doubling values from 250k to 64M
    minItems = 250000
    maxItems = 64000000
    # dictionary that will store times
    default = dict()
    probabilistic = dict()
    dynamic = dict()

    # generates i data points (i array sizes between 10k and 100 million)
    # consider adding a way to get i distinct data points?
    array_size = minItems
    currentPoint = 0
    while array_size <= maxItems:
        print("array size is " + str(array_size))
        # generating the random array
        input_array = createTestArray(max_value, array_size)
        sorted_array = sorted(input_array.copy())
        # getting the average time it takes to run quick select on this array for random k

        choices = ["default", "dynamic"]

        kth = random.randint(1, len(input_array)-1)
        correctVal = sorted_array[kth-1]
        # average of numRuns number of runs
        numRuns = 5
        defaultTimes = []
        dynamicTimes = []
        times = [defaultTimes, dynamicTimes]
        # need a list of lists
        for i in range(numRuns):
            print('running test ' + str(i+1) + " of " + str(numRuns))
            for i in range(len(choices)):
                x = input_array.copy()
                # print("beginning " + choices[i] + " quickselect")
                times[i].append(timeTaken(
                    x, kth, choices[i], correctVal))

        for i in range(len(choices)):
            currentArray = times[i]
            eval(choices[i])[array_size] = sum(currentArray) / \
                len(currentArray)  # avg of the time arrays

        currentPoint += 1
        array_size = array_size*2

    dicts = [default, dynamic]

    with open('complexity.csv', 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerow(['ID', 'default', 'dynamic'])
        for key in default.keys():
            writer.writerow([key] + [d[key] for d in dicts])


if __name__ == "__main__":
    main()
