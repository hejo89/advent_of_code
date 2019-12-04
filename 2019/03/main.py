with open("input.txt", "r") as f:
    a_wire = f.readline().strip().split(",")
    b_wire = f.readline().strip().split(",")
a_wire = ["R8","U5","L5","D3"]
b_wire = ["U7","R6","D4","L4"]
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
               
                if i[0][0] == "L" or  i[0][0] == "R":m = min(m,  abs(i[1][0]) + abs(j[2][0])); print i, j, (i[1][0] , j[2][0]), a_positions[i[3]], b_positions[j[3]]; wire_length.append(sum([int(x[1:]) for x in a_wire[:i[3]]]))

                if i[0][0] == "U" or  i[0][0] == "D":m = min(m,  abs(i[2][0]) + abs(j[1][0])); print i, j, (i[2][0] , j[1][0]), a_positions[i[3]], b_positions[j[3]]
        if (i[0] == "U" or i[0] == "D") and (j[0] == "R" or j[0] == "L"):
            a, b, c, d = i[1][0] - j[1][0]  , i[1][1] - j[1][1], i[2][0] - j[2][0], i[2][1] - j[2][1]
            if a*b < 0 and c*d <0:

                if i[0][0] == "L" or  i[0][0] == "R":m = min(m,  abs(i[1][0]) + abs(j[2][0])); print i, j, (i[1][0] , j[2][0]), a_positions[i[3]], b_positions[j[3]]
                if i[0][0] == "U" or  i[0][0] == "D":m = min(m,  abs(i[2][0]) + abs(j[1][0])); print i, j, (i[2][0] , j[1][0]), a_positions[i[3]], b_positions[j[3]]

print a_positions
print b_positions
#print m
print sum([int(x[1:]) for x in a_wire])
print [int(x[1:]) for x in a_wire]
print wire_length









