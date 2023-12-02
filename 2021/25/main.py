a = [list(j) for j in open("input").read().split()]

def foo():
    v1= set()
    v2= set()
    c = 0
    for i in range(len(a)):
        for j in range(len(a[0])):
            
            if a[i][j] == ">" and a[i][(j + 1) % len(a[0])] == "." and (i, j) not in v1 and (i, (j + 1) % len(a[0])) not in v1:
                a[i][j], a[i][(j + 1) % len(a[0])] = a[i][(j + 1) % len(a[0])], a[i][j]  
                v1.add((i, (j + 1) % len(a[0])))
                v1.add((i, j))
                c += 1

    for i in range(len(a)):
        for j in range(len(a[0])):

            if a[i][j] == "v" and a[(i + 1) % len(a)][j] == "." and (i, j) not in v2 and ((i + 1) % len(a), j) not in v2:
                a[i][j], a[(i + 1) % len(a)][j] = a[(i + 1) % len(a)][j], a[i][j]
                v2.add(((i + 1) % len(a), j))
                v2.add((i, j))
                c += 1

    if c: return True

idx = 0
while foo():
    idx += 1
print(idx + 1)
