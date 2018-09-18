# Uses Python 3
# Fibonacci Modulus
# Takes two inputs m and n. Output the remainder of Fn divided by m
import sys

def fibonacciMod(n, m):
    if n == 1:
        return 1
    # Store two arrays: one for fib, one for fib mod m
    arrayOfFib = [0, 1]
    arrayOfFibMod = [0, 1]

    # Two variables to keep track of the location of 0 and 1 consecutive: The Pisano Period
    x = 0
    y = 0
    for i in range(2, n + 1):
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
            # Periodic length is found
            periodicLength = len(arrayOfFibMod) - 2
            periodic_n = n % periodicLength
            return arrayOfFib[periodic_n] % m
            break
        # The Pisano period length can be greater than n - in which case, evaluate the Fibonacci mod m directly.
        if i == n:
            return currentFibMod
            break

inputs = sys.stdin.read()
tokens = [int(x) for x in inputs.split()]
print (fibonacciMod(tokens[0], tokens[1]))
#print (fibonacciMod(2816213588, 239))