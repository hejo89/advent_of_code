#d = {}
#messages = []
#with open("input.txt", "r") as f:
#    for l in f:
#        if l[0].isdigit():
#            tmp = l.strip().split(":")
#            for i, j in enumerate(tmp[1].split("|")):
#                for m, n in enumerate(j.lstrip()):
#                    if n.isdigit():
#                        print(tmp[1], n, tmp[1][i][m])
#                        tmp[1][i][m] = int(n)
#            d[tmp[0]] = tmp[1].lstrip().split("|")
#        else:
#            messages.append(l.strip())
#messages = messages[1:]
#for j in d:
#    d[j] = [k.lstrip().strip().replace('"', "").split(" ") for k in d[j]]




d = {}
messages = []
with open("input.txt", "r") as f:
    for l in f:
        if l[0].isdigit():
            tmp = l.strip().split(":")
            d[tmp[0]] = tmp[1].lstrip().split("|")
        else:
            messages.append(l.strip())
messages = messages[1:]
for j in d:
    d[j] = [k.lstrip().strip().replace('"', "").split(" ") for k in d[j]]

def f(v):
    global s
    if d[v][0][0] in "ab": return d[v][0][0]
    for j in d[v]:
        for k in j: s += f(k) 

    return s

s = ""
for i in d["0"][0]:
    s += f(i)

print(s)


lines = open("input.txt").readlines()
d = {}
while 1:
    l = lines.pop(0).strip()
    if not l: break
    k, v = l.split(": ")
    d[k] = [w.split() for w in v.split("|")]

print(d)
