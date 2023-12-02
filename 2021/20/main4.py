import collections

def neighbours(i, j):
    n = []
    for x in range(-1, 2):
        for y in range(-1, 2):
            n.append((i + x, j + y))
    return n

conv = {(0, 0): 0, (0, 1): 1, (0, 2): 2, (1, 0): 3, (1, 1): 4, (1, 2): 5, (2, 0): 6, (2, 1): 7, (2, 2): 8}

s = ""
b = []
a = open("input").read().split("\n")[:-1]
for i, j in enumerate(a):
    if j != "": s += j
    else: break

for j in a[i+1:]:
    b.append(list(j))

g = set()
for i in range(len(b)):
    for j in range(len(b[0])):
        if b[i][j] == "#":
            g.add((i, j))

def enhance(g, iteration = 0):
    if iteration == 2: return len(g)
    d = collections.defaultdict(list)
    for x, y in g:
        for j in neighbours(x, y):
            p, q = j
            d[j].append((x-p+1, y-q+1))
    g = set()
    for j in d:
        arr = ["0"]*9
        for k in d[j]:
            arr[conv[k]] = "1"
        if s[int("".join(arr), 2)] == "#": g.add(j)

    return enhance(g, iteration + 1)
            


print(enhance(g))
