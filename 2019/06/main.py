from collections import defaultdict
arr = []
with open("input.txt", "r") as f:
    for l in f: arr.append(l.strip())

#arr = ["COM)B", "B)C", "C)D", "D)E", "E)F", "B)G", "G)H", "D)I", "E)J", "J)K", "K)L"]
#arr = ["COM)B", "B)C", "C)D", "D)E", "E)F", "B)G", "G)H", "D)I", "E)J", "J)K", "K)L", "K)YOU", "I)SAN"]
d = defaultdict(list)
for j in arr:
    a, b =  j.split(")")
    d[a].append(b) 

total = 0
def traverse(key, d, c):
    global total
    total += c
    c += 1
    
    for j in d[key]: traverse(j, d, c)


traverse("COM", d, 0)
print total

d2 = defaultdict(list)
for j in d:
    for i in d[j]: d2[i].append(j)


def traverse_backwards(key, t):
    if d2[key]: t.append(d2[key][0])  
    for j in d2[key]: traverse_backwards(j, t)
    return t

a =  traverse_backwards("YOU", [])
b =  traverse_backwards("SAN", [])
while a[-1] == b[-1]:
    a.pop()
    b.pop()
print len(a) + len(b)
