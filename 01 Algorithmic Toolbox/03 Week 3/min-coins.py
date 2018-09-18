# Uses Python 3
# Changes the input value with the minimum number of coins with values 10, 5 and 1

# 1. Safe move: Find the max number of coins for the largest denomination
# 2. Sub problem: Remove the hundreds, focus on the tens, then the ones 

# Input value m <= 10^3

def minCoinCount(m):
    remainderCash = m

    tens = remainderCash // 10
    remainderCash = remainderCash % 10

    fives = remainderCash // 5
    remainderCash = remainderCash % 5

    ones = remainderCash
    return tens + fives + ones

n = int(input())
print(minCoinCount(n))


