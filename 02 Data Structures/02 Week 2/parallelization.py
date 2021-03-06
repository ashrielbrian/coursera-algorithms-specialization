# python3

# Optimised by: removing the lambda function that compares the workers priorityIndex and whenAvailable
class Worker:
    # Class to describe a Worker Thread
    def __init__(self, priorityIndex, whenAvailable):
        self.priorityIndex = priorityIndex # smaller index, greater importance
        self.whenAvailable = whenAvailable # the time the Worker is available to perform work

class Node:
    # Class to indicate the position of a Worker within the Min-Heap Tree
    def __init__(self, i, minHeap):
        self.worker = minHeap[i]
        self.leftChildIndex = 2 * i + 1
        self.rightChildIndex = 2 * i + 2

        try:
            self.leftChild = minHeap[self.leftChildIndex]
        except IndexError:
            self.leftChild = Worker(float("inf"), float("inf"))
        
        try:
            self.rightChild = minHeap[self.rightChildIndex]
        except IndexError:
            self.rightChild = Worker(float("inf"), float("inf"))

class HeapBuilder:
    def __init__(self, noOfWorkers):
        # the index of workers represents the index location of each node in a tree, from L - R.
        self.workers = [Worker(i, 0) for i in range(noOfWorkers)]

    def siftDown(self, i):
        # Function ensures min-heap property is satisfied
        node = Node(i, self.workers)

        if node.leftChild.whenAvailable == node.rightChild.whenAvailable:
            smallerChild = node.leftChild if node.leftChild.priorityIndex < node.rightChild.priorityIndex else node.rightChild
        else:
            smallerChild = node.leftChild if node.leftChild.whenAvailable < node.rightChild.whenAvailable else node.rightChild

        # the if-else below checks which child (l or r) is the smaller
        if (smallerChild.priorityIndex == node.leftChild.priorityIndex):
            smallerChildIndex = node.leftChildIndex
        else:
            smallerChildIndex = node.rightChildIndex

        # the if-else below checks whether child/parent has a smaller availability; if equal, then to check which has a higher priorityIndex
        if (smallerChild.whenAvailable < node.worker.whenAvailable) or ((smallerChild.whenAvailable == node.worker.whenAvailable) and (smallerChild.priorityIndex < node.worker.priorityIndex)):
            self.swapParentAndChild(i, node.worker, smallerChildIndex, smallerChild)
            self.siftDown(smallerChildIndex)
        return
    
    def swapParentAndChild(self, parentIndex, parent, childIndex, child):
        # swapping the child as the new parent
        self.workers[parentIndex], self.workers[childIndex] = child, parent

    def extractMin(self):
        return self.workers[0]

    def beginWork(self, workerIndex, timeProcessTakes):
        self.workers[workerIndex].whenAvailable += timeProcessTakes
        self.siftDown(workerIndex)
        return


class JobQueue:
    def read_data(self):

        self.num_workers, m = map(int, input().split())
        self.allWorkers = HeapBuilder(self.num_workers)

        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
          print(self.assigned_workers[i], self.start_times[i]) 

    def assign_jobs(self):
        
        self.assigned_workers = []
        self.start_times = []
        
        for i in range(len(self.jobs)):
            timeJobTakes = self.jobs[i]
            worker = self.allWorkers.extractMin()

            self.assigned_workers.append(worker.priorityIndex)
            self.start_times.append(worker.whenAvailable)
            self.allWorkers.beginWork(0, timeJobTakes)

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()
