import math
import matplotlib.pyplot as plt
with open('input.txt', 'r') as f:
    t = list(map(int, f.readline().strip().split()[1:]))
    d = list(map(int, f.readline().strip().split()[1:]))
r = 1
for i, j in enumerate(t):
    c = 0
    for k in range(j):
        if (j - k) * k > d[i]:
            c += 1
    r *= c
print(r)
t = int(''.join(list(map(str, t))))
d = int(''.join(list(map(str, d))))
print(math.floor(t/2 + pow(t**2 / 4 - d, 0.5)) - math.ceil(t/2  - pow(t**2 / 4 - d, 0.5) - 1))
