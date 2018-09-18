# Uses python3
import sys

# The knapsack problem is (i) discrete and (ii) without repetitions

def optimal_weight(W, w):
    width, height = W + 1, len(w) + 1
    ValueMatrix = [[0 for j in range(width)] for i in range(height)]

    # Algorithm checks two possibilities. 
    # First - that the current knapsack does not currently have the item in question.
    # Second - that the current knapsack does indeed have the item in question (i.e. optimal)
    # and we proceed to remove it from the knapsack (w - wi)

    # i - represents the item number, where w[i] gives the value of the item.
    # ValueMatrix - represents the value of the total set of possibilities

    optimalValue = 0
    for i in range(1, height):
        weightIndex = i - 1
        for j in range(1, width): # j represents the current max Weight of the knapsack
            ValueMatrix[i][j] = ValueMatrix[i - 1][j]
            if w[weightIndex] <= j: # the current weight can fit the current item
                currentValue = ValueMatrix[i - 1][j - w[weightIndex]] + w[weightIndex]
                ValueMatrix[i][j] = currentValue if currentValue > ValueMatrix[i][j] else ValueMatrix[i][j]
    return ValueMatrix[height - 1][width - 1]

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
