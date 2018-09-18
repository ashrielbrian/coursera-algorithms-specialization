# Uses Python 3

import sys

def gcdEfficient(a, b):
    if b == 0:
        return a
    aPrime = a % b
    return gcdEfficient(b, aPrime)

inputs = sys.stdin.read()
tokens = [int(x) for x in inputs.split()]
print(gcdEfficient(tokens[0], tokens[1]))
