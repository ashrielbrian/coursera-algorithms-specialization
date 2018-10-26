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

# IMPORTANT: There are two parents in the below data structure. The first parent index refers to the Disjoint Set Parent;
# the second index refers to the actual/true Table parent (its business logic, if you will)
n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split())) # no. of rows per each table; index gives the table no.
rank = [1] * n

# By having each node contain two pieces of information, the directionality of each merge operation is conserved:
# i.e. the true parent of each table will always be known.
parent = [[x, x] for x in range(0, n)] # first index represents the Disjoint Set Parent; second index represents the True Table Parent
ans = max(lines)

def getParentRecursive(table):
    # Gets root
    if table != parent[table][0]:
        # Path compression
        parent[table][0] = getParentRecursive(parent[table][0])
    return parent[table][0]

def getParentIterative(table):
    # Iterative method of obtaining root.
    stack = []
    while table != parent[table][0]:
        stack.append(table)
        table = parent[table][0]

    # Path compression
    while len(stack) != 0:
        index = stack.pop()
        parent[index][0] = table
    
    return table

def merge(destination, source):
    global ans
    # destinationParent/sourceParent refer to the Disjoint Set Parent
    destinationParent, sourceParent = getParentRecursive(destination), getParentRecursive(source)

    # realDestionationParent, realSourceParent refer to the True Table Parent
    realDestinationParent, realSourceParent = parent[destinationParent][1], parent[sourceParent][1]

    if realDestinationParent == realSourceParent: # if dest. and source are in the same set
        return
    
    # if set source is shorter than dest, the parent of source is now dest (i.e. hang source under dest)
    if rank[destinationParent] > rank[sourceParent]:
        # Sets the disjoint and true parent of source to point to the new Destination Parent
        
        parent[source][0], parent[sourceParent][0] = destinationParent, destinationParent  
    else:
        parent[destination][0], parent[destinationParent][0] = sourceParent, sourceParent
        # Union by rank heuristic
        if rank[destinationParent] == rank[sourceParent]:
            rank[sourceParent] += 1
    # Sets the disjoint parent and current source node to point to the true table.
    # This ensures each disjoint parent of a tree (i.e. its root) will contain 
    # the true table of a given disjoint set tree.
    parent[source][1], parent[sourceParent][1] = realDestinationParent, realDestinationParent

    # Merge table; add rows.
    lines[realDestinationParent] += lines[realSourceParent]
    lines[realSourceParent] = 0

    # Outputs max rows.
    ans = max(ans, lines[realDestinationParent])
    return

for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    merge(destination - 1, source - 1)
    print (ans)
