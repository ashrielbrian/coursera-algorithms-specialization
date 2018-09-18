# Uses python3
import sys
import math

def isMajority(noOfElements, total):
    percent = noOfElements / total
    print (percent)
    if percent > 0.5:
        return True
    return False

def countMajority(a, left, right, countKey):
    count = 0
    print ('----> The array being counted: %s, with a key of %s,' %(a, countKey))
    for i in range(len(a)):
        if a[i] == countKey:
            count += 1
    if isMajority(count, len(a)):
        return countKey
    return -1

def get_majority_element(a, left, right):
    print ("----- START OF RECURRECE ----- \n")
    print ("Current array is", a)
    print ("The left index is %s, and the right index is %s" %(left, right))
    countKey = -1
    if left == right: # if there is only a single element left in the array
        return -1
    if left + 1 == right: # if there are only two elements left in the array
        print ('-> Returned a[left] as', a[0])
        return a[0]
    
    mid = math.floor(left + (right - left)/2)
    lower = get_majority_element(a[left: mid + 1], left, mid)
    # upper = get_majority_element(a[mid + 1:], mid + 1, right)
    upper = get_majority_element(a[mid + 1:], 0, len(a[mid + 1:]) - 1)


    if lower != -1:
        countKey = lower
    elif upper != -1:
        countKey = upper
    # finalMajority = countMajority(a[left: right + 1], left, right, countKey)
    finalMajority = countMajority(a[left:], left, right, countKey)

    print ('This recurrence final majority', finalMajority)
    return finalMajority
    
if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n - 1) != -1:
        print(1)
    else:
        print(0)
