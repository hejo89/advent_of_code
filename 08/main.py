ipt = open('input.txt').read().split('\n\n')
instruction = ipt[0]
maps = {j.split('=')[0].strip():j.split('=')[1].strip()[1:-1].split(', ') for j in ipt[1].split('\n') if j}
turn = {'L': 0, 'R': 1}

steps = 0
pos = 'AAA'
while pos != 'ZZZ':
    pos = maps[pos][turn[instruction[steps % len(instruction)]]]
    steps += 1
print(steps)
s = len(instruction)
for j in maps:
    start = j
    if j[-1] == 'A':
        i = 0
        while j[-1] != 'Z':
            j = maps[j][turn[instruction[i % len(instruction)]]]
            i += 1
        s *= i // len(instruction)
print(s)
