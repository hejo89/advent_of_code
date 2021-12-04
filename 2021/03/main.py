arr = [j.strip() for j in open("input.txt")]
a = zip(*arr)
g = ""
e = ""

for j in a:
    tmp = "".join(j).count("0")
    if tmp < len(arr)/2: g += "1"; e += "0"
    else               : g += "0"; e += "1"

print(int(g, 2) * int(e, 2))

Co2 = arr[::]
oxy = arr[::]
idx = 0
while len(Co2) > 1 or len(oxy) > 1:
    c1 = zip(*Co2)[idx].count("1")
    c2 = zip(*oxy)[idx].count("1")
    l1 = len(Co2)
    l2 = len(oxy)
    x, y = [], []
    if len(Co2) > 1:
        for i, j in enumerate(Co2):
            if not int(j[idx]) and l1 <= 2*c1: x.append(i)
            if     int(j[idx]) and l1 >  2*c1: x.append(i)
    if len(oxy) > 1:
        for i, j in enumerate(oxy):
            if not int(j[idx]) and l2 >  2*c2: y.append(i)
            if     int(j[idx]) and l2 <= 2*c2: y.append(i)

    Co2 = [j for i, j in enumerate(Co2) if i not in x]
    oxy = [j for i, j in enumerate(oxy) if i not in y]

    idx += 1

print(int(Co2[0], 2) * int(oxy[0], 2))
