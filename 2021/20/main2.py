ss = ""
b = []
a = open("input").read().split("\n")[:-1]
for i, j in enumerate(a):
    if j != "": ss += j
    else: break
for j in a[i+1:]:
    b.append(list(j))

for i in range(len(b[:-2])):
    for j in range(len(b[0][::-2])):
        s = ""
        for x in range(3):
            for y in range(3):
                tmp = b[i + x][j + y]
                if tmp == "#": s += "1"
                else         : s += "0"
        print s, int(s, 2)

arr = [[0]*5]*5
print(arr)
def foo(n):
    i = 0
    while i < len(b):
        j = 0
        while j < len(b[0]):
            s = ""
            for x in range(-1, 2):  
                for y in range(-1, 2):
                    if   x + i < 0  or x + i > len(b) - 1 or y + j < 0  or y + j > len(b[0]) - 1   :
                        if n % 2: s += "0"
                        else    : s += "1"
                    elif x + i >= 0 or x + i < len(b)     or y + j >= 0 or y + j < len(b[0])       :
                        tmp = b[i + x][j + y]
                        if tmp == "#": s += "1"
                        else         : s += "0"

            print(s, ss[int(s, 2)])
            arr[i][j] = ss[int(s, 2)]
            j += 1
        i += 1
        

foo(1)

for j in arr:
    print j
