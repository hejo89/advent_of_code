import collections
arr = [list(j.strip()) for j in open("input.txt")]

def v(i, j):
    return i >= 0 and i < len(arr) and j >= 0 and j < len(arr[0])



def f(i, j):
    d = collections.defaultdict(int)
    if v(i + 1, j - 1): d[arr[i + 1][j - 1]] += 1
    if v(i + 1, j + 0): d[arr[i + 1][j + 0]] += 1
    if v(i + 1, j + 1): d[arr[i + 1][j + 1]] += 1
    if v(i + 0, j - 1): d[arr[i + 0][j - 1]] += 1
    if v(i + 0, j + 1): d[arr[i + 0][j + 1]] += 1
    if v(i - 1, j - 1): d[arr[i - 1][j - 1]] += 1
    if v(i - 1, j + 0): d[arr[i - 1][j + 0]] += 1
    if v(i - 1, j + 1): d[arr[i - 1][j + 1]] += 1

    return d


def ff(i, j):
    d = collections.defaultdict(int)

    a, b = i, j
    while v(a + 1, b - 1) and arr[a + 1][b - 1] == ".":
        a += 1
        b -= 1
    if v(a + 1, b - 1): d[arr[a + 1][b - 1]] += 1

    a, b = i, j
    while v(a + 1, b) and arr[a + 1][b] == ".":
        a += 1
    if v(a + 1, b): d[arr[a + 1][b]] += 1

    a, b = i, j
    while v(a + 1, b + 1) and arr[a + 1][b + 1] == ".":
        a += 1
        b += 1
    if v(a + 1, b + 1): d[arr[a + 1][b + 1]] += 1

    a, b = i, j
    while v(a, b - 1) and arr[a][b - 1] == ".":
        b -= 1
    if v(a, b - 1): d[arr[a][b - 1]] += 1

    a, b = i, j
    while v(a, b + 1) and arr[a][b + 1] == ".":
        b += 1
    if v(a, b + 1): d[arr[a][b + 1]] += 1

    a, b = i, j
    while v(a - 1, b - 1) and arr[a - 1][b - 1] == ".":
        a -= 1
        b -= 1
    if v(a - 1, b - 1): d[arr[a - 1][b - 1]] += 1

    a, b = i, j
    while v(a - 1, b) and arr[a - 1][b] == ".":
        a -= 1

    if v(a - 1, b): d[arr[a - 1][b]] += 1

    a, b = i, j
    while v(a - 1, b + 1) and arr[a - 1][b + 1] == ".":
        a -= 1
        b += 1
    if v(a - 1, b + 1): d[arr[a - 1][b + 1]] += 1


    return d

def foo(array):
    a = [list(r) for r in array]
    for i, k in enumerate(arr):
        for j, l in enumerate(k):
            tmp = ff(i, j)
            if arr[i][j] == "L" and tmp["#"] == 0: a[i][j] = "#"
            if arr[i][j] == "#" and tmp["#"] >= 5: a[i][j] = "L"

    return a

tmp = foo(arr)

while tmp != arr:
    arr = tmp
    tmp = foo(arr)
    
c = 0
for j in arr:
    for i in j:
        if i == "#": c += 1

print(c)
