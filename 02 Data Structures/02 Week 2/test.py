y = [0] * 10
y[2] = 2
print (y)
print([x for x in range(0, 10)])

size = 5
print([k for k in range((size//2), -1, -1)])

class Worker:
    def __init__(self, name, value):
        self.name = name
        self.value = value

brian = Worker("brian", 10)
tang = Worker("tang", 12)

people = [brian, tang]
who = min(people, key=lambda p: p.value)
print(who.name, who.value)

a = 12
b = 11
c = 10
if (a < b) or ((a == b) and b > c):
    print (True)
else:
    print (False)

for i in range(2):
    print(i)
