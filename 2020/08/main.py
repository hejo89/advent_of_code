arr = [[j.strip().split()[0], int(j.strip().split()[1])] for j in open ("input.txt", "r")]

idx, a, s = 0, 0, set()
while True:
    c, v = arr[idx]
    tmp = len(s)
    s.add(idx)
    if len(s) - tmp == 0: break
    if    c == "jmp": idx += v
    elif  c == "acc":   a += v; idx += 1
    else: idx += 1

print(a)

def f():
    idx, a, s = 0, 0, set()
    while idx != len(arr) - 1:
        c, v = arr[idx]
        tmp = len(s)
        s.add(idx)
        if len(s) - tmp == 0: return False, 0
        if    c == "jmp": idx += v
        elif  c == "acc":   a += v; idx += 1
        else: idx += 1
        if idx == len(arr)-1: return True, a

for i, j in enumerate(arr):
    if  j[0] == "jmp":
        arr[i][0] = "nop"
        r, v = f()
        if r: print(v); break
        arr[i][0] = "jmp"
    elif j[0] == "nop":
        arr[i][0] = "jmp"
        r, v = f()
        if r: print(v); break
        arr[i][0] = "nop"


        
