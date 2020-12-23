import collections
arr = [0] + sorted([int(j.strip()) for j in open("input.txt", "r")])
arr += [arr[-1] + 3]
d = collections.defaultdict(int)
for i, j in enumerate(arr[1:]): d[j - arr[i]] += 1
print(d[1] * d[3])
cache = {}
def f(idx):
    if idx in cache: return cache[idx]
    if idx == len(arr) - 1: return 1
    tmp = [idx + i for i in range(1, 4) if idx + i < len(arr) and arr[idx + i] <= arr[idx] + 3]
    t =  sum(f(x) for x in tmp)
    cache[idx] = t
    return t

print f(0)
