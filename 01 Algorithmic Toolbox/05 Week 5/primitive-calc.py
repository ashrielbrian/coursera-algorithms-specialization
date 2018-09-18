# Uses python3
import sys


# 1. Start the array with n
# 2. Check if remainder == 1
#   2a. Initialise the array's current sequence element
# 3. If not, we go through the three possible scenarios:
#   3a. Divide 3 and check if no remainder, AND whether 


def optimal_sequence(n):
    remainder = n
    i = 1
    sequence = [n]

    while remainder != 1:
        sequence.append(float("inf"))
        previousRemainder = remainder
        if previousRemainder % 3 == 0:
            if previousRemainder // 3 < sequence[i]:
                remainder = previousRemainder // 3
                sequence[i] = remainder
        elif previousRemainder % 2 == 0:
            if previousRemainder // 2 < sequence[i]:
                remainder = previousRemainder // 2
                sequence[i] = remainder
        else:
            remainder = previousRemainder - 1
            sequence[i] = remainder
        i += 1
    print (sequence)
    return sequence

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
