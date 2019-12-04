from collections import defaultdict
d = defaultdict(int)
c1, c2 = 0, 0
for j in range(136760, 595730):
    d = defaultdict(int)
    s = str(j)
    for k in s: d[k] += 1
    a = []
    adjacent = False
    increasing = True
    exactly_one_adjacent_pair = False
    for idx, k in enumerate(s[1:]):
         if s[idx] == k:
            adjacent = True
            a.append(k)

    for idx, k in enumerate(s[1:]):
         if s[idx] > k:
            increasing = False
            break
    for k in a:
        if d[k] == 2:
            exactly_one_adjacent_pair = True
            break

    if adjacent == True and increasing == True: c1 += 1
    if adjacent == True and increasing == True and exactly_one_adjacent_pair == True: c2 += 1

print c1
print c2
 

