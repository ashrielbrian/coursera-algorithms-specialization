# Uses python3
import sys

def getArrayOfFirstNterms(n):
    list = []

    for i in range(1, n):
        list.append(i)
    return list

def optimal_summands(n):
    # Given a large positive integer, return the largest possible k, where k is the total number of summands, and whose summands are wholly unique.
    # Algorithm aims to return an array where max(len(currentSummands)) AND where each element in currentSummands is unique.
        # Solution is to start with n, and begin by finding the smallest possible summand (i = 1), and appending the remainder (n - 1).
        # Then, iterate i++ and append i++ and remainder into the summands array.
        # Return the summands when the remainder is either 0 or there is a duplicate in the summands array.

        # each array consists of summands (one partition each that are updated on each iteration)
    if n == 1:
        return [1]
    elif n == 2:
        return [2]
    
    i = 1
    previousRemainder = 0
    keepGoing = True
    while keepGoing:
        remainder = n - i

        if remainder == 0:
            return getArrayOfFirstNterms(i + 1)
        elif remainder <= i:
            summands = getArrayOfFirstNterms(i)
            summands.append(previousRemainder)
            return summands

        i += 1
        previousRemainder = remainder
        n = remainder

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
