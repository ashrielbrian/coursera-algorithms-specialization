# python3

# Algorithm mimics a set of a number of available parallel worker processes and jobs presented to it.
# Algo efficiently assigns the workers to the jobs via a (priority) min-heap queue method.
# Priority is given: 1. to the first available worker; 2. to the lowest-indexed worker

# Optimised by: Removing the Worker class. 

class Node:
    # Class to indicate the position of a Worker within the Min-Heap Tree
    def __init__(self, i, minHeap):
        self.worker = minHeap[i]
        self.leftChildIndex = 2 * i + 1
        self.rightChildIndex = 2 * i + 2

        try:
            self.leftChild = minHeap[self.leftChildIndex]
        except IndexError:
            self.leftChild = [float("inf"), float("inf")]
        
        try:
            self.rightChild = minHeap[self.rightChildIndex]
        except IndexError:
            self.rightChild = [float("inf"), float("inf")]

class HeapBuilder:
    def __init__(self, noOfWorkers):
        # the index of workers represents the index location of each node in a tree, from L - R.
        # For each worker, the first index represents its priority (where the lower the priority, the greater its importance)
        # and the second index represents its next available time.
        self.workers = [[i, 0] for i in range(noOfWorkers)] 

    def siftDown(self, i):
        # Function ensures min-heap property is satisfied
        node = Node(i, self.workers)

        if node.leftChild[1] == node.rightChild[1]:
            smallerChild = node.leftChild if node.leftChild[0] < node.rightChild[0] else node.rightChild
        else:
            smallerChild = node.leftChild if node.leftChild[1] < node.rightChild[1] else node.rightChild

        # the if-else below checks which child (l or r) is the smaller
        if (smallerChild[0] == node.leftChild[0]):
            smallerChildIndex = node.leftChildIndex
        else:
            smallerChildIndex = node.rightChildIndex

        # the if-else below checks whether child/parent has a smaller availability; if equal, then to check which has a higher priorityIndex
        if (smallerChild[1] < node.worker[1]) or ((smallerChild[1] == node.worker[1]) and (smallerChild[0] < node.worker[0])):
            self.swapParentAndChild(i, node.worker, smallerChildIndex, smallerChild)
            self.siftDown(smallerChildIndex)
        return
    
    def swapParentAndChild(self, parentIndex, parent, childIndex, child):
        # swapping the child as the new parent
        self.workers[parentIndex], self.workers[childIndex] = child, parent

    def extractMin(self):
        return self.workers[0]

    def beginWork(self, workerIndex, timeProcessTakes):
        self.workers[workerIndex][1] += timeProcessTakes
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

            self.assigned_workers.append(worker[0])
            self.start_times.append(worker[1])
            self.allWorkers.beginWork(0, timeJobTakes)

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()