with open("input.txt", "r") as f:
    time = int(f.readline().strip())
    schedule = f.readline().strip().split(",")

m = [0, 10**12]
for j in [int(i) for i in schedule if i != "x"]:
    if time % j:
        tmp = (time // j + 1) * j - time
        if tmp < m[1]: m[0], m[1] = j, tmp 
        
    else: m = [j, 0]; break

print(m[0] * m[1])

def gcdExtended(a, b):  
    if a == 0 :   
        return 0,1

    x1,y1 = gcdExtended(b%a, a)  
    x = y1 - (b//a) * x1  
    y = x1  
     
    return x,y 

arr = [(int(j), int(j) - i) for i, j in enumerate(schedule) if j != "x"]

M = 1
for j in arr: M *= j[0]

r = 0
for j in arr:
    r += j[1] * gcdExtended(j[0], M//j[0])[1] * M//j[0]

print(r%M)
