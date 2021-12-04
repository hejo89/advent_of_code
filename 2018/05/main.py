p = [j.strip() for j in open("input.txt")][0]

def foo(p):
    s = []
    for j in p:
        if s and abs(ord(s[-1]) - ord(j)) == 32: s.pop()
        else: s.append(j)

    return len(s)


print(foo(p))

m = 50001
for j in range(26):
    t = [x for x in p if x != chr(65 + j) and x != chr(97 + j)]
    m = min(m, foo(t))


print(m)
