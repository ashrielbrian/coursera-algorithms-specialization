# Uses python3
import sys


# 1. Start the array with n
# 2. Check if remainder == 1
#   2a. Initialise the array's current sequence element
# 3. If not, we go through the three possible scenarios:
#   3a. Divide 3 and check if no remainder, AND whether 
def backtrack(n, seq):
    multiplicativeSeq = [n]
    remainder = n
    
    while remainder != 1:
        previousRemainder = remainder
        minOperations = float("inf")
        if previousRemainder % 3 == 0:
            lookupIndex = (previousRemainder // 3) - 1
            if seq[lookupIndex] < minOperations:
                minOperations = seq[lookupIndex]
                remainder = previousRemainder // 3
        if previousRemainder % 2 == 0:
            lookupIndex = (previousRemainder // 2) - 1
            if seq[lookupIndex] < minOperations:
                minOperations = seq[lookupIndex]
                remainder = previousRemainder // 2
        lookupIndex = (previousRemainder - 1) - 1
        if seq[lookupIndex] < minOperations:
            minOperations = seq[lookupIndex]
            remainder = previousRemainder - 1
        
        multiplicativeSeq.append(remainder)
    return multiplicativeSeq



# When integer = n, the corresponding index in the vector sequence is (n - 1)
def optimal_sequence(n):
    remainder = n
    noOfOperationsSequence = [0] * (n)
    # index = 0, but the value itself is 1
    for i in range(1, n):
        # index = i; corresponding integer value = i + 1
        integer = i + 1
        noOfOperationsSequence[i] = float("inf")
        if integer % 3 == 0:
            lookup = 0 if integer // 3 == 1 else integer // 3 # To address base case where integer = 3
            if noOfOperationsSequence[lookup - 1] + 1 < noOfOperationsSequence[i]: # (lookup - 1) because while the index = i, the current integer iteration is (i + 1)
                noOfOperationsSequence[i] = noOfOperationsSequence[lookup - 1] + 1 
        if integer % 2 == 0:
            lookup = 0  if integer // 2 == 1 else integer // 2 # To address base case where integer = 2
            if noOfOperationsSequence[lookup - 1] + 1 < noOfOperationsSequence[i]:
                noOfOperationsSequence[i] = noOfOperationsSequence[lookup - 1] + 1 
        if noOfOperationsSequence[i - 1] + 1 < noOfOperationsSequence[i]:
            noOfOperationsSequence[i] = noOfOperationsSequence[i - 1] + 1
        

    # Backtrack to obtain the sequence of multiplication
    multSeq = backtrack(n, noOfOperationsSequence)

    return reversed(multSeq)

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
