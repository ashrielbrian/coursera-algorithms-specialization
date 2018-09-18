# Uses Python 3

import sys

def gcdEfficient(a, b):
    if b == 0:
        return a
    aPrime = a % b
    return gcdEfficient(b, aPrime)

def lcmEfficient(a, b):
    gcd = gcdEfficient(a, b)
    # LCM of two integers is the product of the two divided by the greatest common divisor
    return int((a * b) // gcd)

inputs = sys.stdin.read()
tokens = [int(x) for x in inputs.split()]
print (lcmEfficient(tokens[0], tokens[1]))
#print (lcmEfficient(226553150, 1023473145))