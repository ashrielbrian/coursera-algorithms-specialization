# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')
SegmentWithLength = namedtuple('SegmentWithLength', 'start end length')
Counter = namedtuple('Counter', 'coordinate noOfIntersections')

# IMPORTANT: WHY THIS ALGORITHM WILL NECESSARILY FAIL
# This algo weighs every single coordinate with the same number of intersection points equally. Unfortunately, some intersection points will
# matter more than the others, that is, the selection permutation of coords with the same number of intersection points DO matter.
# Selecting the correct FIRST coord with the highest number of intersection points will influence the final number of points.
# Try the following inputs and compare to covering-segments-revised.py

# 5
# 8 9
# 9 10
# 10 11
# 11 12
# 10 19
# This will give an output of 3: 10 8 11.
# This could go better under covering-segments-revised.py, which outputs 2: 9 and 11

def getIntersectionPoints(list):

    # Big-O of n: 10^9 * 10^2
    smallestCoord = min([segment.start for segment in list])
    largestCoord = max([segment.end for segment in list])
    arrayOfCounters = []
    # Go across every single coordinate
    for i in range(smallestCoord, largestCoord + 1): # i is the coordinate
        counter = 0
        # Go downwards every single line
        for j in range(len(list)): # j is the index
            currentSegment = list[j]
            if (currentSegment.start <= i <= currentSegment.end):
                counter += 1
        arrayOfCounters.append(Counter(i, counter))
    return sorted(arrayOfCounters, key=lambda counter: counter.noOfIntersections, reverse=True)


def optimal_points(segments):

    #segmentsWithLengths = list(map(lambda segment: SegmentWithLength(segment.start, segment.end, segment.end - segment.start), segments))
    sortedSegments = sorted(segments, key=lambda segment: segment.end)
    remainingSegments = sortedSegments
    keepGoing = True
    points = []

    while keepGoing:
        arrayOfCounters = getIntersectionPoints(remainingSegments) # max iterations of n = 100
        #print(arrayOfCounters)
        coordWithMostIntersections = arrayOfCounters[0].coordinate
        requiredCoordinate = coordWithMostIntersections
        points.append(requiredCoordinate)
       
        # Remove the segments that has the points 
        remainingSegments = [segment for segment in remainingSegments if requiredCoordinate < segment.start or requiredCoordinate > segment.end]
        if len(remainingSegments) == 0:
            keepGoing = False
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
