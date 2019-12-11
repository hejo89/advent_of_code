from math import *
from collections import defaultdict
import matplotlib.pyplot as plt
asteroids = []
gaps = []
with open("input.txt", "r") as f:
    for y, i in enumerate(f):
        for x, j in enumerate(i.strip()):
            if j == "#": asteroids.append((x, y))
            if j == ".": gaps.append((x, y))
#for j in open("input2.txt"): print(j)

m = 0, 0
for p in asteroids:
    r = []
    for q in asteroids:
        if q == p: continue
        r.append(atan2(p[0] - q[0], p[1] - q[1]))
    if len(set(r)) > m[0]: m = len(set(r)), p

print(m)

m = m[1]
test = []

for q in asteroids:
    if q !=m:
        if atan2(-m[1] + q[1], -m[0] + q[0])+pi/2 < 0: test.append((atan2(-m[1] + q[1], -m[0] + q[0])+pi/2 + 2*pi,abs(m[0] - q[0])+abs(m[1] - q[1]), q))
        else: test.append((atan2(-m[1] + q[1], -m[0] + q[0])+pi/2,abs(m[0] - q[0])+abs(m[1] - q[1]), q))

d = defaultdict(list)

for j in test:
    d[j[0]].append(j[1:])

a = sorted(d.keys()) + [j for j in d if len(d[j]) > 1]
for i in range(200): 
    tmp = d[a[i]].pop()

print(tmp[1][0] * 100 + tmp[1][1])


x, y = [j[0] for j in asteroids], [-j[1] for j in asteroids]
u, v = [j[0] for j in gaps], [-j[1] for j in gaps]
plt.plot(x, y, "bo", color = 'black')
plt.plot(u, v, "bo", color = 'white')
plt.plot(*(m[0], -m[1]), "bo", color = 'red')
plt.show()
