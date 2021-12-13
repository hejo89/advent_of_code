arr = open("input").read().strip().split("\n")
import matplotlib.pyplot as plt
a = []
b = []
idx = 0

while True:
    if arr[idx] == "": break
    a.append(list(map(int, arr[idx].split(","))))
    idx += 1

idx += 1

while idx < len(arr):
    x, y = arr[idx].split(" ")[2].split("=")
    idx += 1
    b.append((x, int(y)))

def foo(fold, z):
    if fold == "y":
        for i, j in enumerate(a):
            if j[1] > z: a[i][1] = 2*z - j[1]
    if fold == "x":
        for i, j in enumerate(a):
            if j[0] > z: a[i][0] = 2*z - j[0]

for i, j in enumerate(b):
    foo(j[0], j[1])
    if i == 0: print(len(set(map(tuple, a))))

plt.plot(*zip(*a), "bo", ms = 20)
plt.gca().invert_yaxis()
plt.show()
