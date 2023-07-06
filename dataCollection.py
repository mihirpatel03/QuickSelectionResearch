import csv
import random
import time
import quickSelect


def createTestArray(maxVal, numItems):
    # given the max possible value of an element, and the total number of elements the array should have,
    # generates an unsorted array of random, distinct values that meet these speciications.

    testArray = random.sample(range(0, maxVal), numItems)
    return testArray


def timeTaken(input_array, current_point, total_points):
    # given an array, will return the average time it takes to run quickselect on that array (with random k)

    times = []
    last_idx = len(input_array)-1
    # randomizing the number we are looking for
    kth = random.randint(0, last_idx)
    # average of numRuns number of runs
    numRuns = 10
    for i in range(numRuns):
        start = time.time()
        # running quickSelect
        quickSelect.qs(input_array, kth, 0, last_idx)
        elapsed_time = (time.time() - start)
        times.append(elapsed_time)
        print("\n done with " + str(i+1) +
              " run(s) out of " + str(numRuns) + " for data point " + str(current_point+1) + " out of " + str(total_points) + "\n")

    # return average time
    return sum(times)/len(times)


def main():  # main body code
    # max value of an element in our arrays (10 million)
    max_value = 64000000

    # doubling values from 250k to 64M
    minItems = 250000
    maxItems = 2000000
    numDataPoints = 4
    # dictionary that will store times
    default = dict()

    # generates i data points (i array sizes between 10k and 100 million)
    # consider adding a way to get i distinct data points?
    array_size = minItems
    currentPoint = 0
    while array_size <= maxItems:
        print("array size is " + str(array_size))
        # generating the random array
        input_array = createTestArray(max_value, array_size)
        # getting the average time it takes to run quick select on this array for random k
        print("beginning quickselect")
        avg_time_taken = timeTaken(input_array, currentPoint, numDataPoints)
        # storing that in the dictionary
        default[array_size] = avg_time_taken

        currentPoint += 1
        array_size = array_size*2

    dicts = [default, default]

    with open('complexity.csv', 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerow(['ID', 'dict1', 'dict2', 'dict3', 'dict4'])
        for key in default.keys():
            writer.writerow([key] + [d[key] for d in dicts])


if __name__ == "__main__":
    main()
