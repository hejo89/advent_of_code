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


#foo(arr, 0)

#print arr


for i in range(100):
    for j in range(100):
        print arr
        print
        arr[1], arr[2] = i, j
        foo(arr, 0)
        arr = arr_copy
        print arr
        print
        print
        print arr_copy      
        print
#        if arr[0] == 19690720: print i, j, 100 * i + j

