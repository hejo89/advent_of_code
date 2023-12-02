a = open("input").read().strip().split()
b = []
for i in range(len(a)):
    if not i % 2:
        b.append([a[i]])
        b[-1].append([map(int, j[2:].split("..")) for j in a[i + 1].split(",")])        
s = set()
for i in b:
    for x in range(max(-50, i[1][0][0]), min(50 ,i[1][0][1]) + 1):
        for y in range(max(-50, i[1][1][0]), min(50 ,i[1][1][1]) + 1):   
            for z in range(max(-50 ,i[1][2][0]), min(50, i[1][2][1]) + 1):
                if i[0] == "on":                     s.add((x, y, z))
                if i[0] == "off" and (x, y, z) in s: s.remove((x, y, z))

print(len(s))

