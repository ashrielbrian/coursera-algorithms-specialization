# Uses Python 3

def fibonacciLastDigitNaive(n):
    if (n <= 1):
        return n
    return ((fibonacciLastDigit(n - 1) % 10) + (fibonacciLastDigit(n - 2) % 10)) % 10

def fibonacciLastDigitEfficient(n):
    arrayOfFib = [0, 1]
    currentFib = 0
    if n == 0 or n == 1:
        return n
    else:
        for i in range(2, n + 1):
            currentFib = ((arrayOfFib[i - 1] % 10) + (arrayOfFib[i - 2] % 10)) % 10
            arrayOfFib.append(currentFib)
        return arrayOfFib[n]


n = int(input())

print(fibonacciLastDigitEfficient(n))