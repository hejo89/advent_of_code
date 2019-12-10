with open ("input.txt", "r") as f:
    arr = map(int, f.readline().strip().split(","))

parameter_length = {1:3, 2:3, 3:1, 4:1, 5:2, 6:2, 7:3, 8:3, 99:0}

def intcode(arr, ID):
    idx = 0
    while 1:

        op = arr[idx] % 100
        p_mode = arr[idx] / 100
        idx += 1
        p = []
        for _ in range(parameter_length[op]):
            p.append(idx if p_mode % 10 else arr[idx])
            idx += 1
            p_mode /= 10

        if   op == 1: arr[p[2]] = arr[p[0]] + arr[p[1]]
        elif op == 2: arr[p[2]] = arr[p[0]] * arr[p[1]]
        elif op == 3: arr[p[0]] = ID
        elif op == 4: output = arr[p[0]]
        elif op == 5 and arr[p[0]] != 0: idx = arr[p[1]]
        elif op == 6 and arr[p[0]] == 0: idx = arr[p[1]]
        elif op == 7: arr[p[2]] = arr[p[0]] < arr[p[1]]
        elif op == 8: arr[p[2]] = arr[p[0]] == arr[p[1]]
        elif op == 99: return output

print intcode(arr, 1)

with open ("input.txt", "r") as f:
    arr = map(int, f.readline().strip().split(","))

print intcode(arr, 5)
