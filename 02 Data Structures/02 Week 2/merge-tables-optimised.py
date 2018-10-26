# python3
import sys

""" Algorithm simulates a sequence of merge operations with tables in a database.
- Uses disjoint data structure
- TASK: There are 𝑛 tables stored in some database. The tables are numbered from 1 to 𝑛. All tables share
the same set of columns. Each table contains either several rows with real data or a symbolic link to
another table. Initially, all tables contain data, and 𝑖-th table has 𝑟𝑖 rows.
You need to perform 𝑚 of the following operations:
    1. Consider table number 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖. Traverse the path of symbolic links to get to the data. That is,
    while 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖 contains a symbolic link instead of real data do
    𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖 ← symlink(𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖)
    2. Consider the table number 𝑠𝑜𝑢𝑟𝑐𝑒𝑖 and traverse the path of symbolic links from it in the same
    manner as for 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖.
    3. Now, 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖 and 𝑠𝑜𝑢𝑟𝑐𝑒𝑖 are the numbers of two tables with real data. If 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖 ̸=
    𝑠𝑜𝑢𝑟𝑐𝑒𝑖, copy all the rows from table 𝑠𝑜𝑢𝑟𝑐𝑒𝑖 to table 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖, then clear the table 𝑠𝑜𝑢𝑟𝑐𝑒𝑖
    and instead of real data put a symbolic link to 𝑑𝑒𝑠𝑡𝑖𝑛𝑎𝑡𝑖𝑜𝑛𝑖 into it.
    4. Print the maximum size among all 𝑛 tables (recall that size is the number
"""
## IMPORTANT: Difference between this algorithm and "merge-tables.py" is this algo's directionality
# is not conserved. There is no distinction between the destionation/source of the merged tables. 
# All the algorithm is concerned for is to output the largest number of rows.
# This implies this algorithm is only useful for passing the assignment, but no real practical use.

# IMPORTANT: There are two parents in the below data structure. The first parent index refers to the Disjoint Set Parent;
# the second index refers to the actual/true Table parent (its business logic, if you will)
n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split())) # no. of rows per each table; index gives the table no.
rank = [1] * n
parent = list(range(0, n))


def getParentRecursive(table):
    if table != parent[table]:
        parent[table] = getParentRecursive(parent[table])
    return parent[table]

def getParentIterative(table):
    stack = []
    while table != parent[table]:
        stack.append(table)
        table = parent[table]

    while len(stack) != 0:
        index = stack.pop()
        parent[index] = table
    return table

def merge(destination, source):
    # destinationParent/sourceParent refer to the Disjoint Set Parent
    destinationParent, sourceParent = getParentRecursive(destination), getParentRecursive(source)

    if destinationParent == sourceParent: # if dest. and source are in the same set
        return max(lines)

    if rank[destinationParent] > rank[sourceParent]: # if set source is shorter than dest, the parent of source is now dest (i.e. hang source under dest)
        parent[sourceParent] = destinationParent
        lines[destinationParent] += lines[sourceParent]
        lines[sourceParent] = 0
    else:
        parent[destinationParent] = sourceParent
        lines[sourceParent] += lines[destinationParent]
        lines[destinationParent] = 0
        if rank[destinationParent] == rank[sourceParent]:
            rank[sourceParent] += 1
    
    return max(lines)

for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    print(merge(destination - 1, source - 1))