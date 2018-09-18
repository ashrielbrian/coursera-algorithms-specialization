# Uses python3
import sys
import math

def binary_search(arrayToSearch, key):
    left, right = 0, len(arrayToSearch)
    if right <= left:
        return -1 # if the array is empty
    midpoint = math.floor(left + (right - left)/2)
    print('my midpoints', midpoint)
    
    
    if key == arrayToSearch[midpoint]:
        return midpoint
    elif key < arrayToSearch[midpoint]:
        print("Key is smaller, so the lower half array is: %s, with a key of %s" %(arrayToSearch[:midpoint], key))
        return binary_search(arrayToSearch[:midpoint], key)
    elif key > arrayToSearch[midpoint]:
        print("Key is larger, so the upper half array is: %s, with a key of %s" %(arrayToSearch[midpoint + 1:], key))
        return binary_search(arrayToSearch[midpoint + 1:], key)


def linear_search(arrayToSearch, key):
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
        print(binary_search(a, x), end = ' ')
