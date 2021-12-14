import collections
p = ""
t = {}
with open("input", "r") as f:
    p = f.readline().strip()
    f.readline()
    for l in f:
        a, b = l.strip().split(" -> ")
        t[a] = b

d = collections.defaultdict(int)
c = collections.defaultdict(int)

for i in range(len(p) - 1):
    d[p[i:i+2]] += 1

for j in p:
    c[j] += 1

steps = 0
while steps < 40:
    tmp = {j:d[j] for j in d if d[j] > 0}
    for j in tmp:
        if j in t:
            c[t[j]]        += tmp[j] 
            d[j]           -= tmp[j]  
            d[j[0] + t[j]] += max(tmp[j], 1)
            d[t[j] + j[1]] += max(tmp[j], 1)

    steps += 1
    if steps == 10 or steps == 40:
        print(max(c.values()) - min(c.values()))
