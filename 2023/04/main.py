import math
import re
import collections
part_2 = collections.defaultdict(int)
w = []
s = set()
r = 0
for idx, l in enumerate(open('input.txt'), 1):
    part_2[idx] += 1
    a, b = l.strip().split('|')
    w = re.findall(r'(\d+)', a)
    s = re.findall(r'(\d+)', b)
    p = 1
    for i, c in enumerate(w[1:], 1):
        if c in s:
            p *= 2
    for c in range(idx, idx + min(int(math.log(p, 2)), 198 - idx)):
        for n in range(part_2[idx]):
            part_2[c + 1] += 1
    r += p//2

print(r)
print(sum(part_2.values()))
