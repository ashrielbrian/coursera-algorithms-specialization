# Uses python3
# Binary Search Algorithm: Takes two arrays as an input. The first is a sorted array, the second is an array with
# elements we desire to obtain the location of in the first array. The function returns the index position of the
# given element in the first array.
import sys
import math

# Binary Search works by constantly checking the mid point element of a subarray. If the key is smaller or greater,
# than the midpoint element, the subarray is broken up accordingly, either all elements smaller than the midpoint
# or all elements greater. The algo thus solves recursively by constantly halving each of the array until either
# two of the base cases are met.

def binary_search(arrayToSearch, key, left, right):
    # Base Case #1
    if right <= left:
        return -1 # Returns -1 if the array is empty (i.e. the element cannot be found in the array)
    midpoint = math.floor(left + (right - left)/2)
        
    if key == arrayToSearch[midpoint]: # Base Case #2
        return midpoint
    elif key < arrayToSearch[midpoint]: # Recursive calls
        return binary_search(arrayToSearch, key, left, midpoint)
    elif key > arrayToSearch[midpoint]:
        return binary_search(arrayToSearch, key, midpoint + 1, right)

def linear_search(arrayToSearch, key): # Linear search of O(n^2)
    for i in range(len(arrayToSearch)):
        if arrayToSearch[i] == key:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1] # array to search
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, x, 0, len(a)), end = ' ')
