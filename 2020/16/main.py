import collections
arr, a = [], []
nearby_tickets = []
with open("input.txt", "r") as f:   
    for _ in range(20):
        arr.append(f.readline().strip().split(":")[1].strip().split("or"))
    for i, j in enumerate(arr):
        for k, l in enumerate(j):
            arr[i][k] = map(int, l.strip().split("-"))


    f.readline()
    f.readline()
    my_ticket = map(int, f.readline().strip().split(","))
    f.readline()
    f.readline()
    for j in f:
        nearby_tickets.append(map(int, j.strip().split(",")))
    
#arr = [[[0,1], [4,19]], [[0,5], [8,19]], [[0,13], [16,19]]]
def f(t):
    v = []
    for j in t:
        invalid = True
        for i in arr:
            if (j >= i[0][0] and j <= i[0][1]) or (j >= i[1][0] and j <= i[1][1]): invalid = False
        if invalid: v.append(j)

    if v: return sum(v)




def foo(t):
    r = []
    for idx, i in enumerate(arr):
        valid = []
        for j in t:
            if (j >= i[0][0] and j <= i[0][1]) or (j >= i[1][0] and j <= i[1][1]): valid.append(True)
            else: valid.append(False)
        if all(valid): r.append(idx)

    return r

print(sum([f(j) for j in nearby_tickets if f(j)]))
nearby_tickets = [j for j in nearby_tickets if not f(j)]


r = []
#for j in zip(*([my_ticket] + nearby_tickets)):
for j in zip(*nearby_tickets):
    r.append(foo(j))
results = []
while min([x for y in r for x in y]) < 5:
    for i, j in enumerate(r):
        if len(j) == 1:
            tmp = j[0]
            results.append((i, j[0]))


    for i, j in enumerate(r):
        if tmp in j: r[i].remove(tmp)

p = 1
for j in results:
    if j[1] <= 6:
        p*= my_ticket[j[0]]
print(results)
print(p)
