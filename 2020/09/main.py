arr = [int(l.strip()) for l in open("input.txt", "r")]
preamble = arr[:25]


def f(a):
    s = set()
    for i, j in enumerate(a):
        for k in a[i + 1:]: 
            s.add(j + k)

    return s

idx = 25
while arr[idx] in f(arr[idx - 25:idx]):
    idx += 1

N = arr[idx]
print(N)
def foo():
    r = 2
    s = 0
    while True:
        for i in range(len(arr) - r + 1):
            s = sum(arr[i:i + r])
            if s == N: arr[i:i + r].sort(); return min(arr[i:i + r]) + max(arr[i:i + r])

        r += 1

print(foo())
