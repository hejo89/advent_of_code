import collections

a = [map(int, list(j)) for j in open("input").read().split()]

def clamp(x, y):
    return min(max(0, x), len(a) - 1), min(max(0, y), len(a[0]) - 1)

def adjacent(x, y):
    s = set()
    for i in range(-1, 2):
        for j in range(-1, 2):
            s.add(clamp(x+i, y+j))
    s.remove((x, y))    
    return s


total_flashes = 0

def foo():
    global total_flashes
    flash = []
    flash1 = set()
    for i in range(len(a)):
        for j in range(len(a[0])):
            a[i][j] += 1
            if a[i][j] == 10: flash.append((i, j)); a[i][j] = 0; flash1.add((i, j))

    while flash:
        f = flash.pop()
        for j in adjacent(*f):
            if j not in flash1:
                x,y = j
                a[x][y] += 1
                if a[x][y] == 10: flash.append(j); a[x][y] = 0; flash1.add((x, y))

    total_flashes += len(flash1)
    return len(flash1)


for _ in range(100): foo()

print(total_flashes)

a = [map(int, list(j)) for j in open("input").read().split()]

size = len(a) * len(a[0])

steps = 0
while True:
    t = foo()
    steps += 1
    if t == size: break

print(steps)
