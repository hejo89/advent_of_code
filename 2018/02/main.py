import collections
two, three = 0, 0
with open("input.txt", "r") as f:
    for l in f:
        tmp = list(l.strip())
        d = collections.defaultdict(int)
        for j in tmp: d[j] += 1
        s = set(d.values())
        if 2 in s: two   += 1
        if 3 in s: three += 1

print(two * three)

m = 0
a = [j.strip() for j in open("input.txt")]
for i, j in enumerate(a):
    for k in a[i+1:]:
        idx, c = -1, 0
        for x, y in enumerate(j):
            if c > 1: break
            if y != k[x]: c += 1; idx = x
            
        if c == 1: print(j[:idx]+j[idx+1:])
