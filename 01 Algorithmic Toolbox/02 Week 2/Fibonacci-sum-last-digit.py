# Uses Python 3

# Function obtains the last digit of the sum of n Fibonacci numbers: Sn = F0 + F1 + F2 ... + Fn

def fibonacciSumLastDigitNaive(n):
    # Algorithm here is too slow
    arrayOfFib = [0, 1]
    currentFib = 0
    if n == 0 or n == 1:
        return n
    else:
        for i in range(2, n + 3):
            currentFib = ((arrayOfFib[i - 1] % 10) + (arrayOfFib[i - 2] % 10)) % 10
            arrayOfFib.append(currentFib)
        # Sn = Fn+2 - 1
        sumOfFib = arrayOfFib[n + 2] - 1
        return sumOfFib

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

    # The Pisano length of mod 10 is 60.
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

            lastDigit = arrayOfFibMod[periodic_n] % m
            return lastDigit
        # The Pisano period length can be greater than n - in which case, evaluate the Fibonacci mod m directly.
        if i == n:
            return currentFibMod
            break


def fibonacciSumLastDigit(n):
    # Sn = F0 + F1 + ... Fn, can be shown to equal,
    # Sn = Fn+2 - 1
    m = 10 # Mod 10 gives the last digit of an integer

    # 1. If n = 100000 then find F100002, as Sn = Fn+2 - 1, i.e. S100000 = Fn1000002 - 1. 
    # Where last digit of F100002 can be calculated using the FibonacciMod func 
    fibNPlusTwo = fibonacciMod(n + 2, m) # returns the last digit of Fn+2

    if fibNPlusTwo == 0:
        fibNPlusTwo = 10

    lastDigitOfFibSum = fibNPlusTwo - 1
    return lastDigitOfFibSum

n = int(input())
print(fibonacciSumLastDigit(n)) 
