import heapq

a = [map(int, 5 * list(j.strip())) for _ in range(5) for j in open("input")]

for i in range(len(a)):
    for j in range(len(a[0])):
        a[i][j] += i//(len(a) // 5) + j//(len(a[0]) // 5)
        if a[i][j] > 9: a[i][j] = a[i][j] % 10 + 1

def clamp(x, y):
    return min(max(0, x), len(a) - 1), min(max(0, y), len(a[0]) - 1)

def adjacent(x, y):
    s = set()
    s.add(clamp(x + 1, y))
    s.add(clamp(x - 1, y))
    s.add(clamp(x, y + 1))
    s.add(clamp(x, y - 1))
    if (x, y) in s: s.remove((x, y))
    return s

uv = set([(0, 0)])
d  = {}

for i in range(len(a)):
    for j in range(len(a[0])):
        d[(i, j)] = float('inf')
        uv.add((i, j))

d[(0, 0)] = 0

pq = [(0, (0, 0))]
heapq.heapify(pq)

while pq:
    c = heapq.heappop(pq)
    if c[1] not in uv: continue
    for n in adjacent(*c[1]):
        i, j = n
        if d[c[1]] + a[i][j] < d[n]: d[n] = d[c[1]] + a[i][j]
        heapq.heappush(pq, (d[n], n))
    uv.remove(c[1])

print(d[((len(a) // 5) - 1, (len(a[0]) // 5) - 1)])
print(d[(len(a) - 1, len(a[0]) - 1)])
