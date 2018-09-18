# Uses Python 3

def fibonacciRecursive(n):
    if (n <= 1):
        return n
    return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2)


def fibonacciEfficient(n):
    arrayOfFib = [0, 1]
    currentFib = 0
    if n == 0 or n == 1:
        return n
    else:
        for i in range(2, n + 1):
            currentFib = arrayOfFib[i - 1] + arrayOfFib[i - 2]
            arrayOfFib.append(currentFib)
        return arrayOfFib[n]

n = int(input())

print(fibonacciEfficient(n))
#print(fibonacciRecursive(n))

