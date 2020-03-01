# python3
from collections import deque

"""
    Algorithm builds and stores key-value pairs in a hash table using chaining.
    Supports the following commands:

    ∙ add string — insert string into the table. If there is already such string in the hash table, then
    just ignore the query.
    ∙ del string — remove string from the table. If there is no such string in the hash table, then
    just ignore the query.
    ∙ find string — output “yes" or “no" (without quotes) depending on whether the table contains
    string or not.
    ∙ check 𝑖 — output the content of the 𝑖-th list in the table. Use spaces to separate the elements of
    the list. If 𝑖-th list is empty, output a blank line.

    Inserting a new string into a hash chain inserts to the beginning of the chain.

    Input: There is a single integer 𝑚 in the first line — the number of buckets you should have. The
    next line contains the number of queries 𝑁. It’s followed by 𝑁 lines, each of them contains one query
    in the format described above. E.g. 
    5
    6
    add world
    add Hell0
    check 4
    find world
    del world
    add good

    Output: Print the result of each of the find and check queries, one result per line, in the same
    order as these queries are given in the input.
    
    Hash Table:
     _
    |0| ---> chain #1 (linked-list)
     -
     _
    |1| ---> chain #2
     -
     _
    |2| ---> chain #3
     -
     .
     .
     .
       _
    |m - 1| ---> chain #(m-1)
       -
"""

class Query:
    # Structures the query into accessible elements
    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]


class QueryProcessor:
    
    # Arbitrarily chosen cardinality (prime), and a multiplier for selecting
    # a hash function from the polynomial family.
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # Sets up the hash table of cardinality length. Each node is a linked-list (hence, chaining).
        self.elems = [deque() for _ in range(0, self.bucket_count)]

    def _hash_func(self, s):
        ans = 0
        for c in reversed(s):
            # ord() converts character to ASCII int code
            ans = (ans * self._multiplier + ord(c)) % self._prime
        final_answer = ans % self.bucket_count
        return final_answer

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        return Query(input().split())

    def process_query(self, query):
        if query.type == "check":
            # Locates and prints the entire chain of an associated node of index query.ind
            if self.elems[query.ind]:
                # Prints out the entire list of the i'th index of the hash table
                self.write_chain(eachElem for eachElem in self.elems[query.ind])
            else:
                print() # prints an empty line if the list is empty
        else:
            hashValue = self._hash_func(query.s)
            wasFound = self.find(hashValue, query.s)

            if query.type == 'find':
                self.write_search_result(wasFound)
            # Ignores the request to add if element already exists; deletes if already exists, do nothing otherwise.
            elif query.type == 'add':
                if not wasFound:
                    self.elems[hashValue].appendleft(query.s)
            elif query.type == 'del':
                if wasFound:
                    self.elems[hashValue].remove(query.s)


    def find(self, hashValue, s):
        # Checks if the element is already within the hash table
        if self.elems[hashValue]:
            for eachElem in self.elems[hashValue]:
                if s == eachElem:
                    return True
        return False
        
    def process_queries(self):
        n = int(input())
        for i in range(n):
             self.process_query(self.read_query())

if __name__ == '__main__':
    bucket_count = int(input())
    proc = QueryProcessor(bucket_count)
    proc.process_queries()

    
    