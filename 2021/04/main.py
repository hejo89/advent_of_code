arr = []

with open("input.txt", "r") as f:
    n = map(int, f.readline().strip().split(","))
    for i, j in enumerate(f):
        if not i % 6: arr.append([])
        else: arr[-1].append(map(int, j.strip().split()))


r = [[set() for j in range(len(arr[0]))] for i in range(len(arr))]
c = [[set() for j in range(len(arr[0]))] for i in range(len(arr))]


def foo():
    for l in n:
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                for k in range(len(arr[0][0])):

                    if l == arr[i][j][k]: r[i][j].add(l)
                    if l == arr[i][j][k]: c[i][k].add(l)

        for i, j in enumerate(r):
            for k in j:
                if len(k) == 5: return l * (sum(x for y in arr[i] for x in y) - sum(x for y in r[i] for x in y))
        

        for i, j in enumerate(c):
            for k in j:
                if len(k) == 5: return l * (sum(x for y in arr[i] for x in y) - sum(x for y in r[i] for x in y))

print(foo())

def foo():
    s = set()
    for l in n:
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                for k in range(len(arr[0][0])):

                    if l == arr[i][j][k]: r[i][j].add(l)
                    if l == arr[i][j][k]: c[i][k].add(l)

        for i, j in enumerate(r):
            for k in j:
                if len(k) == 5:
                    s.add(i)
                    if len(s) == len(arr):
                        return l * (sum(x for y in arr[i] for x in y) - sum(x for y in r[i] for x in y))
        

        for i, j in enumerate(c):
            for k in j:
                if len(k) == 5:
                    s.add(i)
                    if len(s) == len(arr):
                        return l * (sum(x for y in arr[i] for x in y) - sum(x for y in r[i] for x in y))
                        return l * (sum(x for y in arr[i] for x in y) - sum(x for y in r[i] for x in y))

print(foo())
