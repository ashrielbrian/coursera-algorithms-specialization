# Uses Python 3

# Input: first line takes n numbers of items, and W knapsack capacity
# all lines after give value v and then weight w of item i

# Outputs the maximum value of fractions of the items

import sys

def get_optimal_value(capacity, weights, values):
    value = 0
    numberOfItems = len(weights)

    arrayOfvalueToWeightRatio = []
    for i in range(0, numberOfItems):
        currentRatio = values[i] / weights[i]
        arrayOfvalueToWeightRatio.append([currentRatio, values[i], weights[i]])
    
    # Sorts the array in nlogn time, according to the currentRatio in desc order
    sortedArrayDesc = sorted(arrayOfvalueToWeightRatio,key=lambda item: item[0], reverse=True)

    for i in range(0, numberOfItems):
        currentItem = sortedArrayDesc[i]
        currentItemRatio = currentItem[0]
        currentItemValue = currentItem[1]
        currentItemWeight = currentItem[2]
        # choose the smallest value of weights OR capacity left
        itemWeightToFill = min(currentItemWeight, capacity) # This is the fraction to multiply the value-weight ratio
        value = value + (itemWeightToFill * currentItemRatio)
        capacity = capacity - itemWeightToFill # update the new knapsack capacity
        # print ("Here's the current %s th iteration: with a %s value-cost ratio, filling %s kg of %s kg of capacity left" %(i, currentItemRatio, currentItemWeight, capacity))
        if capacity == 0:
            break
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
