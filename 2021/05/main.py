import collections

d = collections.defaultdict(int)
a = [[map(int, i.split(",")) for i in j.strip().split(" -> ")] for j in open("input.txt")]
for c in a:
    u, v, x, y = c[0][0], c[1][0], c[0][1], c[1][1]
    if u == v or x == y:
        for i in range(min(u, v), max(u, v) + 1):
            for j in range(min(x, y), max(x, y) + 1):
                d[(i, j)] += 1

    # part 2
    if abs(u - v) == abs(x - y):
        for i in range(abs(u - v) + 1):
            if v > u and y > x: d[(u + i, x + i)] += 1
            if v > u and y < x: d[(u + i, x - i)] += 1
            if v < u and y > x: d[(u - i, x + i)] += 1
            if v < u and y < x: d[(u - i, x - i)] += 1


print(sum(1 for j in d if d[j] > 1))

