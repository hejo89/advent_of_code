s = ""
b = []
a = open("input").read().split("\n")[:-1]
for i, j in enumerate(a):
    if j != "": s += j
    else: break
for j in a[i+1:]:
    b.append(list(j))
a = "".join(a)

def foo(arr, x, y):
    return arr[x-1][y-1:y+2] + arr[x][y-1:y+2] + arr[x+1][y-1:y+2]

tmp = [["."] * (len(b[0]) + 4), ["."] * (len(b[0]) + 4)]
for j in b:
    tmp += [[".", "."] + j + [".", "."]]
tmp += [["."] * (len(b[0]) + 4), ["."] * (len(b[0]) + 4)]

tmp2 = [["."] * (len(b[0]) + 4), ["."] * (len(b[0]) + 4)]
for j in b:
    tmp2 += [[".", "."] + j + [".", "."]]
tmp2 += [["."] * (len(b[0]) + 4), ["."] * (len(b[0]) + 4)]


for x in range(1, len(tmp) - 1):
    for y in range(1, len(tmp[0]) - 1):
        t = "".join(foo(tmp, x, y))
        t = t.replace(".", "0")
        t = t.replace("#", "1")
        t = int(t, 2)
        tmp2[x][y] = s[t]

for x in range(len(tmp)):
    for y in range(len(tmp[0])):
        if x == 0 or y == 0 or x == len(tmp) - 1 or y == len(tmp[0]) - 1:
            tmp2[x][y] = "#"

tmp3 = [["#"] * (len(tmp2[0]) + 2)]
for j in tmp2:
    tmp3 += [["#"] + j + ["#"]]
tmp3 += [["#"] * (len(tmp2[0]) + 2)]

#for j in tmp3:
#    print(j)

for x in range(1, len(tmp) - 1):
    for y in range(1, len(tmp[0]) - 1):
        t = "".join(foo(tmp, x, y))
        t = t.replace(".", "0")
        t = t.replace("#", "1")
        t = int(t, 2)
        tmp2[x][y] = s[t]

tmp4 = [j[1:-1] for j in tmp3[1:-1]]

for x in range(1, len(tmp3) - 1):
    for y in range(1, len(tmp3[0]) - 1):
        t = "".join(foo(tmp3, x, y))
        t = t.replace(".", "0")
        t = t.replace("#", "1")
        t = int(t, 2)
        tmp4[x - 1][y - 1] = s[t]

c = 0
for j in tmp4:
    c += j.count("#")

print(c)
