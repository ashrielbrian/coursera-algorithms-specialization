# Uses Python 3
# Function takes an input of m and n and returns the last digit of the sum of Fm + Fm+1 + ... Fn
import sys

def fibonacciMod(n, m):
    # Sn = Fn+2 - 1
    if n == 1:
        return 1
    # Store two arrays: one for fib, one for fib mod m
    arrayOfFib = [0, 1]
    arrayOfFibMod = [0, 1]

    # Two variables to keep track of the location of 0 and 1 consecutive: The Pisano Period
    x = 0
    y = 0

    # The Pisano length of mod 100 is 300. This stores in the array the last TWO digits of the Fibonacci number
    for i in range(2, n + 1):
        # Part 1: Find the Pisano Period
        # Evaluating the current fib
        currentFib = arrayOfFib[i - 1] + arrayOfFib[i - 2]
        arrayOfFib.append(currentFib)
        # Evaluating the current fib mod
        currentFibMod = currentFib % m
        arrayOfFibMod.append(currentFibMod)
        x = arrayOfFibMod[i - 1]
        y = arrayOfFibMod[i]
        # Checks if the period has been found. If not, keep looping.
        if (x == 0) and (y == 1):
            # Part 2: Evaluate the periodic length
            # Periodic length is found 
            periodicLength = len(arrayOfFibMod) - 2
            periodic_n = n % periodicLength
            return arrayOfFib[periodic_n] % m
            break
        # The Pisano period length can be greater than n - in which case, evaluate the Fibonacci mod m directly.
        if i == n:
            return currentFibMod
            break


def fibonacciPartialSumLastDigit(m, n):

    mod = 100
    
    fibNPlusTwo = fibonacciMod(n + 2, mod) # returns the last digit of Fn+2
    fibMPlusOne = fibonacciMod(m + 1, mod)

    lastDigitOfFibPartialSum = (fibNPlusTwo - fibMPlusOne) % 10
    return lastDigitOfFibPartialSum

inputs = sys.stdin.read()
tokens = [int(x) for x in inputs.split()]

print(fibonacciPartialSumLastDigit(tokens[0], tokens[1]))