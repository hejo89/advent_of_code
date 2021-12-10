import collections
a = [map(int, list(j)) for j in open("input").read().split()]

b = [len(a) - 1, len(a[0]) - 1]
risk = 0
p = []
for x in range(len(a)):
    for y in range(len(a[0])):
        lp = True
        for c in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            i, j = min(max(0, x+c[0]), b[0]), min(max(0, y+c[1]), b[1])
            if (i, j) != (x, y) and a[x][y] >= a[i][j]: lp = False

        if lp:
            risk += 1 + a[x][y]
            p.append((x, y))

print(risk)

def foo(x, y):
    v = set([(x, y)])
    q = collections.deque([(x, y)])
    while q:
        n = q.popleft()
        x, y = n
        for c in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            i, j = min(max(0, x+c[0]), b[0]), min(max(0, y+c[1]), b[1])
            if (i, j) != (x, y) and a[i][j] != 9 and (i, j) not in v: 
                q.append((i, j))
                v.add((i, j))

    return v


r = []
for j in p: r.append(len(foo(*j)))
r.sort()
print(r[-1]*r[-2]*r[-3])
