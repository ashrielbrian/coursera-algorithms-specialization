# Uses python3
import sys

def updateSummandsWith(list, first, second):
    # replace the last element in the list
    list[-1] = first
    # append the second arg to the end of the list
    list.append(second)
    return list

def checkDuplicates(list):
    # Function returns True if there are duplicates in the list
    # set() returns an unordered list of unique elements from a given list
    noDuplicates = set(list)
    bool = len(noDuplicates) != len(list)
    return bool

def optimal_summands(n):
    # Given a large positive integer, return the largest possible k, where k is the total number of summands, and whose summands are wholly unique.
    # Algorithm aims to return an array where max(len(currentSummands)) AND where each element in currentSummands is unique.
        # Solution is to start with n, and begin by finding the smallest possible summand (i = 1), and appending the remainder (n - 1).
        # Then, iterate i++ and append i++ and remainder into the summands array.
        # Return the summands when the remainder is either 0 or there is a duplicate in the summands array.

        # each array consists of summands (one partition each that are updated on each iteration)

    previousSummands = [n]
    currentSummands = [n]

    i = 1
    keepGoing = True
    while keepGoing:
        remainder = n - i
        if remainder == 0:
            return previousSummands
        
        # Replacing the last element of the currentSummands array with i and x
        currentSummands = updateSummandsWith(currentSummands, i, remainder)
        if checkDuplicates(currentSummands):
            return previousSummands
        
        i += 1
        n = remainder
        previousSummands = currentSummands[:]
        

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')

