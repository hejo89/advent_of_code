m = 0
ids = []
with open("input.txt", "r") as f:
    for l in f:
        tmp = list(l.strip())
        for i, j in enumerate(tmp[:7]):
            if j == "F": tmp[i] = "0"
            if j == "B": tmp[i] = "1"

        for i, j in enumerate(tmp[7:], 7):
            if j == "L": tmp[i] = "0"
            if j == "R": tmp[i] = "1"
        row = tmp[:7]
        col = tmp[7:]
        ids.append(int("".join(row), 2) * 8 + int("".join(col), 2))

        m = max(int("".join(row), 2) * 8 + int("".join(col), 2), m)

print(m)

ids.sort()
print(list(set(range(min(ids), max(ids) + 1)).difference(set(ids))))[0]
