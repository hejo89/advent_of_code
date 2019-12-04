with open("input.txt", "r") as f:
    a_wire = f.readline().strip().split(",")
    b_wire = f.readline().strip().split(",")
#a_wire = ["R8","U5","L5","D3"]
#b_wire = ["U7","R6","D4","L4"]

#a_wire = ["R75","D30","R83","U83","L12","D49","R71","U7","L72"]
#b_wire = ["U62","R66","U55","R34","D71","R55","D58","R83"]

#a_wire = ["R98","U47","R26","D63","R33","U87","L62","D20","R33","U53","R51"]
#b_wire = ["U98","R91","D20","R16","D67","R40","U7","R15","U6","R7"]

#a_wire = ["R100","U150"]
#b_wire = ["U100","R150"]

a_positions = [(0, 0)]
b_positions = [(0, 0)]

for j in a_wire:
    if j[0] == "R": a_positions.append((a_positions[-1][0], a_positions[-1][1] + int(j[1:])))
    if j[0] == "U": a_positions.append((a_positions[-1][0] + int(j[1:]), a_positions[-1][1]))
    if j[0] == "L": a_positions.append((a_positions[-1][0], a_positions[-1][1] - int(j[1:])))
    if j[0] == "D": a_positions.append((a_positions[-1][0] - int(j[1:]), a_positions[-1][1]))

for j in b_wire:
    if j[0] == "R": b_positions.append((b_positions[-1][0], b_positions[-1][1] + int(j[1:])))
    if j[0] == "U": b_positions.append((b_positions[-1][0] + int(j[1:]), b_positions[-1][1]))
    if j[0] == "L": b_positions.append((b_positions[-1][0], b_positions[-1][1] - int(j[1:])))
    if j[0] == "D": b_positions.append((b_positions[-1][0] - int(j[1:]), b_positions[-1][1]))

test = []
test2 = []
m = 10**9
wire_length = []
for i, j in enumerate(a_positions[1:]):
    test.append((a_wire[i][0], (a_positions[i][0], j[0]), (a_positions[i][1], j[1]), i))

for i, j in enumerate(b_positions[1:]):
    test2.append((b_wire[i][0], (b_positions[i][0], j[0]), (b_positions[i][1], j[1]), i))


for i in test:
    for j in test2:
        if (i[0] == "R" or i[0] == "L") and (j[0] == "U" or j[0] == "D"):
            a, b, c, d =  i[1][0] - j[1][0]  , i[1][1] - j[1][1], i[2][0] - j[2][0], i[2][1] - j[2][1]
            if a*b < 0 and c*d <0:
               
                if i[0][0] == "L" or  i[0][0] == "R":m = min(m,  abs(i[1][0]) + abs(j[2][0])); l = sum([int(x[1:]) for x in a_wire[:i[3]]] + [int(x[1:]) for x in b_wire[:j[3]]] + [abs(a_positions[i[3]][0] - i[1][0]) + abs(a_positions[i[3]][1] - j[2][0])] + [abs(b_positions[j[3]][0] - i[1][0]) + abs(b_positions[j[3]][1] - j[2][0])]); wire_length.append(l)

                if i[0][0] == "U" or  i[0][0] == "D":m = min(m,  abs(i[2][0]) + abs(j[1][0])); l = sum([int(x[1:]) for x in a_wire[:i[3]]] + [int(x[1:]) for x in b_wire[:j[3]]] + [abs(a_positions[i[3]][0] - j[1][0]) + abs(a_positions[i[3]][1] - i[2][0])] + [abs(b_positions[j[3]][0] - j[1][0]) + abs(b_positions[j[3]][1] - i[2][0])]); wire_length.append(l)
        if (i[0] == "U" or i[0] == "D") and (j[0] == "R" or j[0] == "L"):
            a, b, c, d = i[1][0] - j[1][0]  , i[1][1] - j[1][1], i[2][0] - j[2][0], i[2][1] - j[2][1]
            if a*b < 0 and c*d <0:

                if i[0][0] == "L" or  i[0][0] == "R":m = min(m,  abs(i[1][0]) + abs(j[2][0]));l = sum([int(x[1:]) for x in a_wire[:i[3]]] + [int(x[1:]) for x in b_wire[:j[3]]] + [abs(a_positions[i[3]][0] - i[1][0]) + abs(a_positions[i[3]][1] - j[2][0])] + [abs(b_positions[j[3]][0] - i[1][0]) + abs(b_positions[j[3]][1] - j[2][0])]); wire_length.append(l)
                if i[0][0] == "U" or  i[0][0] == "D":m = min(m,  abs(i[2][0]) + abs(j[1][0]));l = sum([int(x[1:]) for x in a_wire[:i[3]]] + [int(x[1:]) for x in b_wire[:j[3]]] + [abs(a_positions[i[3]][0] - j[1][0]) + abs(a_positions[i[3]][1] - i[2][0])] + [abs(b_positions[j[3]][0] - j[1][0]) + abs(b_positions[j[3]][1] - i[2][0])]); wire_length.append(l)

print m
print min(wire_length)
