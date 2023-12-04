import math
import re
import collections
r = 0
q = collections.defaultdict(int)
for idx, l in enumerate(open('input.txt'), 1):
    q[idx] += 1
    a, b = l.strip().split('|')
    w = re.findall(r'(\d+)', a)
    s = re.findall(r'(\d+)', b)
    p = 1
    for i, c in enumerate(w[1:], 1):
        if c in s:
            p *= 2
    for c in range(idx, idx + min(int(math.log(p, 2)), 198 - idx)):
        for n in range(q[idx]):
            q[c + 1] += 1
    r += p//2

print(r)
print(sum(q.values()))
