# python3

import sys, threading, math
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class Node:
        def __init__(self):
                self.childrenNodes = []
        def addChild(self, child):
                self.childrenNodes.append(child)
        def readChildren(self):
                return self.childrenNodes
        

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))
                self.allNodes = [[] for _ in range(self.n)] # "an array whose index is the label of the node"

                for childIndex in range(0, self.n):
                        
                        # the index i is the child node
                        parentNode = self.parent[childIndex]
                        if parentNode == -1:
                                self.root = childIndex # IMPORTANT: Amend
                        else:
                                self.allNodes[parentNode].append(childIndex)
                # print (self.allNodes)
                                
        # [R, 0, 4, 0, 3] is the parent of
        # [0, 1, 2, 3, 4]

        def compute_height(self, node):
                maxHeight = 0
                if not self.allNodes[node]:
                        # Base Case: if the list is empty, i.e. there are no child nodes
                        return 0
                for childNode in self.allNodes[node]:
                        maxHeight = max(self.compute_height(childNode), maxHeight)
                return maxHeight + 1

def main():
        tree = TreeHeight()
        tree.read()

        print(tree.compute_height(tree.root) + 1)

threading.Thread(target=main).start()