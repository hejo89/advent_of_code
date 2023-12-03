import re
import collections
n = {}
s = {}
g = collections.defaultdict(list)
part_1 = 0
part_2 = 0
for x, l in enumerate(open('input.txt')):
    for t in re.finditer(r'\d+', l.strip()):
        n[(x, t.start())] = t.group()
    for y, symbl in enumerate(l.strip()):
        if not symbl.isdigit() and symbl != '.':
            s[(x, y)] = symbl


valid_numbers = set()
for a, b in n:
    for d in range(len(n[(a, b)])):
        for x in range(-1, 2):
            for y in range(-1, 2):
                if (a + x, b + y + int(d)) in s and (a, b) not in valid_numbers:
                    part_1 += int(n[(a, b)])
                    valid_numbers.add((a, b))
                    g[(a + x, b + y + int(d))].append(int(n[(a, b)]))


for j in g:
    if s[j] == '*' and len(g[j]) == 2:
        part_2 += g[j][0] * g[j][1]

print(part_1)
print(part_2)
