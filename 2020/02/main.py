from collections import defaultdict
arr = []
with open("input.txt", "r") as f:
    for l in f:
        tmp = l.strip().split(":")
        arr.append(map(int, tmp[0].split(" ")[0].split("-")) + [tmp[0].split(" ")[1]] + [tmp[1].lstrip()])


#c = 0
#for p in arr:
#    d = defaultdict(int)
#    for j in p[3]: d[j] += 1
#    if d[p[2]] >= p[0] and d[p[2]] <= p[1]: c += 1

#print c 
print arr
c = 0
for p in arr:
    print p
    if ((p[3][p[0] - 1] == p[2])^(p[3][p[1] - 1] == p[2])): c += 1

print c

