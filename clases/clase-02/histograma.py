import random
l = []

for i in range(10000):
    l.append(random.randint(0,99))

d = {}

for i in range(99):
    d[i] = l.count(i)

print(d)
