i = []
with open("input", "r") as f:
    for l in f:
        i.append(l.strip().split())


types = [(0, 0)] * 14
idx = 0
for x, y in enumerate(i):
    if x % 18 == 5: 
        if y[2][0] == "-":
            types[idx] = (1, int(y[2]))
        idx += 1


def c(l):
    if l == "w": return 0
    if l == "x": return 1
    if l == "y": return 2
    if l == "z": return 3



def op(o):
    global r
    global m
    global idxx   
    if o[0] == "inp":
        if types[idxx][0] == 0: a[0] = int(m.pop())
        if types[idxx][0] == 1: a[0] = a[-1] % 26 + types[idxx][1]
        idxx += 1
        if a[0] > 9 or a[0] < 1: return False
        r += str(a[0])
    if o[0] == "add":
        if o[2].lstrip("-").isdigit(): a[c(o[1])]  += int(o[2])
        else                         : a[c(o[1])]  += a[c(o[2])]
    if o[0] == "mul":
        if o[2].lstrip("-").isdigit(): a[c(o[1])]  *= int(o[2])
        else                         : a[c(o[1])]  *= a[c(o[2])]
    if o[0] == "div":
        if o[2].lstrip("-").isdigit(): a[c(o[1])] //= int(o[2])
        else                         : a[c(o[1])] //= a[c(o[2])]
    if o[0] == "mod":
        if o[2].lstrip("-").isdigit(): a[c(o[1])]  %= int(o[2])
        else                         : a[c(o[1])]  %= a[c(o[2])]
    if o[0] == "eql":
        if o[2] == "0": a[1]  = int(a[1] == 0)
        else          : a[1]  = int(a[1] == a[0])
    return True



start = 9999999
invalid = True
while invalid:
    idxx = 0
    invalid = False
    r = ""
    m = list(str(start))
    if "0" in m:
        invalid = True
        start -= 1
        continue
    
    a = [0]*4
    for j in i:
        if not op(j):
            invalid = True   
            break
    start -= 1
print(r)

start = 1111111
invalid = True
while invalid:
    idxx = 0
    invalid = False
    r = ""
    m = list(str(start))
    if "0" in m:
        invalid = True
        start += 1
        continue
    
    a = [0]*4
    for j in i:
        if not op(j):
            invalid = True   
            break
    start += 1
print(r)
