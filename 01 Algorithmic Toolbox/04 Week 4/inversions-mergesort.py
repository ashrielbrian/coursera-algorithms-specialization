# Uses python3
import sys

# Merge(B, C) should return a resulting sorted array 
# where b { B, c { C,
# and b > c

# mergeSort(A) returns a sorted array as A' and the number of inversions

def mergeAndCount(B, C):
    sortedArray = []
    numberOfInversions = 0
    while B or C: # while either array have elements
        #print ("This is the sorted array from mergeAndCount: ", sortedArray)
        if B and not C:
            # if C is empty, but B isn't
            sortedArray.append(B.pop(0))
        elif C and not B:
            # if B is empty, but C isn't
            sortedArray.append(C.pop(0))
        elif not B and not C:
            # if both empty
            break
        else:
            # there are elements in both arrays 
            b = B[0]
            c = C[0]
            if b <= c:
                sortedArray.append(B.pop(0)) # .pop(0) removes the first element from the list, and returns its element
            else: 
                # if b > c
                noOfCurrentInversions = len(B) * 1 
                # Because if b is > c, then every other element in B after b, will also be greater than c
                # Hence we need to multiply 1 (for each inversion) with the length of B, ie all remaining elements in B
                numberOfInversions += noOfCurrentInversions
                sortedArray.append(C.pop(0))
    return (sortedArray, numberOfInversions)

    

def get_number_of_inversions(a, left, right):
    a = a[left:right]
    left, right = 0, len(a) # reset-ing the (left, right) variables so it is accurate for recursions of the upper halves
    # print (a)
    number_of_inversions = 0
    if right - left <= 1:
        return a, number_of_inversions
    ave = (left + right) // 2
    B, number_of_B_inversions = get_number_of_inversions(a, left, ave)
    number_of_inversions += number_of_B_inversions

    C, number_of_C_inversions = get_number_of_inversions(a, ave, right)
    number_of_inversions += number_of_C_inversions

    sortedArray, number_of_initial_inversions = mergeAndCount(B, C)
    number_of_inversions += number_of_initial_inversions
    #print ("Sorted array from this recursion call is %s, and number of inversions of %s" %(sortedArray, number_of_inversions))
    return sortedArray, number_of_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    array, inversions = get_number_of_inversions(a, 0, len(a))
    print (inversions)