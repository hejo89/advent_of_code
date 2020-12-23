arr = [j.strip() for j in open("input.txt")]
d  = {"NS":0, "EW":0}
direction = 1

for c in arr:
    if c[:1] == "N": d["NS"] += int(c[1:])
    if c[:1] == "E": d["EW"] += int(c[1:])
    if c[:1] == "S": d["NS"] -= int(c[1:])
    if c[:1] == "W": d["EW"] -= int(c[1:])
    if c[:1] == "R": direction = (direction + int(c[1:]) // 90) % 4        
    if c[:1] == "L": direction = (direction - int(c[1:]) // 90) % 4
    if c[:1] == "F": 
        if direction == 0: d["NS"] += int(c[1:])
        if direction == 1: d["EW"] += int(c[1:])
        if direction == 2: d["NS"] -= int(c[1:])
        if direction == 3: d["EW"] -= int(c[1:])

print(sum(map(abs, d.values())))

d  = {"NS":0, "EW":0}
wp = {"NS":1, "EW":10}

for c in arr:

    if c[:1] == "N": wp["NS"] += int(c[1:])
    if c[:1] == "E": wp["EW"] += int(c[1:])
    if c[:1] == "S": wp["NS"] -= int(c[1:])
    if c[:1] == "W": wp["EW"] -= int(c[1:])
    if c[:1] in "RL":

        tmp = (int(c[1:]) // 90) % 4
        if c[:1] == "L": tmp = (4 - tmp) % 4
        if tmp == 1:
            a, b = wp.values()
            wp["NS"] -= a + b
            wp["EW"] -= b - a
        if tmp == 2:
            a, b = wp.values()
            wp["NS"] -= 2*a
            wp["EW"] -= 2*b
        if tmp == 3:
            a, b = wp.values()
            wp["NS"] -= a - b
            wp["EW"] -= b + a

    if c[:1] == "F":        
        for j in wp:
            d[j] += int(c[1:]) * wp[j]

print(sum(map(abs, d.values())))

