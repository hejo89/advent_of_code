import collections

a = [i[1].split("..") for i in [j.split("=") for j in open("input").read().strip().split(" ")[2:]]]
a = [[int(i.strip(",")) for i in j] for j in a]
xl, xr = a[0]
yd, yu = a[1]
n = abs(a[1][0]) - 1
print((n+1)*(n) / 2)

x = collections.defaultdict(list)
for n in range(xr, -1, -1):
    for m in range(n - 1, -1, -1):
        t = (n+1)*n/2 - (m+1)*m/2
        if t <= xr and t >= xl:
            if m == 0: x[n].append(float("inf"))
            else: x[n].append(n-m)
    if n in x:
        if len(x[n]) == 1: x[n] = [x[n][0]] + [x[n][ 0]] 
        else             : x[n] = [x[n][0]] + [x[n][-1]] 

y = collections.defaultdict(list)
for n in range(abs(yd) + 1):
    d = 0
    for c, m in enumerate(range(n, abs(yd) + 1), 1):
        d += m
        if d <= abs(yd) and d >= abs(yu):
   
         y[n].append(c)

z = collections.defaultdict(list)
for j in y:
    if j > 1:

        if len(y[j]) == 1:
            z[j] = [y[j] + y[j]]
            z[j-1].append([y[j][0] + 2*(j-1) + 1] + [y[j][-1] + 2*(j-1) + 1])
        else:
            z[j] = [[y[j][0]] + [y[j][-1]]]
            z[j-1].append([y[j][0] + 2*(j-1) + 1] + [y[j][-1] + 2*(j-1) + 1])

    else:

        if len(y[j]) == 1:
            z[j] = [y[j] + y[j]]
        else:
            z[j] = [[y[j][0]] + [y[j][-1]]]

c = 0
for i in x:
    for j in z:
        for k in z[j]:
            u, v = max(x[i][0], k[0]), min(x[i][1], k[1])
            if u <= v:
                c += 1
print(c)
