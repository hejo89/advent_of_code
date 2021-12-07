p = map(int, open("input").read().strip().split(","))
d = {j:[0, 0] for j in range(max(p) + 1)}
for i in d:
    for j in p:
        r = abs(j-i)
        d[i][0] += r
        d[i][1] += r*(r+1)/2


print(min(zip(*d.values())[0]))
print(min(zip(*d.values())[1]))
