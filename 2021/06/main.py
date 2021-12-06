a = [map(int, j.strip().split(",")) for j in open("input.txt")][0]

d = {j:0 for j in range(9)}

for j in a:
    d[j] += 1

c = len(a)

for _ in range(256):

    t = d[0]
    d[0] -= t

    for j in d:
        if j != 0:
            d[j - 1] += d[j]
            d[j]     -= d[j]

    if t:
        c += t
        d[6] += t
        d[8] += t

print(c)
