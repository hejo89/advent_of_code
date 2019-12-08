with open ("input.txt", "r") as f:
    arr = map(int, f.readline().strip().split(","))

parameter_length = {1:4, 2:4, 3:2, 4:2, 5:3, 6:3, 7:4, 8:4}

def parameter_state(p, l):
    arr = []
    for _ in range(l):
        arr.append(p % 10)
        p /= 10
    return arr

def foo(arr, pos_imm, idx):
    if not pos_imm:
        return arr[arr[idx]]
    return arr[idx]

def intcode(ID):
    idx = 0
    while 1:
        pointer_already_set = False
        operation = arr[idx] % 100

        if arr[idx] % 100 == 1:
            indices = [0] * 3
            a, b, c = parameter_state(arr[idx] / 100, 3)
            if c:
                arr[idx + 3] = foo(arr, a, idx + 1) + foo(arr, b, idx + 2)
            else:
                arr[arr[idx + 3]] = foo(arr, a, idx + 1) + foo(arr, b, idx + 2)

        elif arr[idx] % 100 == 2:

            a, b, c = parameter_state(arr[idx] / 100, 3)
            if c:
                arr[idx + 3] = foo(arr, a, idx + 1) + foo(arr, b, idx + 2)
            else:
                arr[arr[idx + 3]] = foo(arr, a, idx + 1) * foo(arr, b, idx + 2)

        elif arr[idx] % 100 == 3:
            a = arr[idx] / 100 
            if a: arr[idx + 1] = ID
            else: arr[arr[idx + 1]] = ID 
        
        elif arr[idx] % 100 == 4:
            a = arr[idx] / 100
            if a: print arr[idx + 1]
            else: print arr[arr[idx + 1]]
        
        elif arr[idx] % 100 == 5:
            a, b = parameter_state(arr[idx] / 100, 2)
            if foo(arr, a, idx + 1) != 0:
                idx  = foo(arr, b, idx + 2)
                pointer_already_set = True

        elif arr[idx] % 100 == 6:
            a, b = parameter_state(arr[idx] / 100, 2)
            if foo(arr, a, idx + 1) == 0:
                idx  = foo(arr, b, idx + 2)
                pointer_already_set = True

        elif arr[idx] % 100 == 7:
            a, b, c = parameter_state(arr[idx] / 100, 3)
            if c:
                if foo(arr, a, idx + 1) < foo(arr, b, idx + 2):
                    arr[idx + 3] = 1

                else: arr[idx + 3] = 0
            else:
                if foo(arr, a, idx + 1) < foo(arr, b, idx + 2):
                    arr[arr[idx + 3]] = 1
                else: arr[arr[idx + 3]] = 0

        elif arr[idx] % 100 == 8:
            a, b, c = parameter_state(arr[idx] / 100, 3)
            if c:
                if foo(arr, a, idx + 1) == foo(arr, b, idx + 2):
                    arr[idx + 3] = 1
                else: arr[idx + 3] = 0
            else:
                if foo(arr, a, idx + 1) == foo(arr, b, idx + 2):
                    arr[arr[idx + 3]] = 1
                else: arr[arr[idx + 3]] = 0

        elif arr[idx] % 100 == 99: break

        if not pointer_already_set: idx += parameter_length[operation]

intcode(1)

with open ("input.txt", "r") as f:
    arr = map(int, f.readline().strip().split(","))

intcode(5)
