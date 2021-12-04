import collections
d = collections.defaultdict(int)
a = [list(map(int, l.strip().split()[2:][0].split()[0][:-1].split(","))) + list(map(int, l.strip().split()[2:][1].split("x"))) for l in open("input.txt")]
a = [[(j[0], j[0] + j[2]), (j[1], j[1] + j[3])] for j in a]



for i in a:
    for j in range(i[0][0], i[0][1]):
        for k in range(i[1][0], i[1][1]):
            d[(j, k)] += 1

print(sum(1 for j in d.values() if j != 1))


