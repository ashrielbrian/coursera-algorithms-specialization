# Uses python3
import sys

# Algorithm uses Dynamic Programming (tabulation) in order to obtain the smallest
# number of coins required to change a given money (in integer, < 10^3)
def get_change(m):
    coinDenominations = [1, 3, 4]
    minNumOfCoins = [0] * (m + 1) # Tabulation of data
    # i acts as both the index and current iteration of money integer
    for i in range(1, m + 1):
        minNumOfCoins[i] = float("inf") # Sets the initial element to be infinite
        for eachCoin in coinDenominations:
            if i >= eachCoin:
                numOfCoins = minNumOfCoins[i - eachCoin] + 1 # looks up previous money-coin changes
                if numOfCoins < minNumOfCoins[i] :
                    minNumOfCoins[i] = numOfCoins
    return minNumOfCoins[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
