# Uses Python 3
import sys

inputs = sys.stdin.read()
# Converts each input into an integer
tokens = [int(x) for x in inputs.split()]

# Max Pairwise Algorithm where the first integer in the user input is the number of integers in an array.
# Algo calculates the maximum product of a pair of numbers.

# The array is scanned through once to locate first the largest integer. Then removes it from the array.
# Array is scanned a second time through to locate the second largest integer. O(n) -- linear.
number_of_integers = tokens[0]
list_of_integers = tokens[1: number_of_integers + 1]

largest = max(list_of_integers)

# remove largest value from list
list_of_integers.remove(largest)

second_largest = max(list_of_integers)

print (largest * second_largest)
