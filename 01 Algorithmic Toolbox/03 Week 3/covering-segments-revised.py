# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):

    points = []
    # Sort according to the end points of each segment in ascending order
    sortedSegments = sorted(segments, key=lambda segment: segment.end)
    requiredPoint = sortedSegments[0].end
    points.append(requiredPoint)

    # Iterate through each segment in list
    for i in range(len(sortedSegments)):
        currentSegment = sortedSegments[i]
        # If the segment in question is outside the range of the selected coordinate, we choose this new segment end coordinate as the next required point
        if (requiredPoint < currentSegment.start or requiredPoint > currentSegment.end):
            requiredPoint = currentSegment.end
            points.append(requiredPoint)
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')