arr = [j.strip().split() for j in open("input.txt")]

h, v = 0, 0

for x in arr:
    if x[0] == "forward": h += int(x[1])
    if x[0] ==    "down": v += int(x[1])
    if x[0] ==      "up": v -= int(x[1]) 

print(h*v)

h, v, a = 0, 0, 0

for x in arr:
    if x[0] == "forward": h += int(x[1]); v += a*int(x[1])
    if x[0] ==    "down": a += int(x[1])
    if x[0] ==      "up": a -= int(x[1]) 

print(h*v)
