inpt = (open("input.txt").read().strip().split("\n\n"))
s = list(map(int, inpt.pop(0).split()[1:]))
print(s)
