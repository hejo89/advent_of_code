#from collections import defaultdict
#d = defaultdict(list)
#dd = defaultdict(list)
#with open("input2.txt", "r") as f:
#    for l in f:
#        tmp = l.strip().split("contain")
#        key = " ".join(tmp[0].split(" ")[:2])
#        tmp = [{" ".join(j.split(" ")[2:-1]): j.split(" ")[1]} for j in tmp[1].split(",")]
#        if tmp != [{'other': 'no'}]: d[key] = tmp
#        else: d[key] = [{'exit': '1'}]

#for i in d:
#    for j in d[i]:
#        dd[list(j.keys())[0]].append(i)

#s = set()
#def foo(j):
#    for i in dd[j]:
#        s.add(i)
#        foo(i)
#foo("shiny gold")

#print(len(s))
#print(d)
#def foo(k): return 1 + sum(int(list(i.values())[0]) * foo(j) for i, j in d[k])

#print(foo("shiny gold"))
#print(c)


import collections
d = collections.defaultdict(list)
e = collections.defaultdict(list)
for l in open("input.txt"):
    k, v = l.split(" contain ")
    k, _ = k.rsplit(" ", 1)
    for v in v.split(", "):
        v = v.split()
        t = " ".join(v[1:3])
        d[t].append(k)
        if v[0].isdigit(): e[k].append((int(v[0]), t))

q = ["shiny gold"]
v = set()
while q:
    k = q.pop()
    v.add(k)
    for x in d[k]:
        if not x in v: q.append(x)
print(len(v) - 1)

def f(k): return 1 + sum(n * f(v) for n, v in e[k])
print(f("shiny gold") - 1)
