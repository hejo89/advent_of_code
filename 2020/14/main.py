import itertools
arr = []
mem = {}
with open("input.txt", "r") as f:
    for l in f:
        tmp = l.strip().split("=")
        if tmp[0].strip() == "mask":
            arr.append([tmp[1].strip()])
        else: 
            arr[-1].append((int(tmp[0].strip()[4:-1]), int(tmp[1].strip())))
    
def bm(m, n):
    n = list("0" * (36 - len(bin(n)) + 2) + bin(n)[2:])
    for i, j in enumerate(m):
        if j != "X": n[i] = j
    return int("".join(n), 2)


for i in arr:
    for j in i[1:]:
        mem[j[0]] = bm(i[0], j[1])

        
        
print(sum(mem.values()))

mem = {}

def bm(m, n):
    adresses = []
    n = list("0" * (36 - len(bin(n)) + 2) + bin(n)[2:])
    for i, j in enumerate(m):
        if j == "1": n[i] = j
        if j == "X": n[i] = "X"
    return n


def f(m, n):
    a = []
    n = bm(m, n)
    for j in itertools.product([0, 1], repeat = n.count("X")):
        tmp = list(n)
        j = list(j)
        for x, y in enumerate(tmp):
            if y == "X": tmp[x] = str(j.pop())

        a.append(int("".join(tmp), 2))

    return a


for i in arr:
    for j in i[1:]:
        for k in f(i[0], j[0]):
            mem[k] = j[1]

        
        
print(sum(mem.values()))
            

