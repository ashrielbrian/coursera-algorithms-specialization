# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def evaltMinAndMax(i, j, m, M, operations):
    minValue = float("inf")
    maxValue = float("-inf")

    for k in range(i, j):
    #    print (M[i][k], M[k + 1][j], m[i][k],m[k + 1][j])
        a = evalt(M[i][k], M[k + 1][j], operations[k])
        b = evalt(M[i][k], m[k + 1][j], operations[k])
        c = evalt(m[i][k], M[k + 1][j], operations[k])
        d = evalt(m[i][k], m[k + 1][j], operations[k])
        minValue = min(minValue, a, b, c, d)
        maxValue = max(maxValue, a, b, c, d)
    return (minValue, maxValue)

def get_maximum_value(dataset):
    numbers = [int(x) for x in dataset[::2]] # all even values
    ops = dataset[1::2] # all odd values
    size = len(numbers)
    MinMatrix = [[0 for i in range(size)] for j in range(size)]
    MaxMatrix = [[0 for i in range(size)] for j in range(size)]

    # Initialising the main diagonals of both matrices
    for i in range(size):
        MinMatrix[i][i] = numbers[i]
        MaxMatrix[i][i] = numbers[i]
    # Code below iterates across the diagonal lines of the matrices
    for s in range(1, size): # s = j - i, i.e. the length of the specific subsequence 
        for i in range(size - s):
            j = i + s
            MinMatrix[i][j], MaxMatrix[i][j] = evaltMinAndMax(i, j, MinMatrix, MaxMatrix, ops)
    #print (MinMatrix)
    #print (MaxMatrix)
    return MaxMatrix[0][size - 1]


if __name__ == "__main__":
    print(get_maximum_value(input()))