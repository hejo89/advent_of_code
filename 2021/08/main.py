import itertools

a = open("input").read().strip().split()
b = []
i = 0
c = 0   
while i <len(a):
    b.append([a[i:i+10], a[i+11:i+15]])
    i += 15
for i in b:
    for j in i[1]:
        if len(j) in [2,3,4,7]:
            c += 1
print(c)


n = {0:frozenset([0,1,2,4,5,6]), 1:frozenset([2,5]), 2:frozenset([0,2,3,4,6]), 3:frozenset([0,2,3,5,6]), 4:frozenset([1,2,3,5]), 5:frozenset([0,1,3,5,6]), 6:frozenset([0,1,3,4,5,6]), 7:frozenset([0,2,5]), 8:frozenset([0,1,2,3,4,5,6]), 9:frozenset([0,1,2,3,5,6])}

m = {n[i]:str(i) for i in n}

def foo(inpt):

    for j in itertools.permutations("abcdefg"):
        r = {y:x for x, y in enumerate(j)}
        s = set()
        for digit in inpt:
            d = []
            for letter in digit:
                d.append(r[letter])
            s.add(frozenset(d))   
        if s == set(n.values()): return r


final = 0
for i in b:
    c = ""
    decoded = foo(i[0])
    for j in i[1]:
        s = set()
        for k in j:
            s.add(decoded[k])
        c += m[frozenset(s)]

    final += int(c)

print(final)
