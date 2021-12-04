import collections

a = [tuple(map(int, j.strip().split(","))) for j in open("input.txt")]
#a = [tuple(map(int, j.strip().split(","))) for j in open("input_test.txt")]

b_min_c, b_max_c, b_min_r, b_max_r = min(list(zip(*a))[0]), max(list(zip(*a))[0]), min(list(zip(*a))[1]), max(list(zip(*a))[1])

d = collections.defaultdict(list)
a = sorted(a, key = lambda x:x[0] + x[1])
grid_size = 500

for i in range(0, grid_size + 1):
    for j in range(0, grid_size + 1):
        m = (10e9, 10e9)
        c = 0
        for z in a:
            t = abs(z[0] - i), abs(z[1] - j)
            mm = abs(m[0] - i), abs(m[1] - j)
            if sum(t) < sum(mm): m = z
        for z in a:
            t = abs(z[0] - i), abs(z[1] - j)
            mm = abs(m[0] - i), abs(m[1] - j)
            if sum(t) == sum(mm): c += 1



        if c == 1: d[m].append((i, j))


test = [[(j, 0), (0, j), (j, grid_size), (grid_size, j)] for j in range(grid_size + 1)]
test = set([i for j in test for i in j])
inf = set()
for i in d:
    for j in d[i]:
        if j in test: inf.add(i); break   

d = {i:len(d[i]) for i in d if i not in inf}
d = sorted(d.items(), key=lambda x:x[1]) 
print(d)

def mnhttn_dstnc(x, y, w, z):
    return abs(x - w) + abs(y - z)
r = set()

for i in range(0, grid_size + 1):
    for j in range(0, grid_size + 1):
        c = 0
        for k in a:
            w, z = k
            c += mnhttn_dstnc(i, j, w, z)


        if c < 10000: r.add((i, j))
            
print(len(r))        
