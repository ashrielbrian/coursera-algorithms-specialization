from collections import deque

d = [deque() for _ in range(0, 5)]
d[3].appendleft(1)
d[3].appendleft(2)
d[3].appendleft(3)
d[3].append(1)

print(d[1].maxlen)
print(d)

e = [deque() for _ in range(0, 5)]
e[2].appendleft('world')
e[2].appendleft('hello')



def write_chain(chain):
    print(' '.join(chain))
write_chain(each for each in e[2])

e[1].append("10")
e[1].append("5")
e[1].append("2")
e[1].append("99")


diff = 10 - 3
for x in range(diff - 1, -1, -1):
    print(x)