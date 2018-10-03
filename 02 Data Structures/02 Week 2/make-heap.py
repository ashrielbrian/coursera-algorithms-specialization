# python3

# In-place Min-Heap Builder
class Node:
    # Class for any specific node within the Binary Tree
    def __init__(self, i, data):
        self.value = data[i]
        self.leftChildIndex = 2 * i + 1
        self.rightChildIndex = 2 * i + 2

        # Checks for the possibility if there are no children for that specific node.
        # If there are no children, avoids the IndexError by creating an infinite value child,
        # to ensure the min-heap property continues to be satisfied during siftDown. No impact on original data structure.
        try:
            self.leftChild = data[self.leftChildIndex]
        except IndexError:
            self.leftChild = float("inf")
        
        try:
            self.rightChild = data[self.rightChildIndex]
        except IndexError:
            self.rightChild = float("inf")

class HeapBuilder:
    def __init__(self):
        self._swaps = []
        # the index of ._data represents the index location of each node in a tree, from L - R.
        self._data = []

    def ReadData(self):
        n = int(input())
        self._data = [int(s) for s in input().split()]
        assert n == len(self._data)

    def WriteResponse(self):
        print(len(self._swaps))
        for swap in self._swaps:
            print(swap[0], swap[1])

    def siftDown(self, i):
        # Function ensures min-heap property is satisfied
        node = Node(i, self._data)
        smallerChild = min(node.leftChild, node.rightChild)
        
        if smallerChild < node.value:
            self._data[i] = smallerChild # swapping the child as the new parent
            if (smallerChild == node.leftChild):
                smallerChildIndex = node.leftChildIndex
                self._data[node.leftChildIndex] = node.value
            elif (smallerChild == node.rightChild):
                smallerChildIndex = node.rightChildIndex
                self._data[node.rightChildIndex] = node.value
            self._swaps.append([i, smallerChildIndex])
            self.siftDown(smallerChildIndex)
        return

    def GenerateSwaps(self):
        size = len(self._data)
        # Iterate from size/2 to 1, sifting down each element
        for k in range((size//2), -1, -1):
            self.siftDown(k)

    def Solve(self):
        self.ReadData()
        self.GenerateSwaps()
        self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
