import csv
import random
import time
import quickSelect
import cProfile
import re

# if you want to check quickSelect's correctness by sorting the list and accessing its kth element, set this to true.
# Works for smaller values but too time consuming for larger values, so commented out when calculating the runtimes
verifyResults = False


def createTestArray(maxVal, numItems):
    # given the max possible value of an element, and the total number of elements the array should have,
    # generates an unsorted array of random, distinct values that meet these speciications.

    testArray = random.sample(range(0, maxVal), numItems)
    return testArray


def timeTaken(input_array, k, choice, correctK):
    # given an array and a value k, will return the time it takes to run quickSelect on those inputs. Also
    # takes a string which determines which method of pivot choosing we use for quickSelect (default, dynamic,
    # probabilistic, deterministic, etc.)

    start = time.time()
    # running quickSelect
    result = quickSelect.qs(input_array, k, 0, len(input_array)-1, choice)
    # checks that quickSelect returned the correct value
    if verifyResults:
        assert correctK == result
        print("quickselect returned the correct value!")
    elapsed_time = (time.time() - start)
    return elapsed_time


def main():  # main body code

    # max value of an element in our arrays
    max_value = 100000000

    # doubling values from 250k to 64M
    minItems = 250000
    maxItems = 64000000

    # dictionary that will store times for each pivot choosing method
    default = dict()
    probabilistic = dict()
    dynamic = dict()
    dicts = [default, dynamic]

    # initially the size of the array is 250k, and we are on point 0 of
    array_size = minItems
    # while loop will double 250k until we get to 64M
    while array_size <= maxItems:
        print("\n--------------------------------------")
        print("ARRAY SIZE IS " + str(array_size))
        print("--------------------------------------\n")

        # number of times we want to run quickSelect on each method for a given size
        numRuns = 5
        # list of each method's time list, need to add more lists if want to include more methods
        times = [[], []]

        # list of possible methods for pivot choosing, need to increase if want to add more methods
        choices = ["default", "dynamic"]

        # for each run
        for i in range(numRuns):

            # generating the random array
            input_array = createTestArray(max_value, array_size)
            print("created input array")
            # copying it so that when we modify arrays with the partition, we always have the original to go back to
            copy_array = input_array.copy()
            print("copied input array")

            # generate a random k
            kth = random.randint(1, len(input_array)-1)

            # #necessary code if we want to check quickSelect values (algorithm works for smaller list sizes, but
            # #it is too time consuming to sort the list and check it for higher list sizes)
            if (verifyResults):
                sorted_array = sorted(copy_array)
                print("sorted the copied array")

            # finding the correct value, only needed when we want to verify results
            if verifyResults:
                correctVal = sorted_array[kth-1]
            else:
                correctVal = 0

            print('\n running test ' + str(i+1) + " of " + str(numRuns) + "\n")
            # for each pivot choosing method
            for i in range(len(choices)):
                # restore the original array for this size
                copy_array = input_array
                print("\n beginning " + choices[i] + " quickselect \n")
                # add the resulting time it takes to run quick select to this pivot choosing's time list
                times[i].append(
                    timeTaken(copy_array, kth, choices[i], correctVal))

        # for each pivot choice method
        for i in range(len(choices)):
            # access the list of this method's run times
            currentArray = times[i]
            # average them, and assign that value to this method's dictionary (with the list size as the key and
            # the time as the value)
            eval(choices[i])[array_size] = sum(currentArray) / \
                len(currentArray)

        # doubling array size
        array_size = array_size*2

    # writing results to a csv file
    with open('complexity.csv', 'w') as f:
        writer = csv.writer(f, delimiter='\t')
        writer.writerow(['list size', 'default', 'dynamic'])
        for key in default.keys():
            writer.writerow([key] + [d[key] for d in dicts])


if __name__ == "__main__":
    main()
