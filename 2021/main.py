a = [int(j)for i, j in enumerate(open("input").read().strip().split()) if i == 4 or i == 9]



start1 = a[0]
start2 = a[1]
#start1 = 4
#start2 = 8
print(start1, start2)
score1 = 0
score2 = 0
d = 0
while True:
    start1 = start1 + (6 + 9*d - 1) % 100 + 1
    start1 = (start1 - 1) % 10 + 1
    score1 += start1
    d += 1
    if score1 > 999:
        print(score2 * 3 * d)
        break

    start2 = start2 + (6 + 9*d - 1) % 100 + 1
    start2 = (start2 - 1) % 10 + 1
    score2 += start2
    d += 1
    if score2 > 999:
        print(score1 * 3 * d)
        break


print(6.3/8*7000)
