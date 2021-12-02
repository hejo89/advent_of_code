arr = []
with open("input.txt", "r") as f:
    for j in f: arr.append(int(j.strip()))

c = 0
for i, j in enumerate(arr[1:]):
    if j > arr[i]: c += 1

print(c)

c = 0
for i in range(len(arr)):
    if sum(arr[i+1:i+4]) > sum(arr[i:i+3]): c += 1  

print(c)
