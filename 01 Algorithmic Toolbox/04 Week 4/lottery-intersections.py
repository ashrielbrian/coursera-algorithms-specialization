# Uses python3
import sys

# Algorithm finds the number of segments a given point lies within.
# The input is a number of points and segments.

def fast_count_segments(starts, ends, points):
    count = [0] * len(points)
    # starts - var containing the starting points of all the segments
    # ends - var containing the end points of all segments

    # Create a combined array of all starts, ends and points - labelling them as "p", "l", "r"
    # for points, left and right respectively
    
    pointIndex = 0
    combinedArray = [[x, "l"] for x in starts]
    for each in ends:
        combinedArray.append([each, "r"])
    for each in points:
        combinedArray.append([each, "p", pointIndex])
        pointIndex += 1

    # sorts first by the coordinate, then by the element type, where if the coordinates are equal, "p" will come before "r"
    sortedArray = sorted(combinedArray, key=lambda each: (each[0], each[1]))

    # Keep track of the number of l's and r's
    # The (l - r) value will indicate how many segments the current element is in
    l, r = 0, 0
    for eachElement in sortedArray:
        elementType = eachElement[1]
        if elementType == "l":
            l += 1
        elif elementType == "r":
            r += 1
        else:
            # element is a point
            currentPointIndex = eachElement[2]
            count[currentPointIndex] = l - r
    return count

def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')