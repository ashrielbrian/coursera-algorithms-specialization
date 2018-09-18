# Uses python3
import sys
import random

# Partition 3 is specifically useful when it is known that the data set consists of many duplicate numbers
def partition3(a, l, r):
    # returns two indices, m1 and m2. where A[m1] = A[x] = A[m2], and m1 < x < m2
    x = a[l]
    j = l
    k = j
    # See my Notes in Data Science booklet for a clearer understanding of this code
    for i in range(l + 1, r + 1):
        if a[i] == a[l]:
            k += 1
            a[k], a[i] = a[i], a[k]
        elif a[i] < a[l]:
            j += 1
            k += 1
            a[j], a[k] = a[k], a[j]
            if i != k: 
                # this if condition is extremely important to ensure that we do not accidentally swap
                # elements when the "greater than pivot" region is not yet constructed.
                a[j], a[i] = a[i], a[j]
    a[l], a[j] = a[j], a[l]
    return (j, k)



def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    #print ('Current array is %s, with a starting random int of: %s' %(a, k))
    a[l], a[k] = a[k], a[l]
    #use partition3
    m1, m2 = partition3(a, l, r)
    randomized_quick_sort(a, l, m1 - 1);
    randomized_quick_sort(a, m2 + 1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')