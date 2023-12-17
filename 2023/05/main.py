inpt = (open("input.txt").read().strip().split("\n\n"))
s = list(map(int, inpt.pop(0).split()[1:]))
m = [[list(map(int, k.split())) for k in j.split('\n')[1:]] for j in inpt]




print(s)
print(m)
