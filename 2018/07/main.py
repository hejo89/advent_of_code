import collections

a, b = collections.defaultdict(list), collections.defaultdict(list)
with open ("input.txt") as f:
    for l in f:
        l = l.strip().split(" ")
        a[l[1]].append(l[7])
        b[l[7]].append(l[1])


# part 1

r = ""
q = set(a) - set(b)
while q:
    x = min(q)
    r += x
    q.remove(x)
    for y in a[x]:
        b[y].remove(x)
        if not b[y]: q.add(y)

print(r)

