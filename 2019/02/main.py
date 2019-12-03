with open ("input.txt", "r") as f:
    arr = map(int, f.readline().strip().split(","))
arr_copy = [j for j in arr]
arr[1] = 12
arr[2] = 2
def foo(arr, idx):
    if arr[idx] == 99: return
    if arr[idx] == 1: arr[arr[idx + 3]] = arr[arr[idx + 1]] + arr[arr[idx + 2]]
    elif arr[idx] == 2: arr[arr[idx + 3]] = arr[arr[idx + 1]] * arr[arr[idx + 2]]
    foo(arr, idx + 4)


foo(arr, 0)

print arr[0]
arr = arr_copy[::]

for i in range(100):
    for j in range(100):
        arr[1], arr[2] = i, j
        foo(arr, 0)

        if arr[0] == 19690720: print 100 * i + j
        arr = arr_copy[::]
