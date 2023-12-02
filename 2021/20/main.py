s = ""
b = []
a = open("input").read().split("\n")[:-1]
for i, j in enumerate(a):
    if j != "": s += j
    else: break
for j in a[i+1:]:
    b.append(list(j))

def extend():
    global b
    x, y = [0, float("inf")], [0, float("inf")]
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] == "#":
                x[1] = min(i, x[1])
                x[1] = max(i, x[1])
                y[1] = min(i, y[1])
                y[1] = max(i, y[1])     
      
    for j in range(len(b)):
        b[j] = ["."] * (max(1, y[0])) + b[j] + ["."] * max(1, len(b) - y[1] - 1)
    for j in range(max(1, len(b) - x[1]  - 1)):
        b = b + [["."] * len(b[0])]  
    for j in range(max(1, x[0])):
        b = [["."] * len(b[0])] + b


def enhance():
    extend()
    bb = [j[::] for j in b]
    for i in range(1, len(b) - 1):
        for j in range(1, len(b[0]) - 1):
            tmp = ""
            for idx in range(-1, 2):
                tmp += "".join(b[i + idx][j-1:j+2])
            n = ""
            for l in tmp:
                if l == "#": n += "1"
                else       : n += "0"
            bb[i][j] = s[int(n, 2)]

    return bb
#extend()
#for j in b:
#    print("".join(j))
b = enhance()
c = 0
for i in enhance():
    for j in i:
        if j == "#": c += 1


print(c)
