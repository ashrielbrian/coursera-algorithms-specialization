#Uses python3

import sys

def isGreaterOrEqual(next, current):
    # Append digit to the back and front of maxDigit
    # Compare the two numbers: return the number with the larger number
    firstValue = int(next + current)
    secondValue = int(current + next)
    if firstValue > secondValue:
        return True # That is, the next value in the array is greater than the current: True
    return False

def largest_number(a):
    previousArray = []
    currentArray = a
    res = ""

    while previousArray != currentArray:
        previousArray = currentArray[:]

        for i in range(len(currentArray) - 1):
            currentDigit = currentArray[i]
            nextDigit = currentArray[i + 1]
            if isGreaterOrEqual(nextDigit, currentDigit):
                # If true, swap the values of both elements
                currentArray[i] = nextDigit
                currentArray[i + 1] = currentDigit

    for x in currentArray:
        res += x
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
