import collections
g = collections.defaultdict(list)

a = open("input").read().split()

for x in a:
    y, z = x.split("-")
    if y != "end" and z != "start":
        g[y].append(z)
    if z != "end" and y != "start":
        g[z].append(y)


v = set("start")
s = [["start", 0]]
path = []
c = 0
while s:
    t = s.pop()
    if not path: path.append(t)
    elif t[1]>path[-1][1]: path.append(t)
    else:
        while t[1] <= path[-1][1]:
            path.pop()
        path.append(t)
    if not g[t[0]] and path[-1][0] == "end":
#        print("-".join(list(zip(*path))[0]))
        c += 1

    d = collections.defaultdict(int)
    for j in path:
        if j[0] != "end" and j[0] != "start" and ord(j[0][0]) > 96:
            d[j[0]] += 1
    
    dd = [d[j] > 1 for j in d]
    for n in g[t[0]]:
        if n != "end" and ord(n[0]) > 96 and list(zip(*path))[0].count(n) < 1:
            s.append([n, t[1] + 1])
# part 2
#        if n != "end" and ord(n[0]) > 96 and (dd.count(True) < 1 or d[n] < 1): 
#            s.append([n, t[1] + 1])
        if n == "end":
            s.append([n, t[1] + 1])
        if n != "end" and ord(n[0]) < 97:
            s.append([n, t[1] + 1])

print(c)
