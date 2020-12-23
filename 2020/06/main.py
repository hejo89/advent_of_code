import string
s1 = set()
s2 = set(string.ascii_lowercase)
c1 = c2 = 0
with open("input.txt", "r") as f:
    for l in f:
        if l == "\n":
            c1 += len(s1)
            c2 += len(s2)
            s1 = set()
            s2 = set(string.ascii_lowercase)
        else:
            s1 = s1.union(l.strip())
            s2 = s2.intersection(l.strip())

print(c1, c2)
