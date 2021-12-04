import datetime
import collections

a = sorted([[datetime.datetime.strptime(j[0][1:] + " " + j[1][:-1], "%Y-%m-%d %H:%M")] + [" ".join(j[2:])] for j in [j.strip().split() for j in open("input.txt")]])
#for j in a: print(j)
d = collections.defaultdict(list)
dd = collections.defaultdict(int)
i = 0
while i < len(a):
    if a[i][1][:5] == "Guard":
        k = 1
        while i + k < len(a) and a[i + k][1] == "falls asleep":
            d[a[i][1].split()[1]].append((a[i+k][0].minute, a[i+k+1][0].minute))
            k += 2 
        i += k

m = (0, '#')

for i in d:
    c = 0
    for j in d[i]:        
        c += j[1] - j[0]
    if c > m[0]: m = (c, i)

for j in d[m[1]]:
    for k in range(*j):
        dd[k] += 1

r = {}
for j in dd:
    r[dd[j]] = j

print(r[max(r)] * int(m[1][1:]))

ddd = collections.defaultdict(dict)
for i in d:
    for j in d[i]:
        for k in range(*j):
            if i in ddd[k]: ddd[k][i] += 1
            else: ddd[k][i] = 1


ddd = {j:{ddd[j][i]:i for i in ddd[j]} for j in ddd}
ddd = {max(ddd[j].keys()):(j, ddd[j][max(ddd[j].keys())]) for j in ddd}
t = ddd[max(ddd.keys())]
print(t[0] * int(t[1][1:]))
