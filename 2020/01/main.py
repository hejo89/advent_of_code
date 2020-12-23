arr = []
with open("input.txt", "r") as f:
    for l in f:
        arr.append(int(l))


def foo():
    for i, j in enumerate(arr):
        for k, l in enumerate(arr):
            for m, n in enumerate(arr):
                if (i != k != m) and j + l + n == 2020: return j*l*n

print foo()
