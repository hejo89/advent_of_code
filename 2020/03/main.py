s = "" 
with open("input.txt", "r") as f:
    for l in f: s += l.strip()
m=1
for k in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    c = 0
    for j in range(len(s) / 31 / k[1]):
        if s[j * k[1]*31 + (j*k[0])%31] == "#": c += 1

    print c
    m*=c

print m
