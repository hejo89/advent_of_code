arr = [list(j.strip()) for j in open("input.txt")]
s = set()
for i, x in enumerate(arr):
    for j, y in enumerate(x):
        if y == "#":
            s.add((i, j, 0, 0))
def foo(s):
    ss = set()
    for j in s:
        x, y, z, w = j

        for a in range(-1, 2):
            for b in range(-1, 2):
                for c in range(-1, 2):
                    for d in range(-1, 2):
                        t = (x+a, y+b, z+c, w+d)
                        ss.add(t)

    return ss

def f(t):
    cc = 0
    x, y, z, w = t
    for a in range(-1, 2):
        for b in range(-1, 2):
            for c in range(-1, 2):
                for d in range(-1, 2):
                    t = (x+a, y+b, z+c, w+d)

                    if t in s: cc += 1

    return cc

ccc = 0

while ccc < 6:
    sss = s.copy()
    for j in foo(s):
        tmp = f(j)
        if j in s and (tmp != 3 and tmp != 4): sss.remove(j)
        if j not in s and tmp == 3: sss.add(j)

    s = sss.copy()
    ccc += 1
print(len(sss))
