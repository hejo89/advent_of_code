import collections
r = 0
with open("input.txt", "r") as f:
    for j in f:
        r += int(j)

print(r)

arr = []
with open("input.txt", "r") as f:
    for j in f:
        arr.append(int(j))

c = 0
i = 0
initial = collections.defaultdict(int)
while True:
    if initial[c] > 1: 
        print(c)
        break
    c += arr[i]
    initial[c] += 1
    i += 1
    i %= len(arr)
