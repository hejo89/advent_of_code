a = [18,8,0,5,4,1,20]
d = {j:i for i, j in enumerate(a[:-1])}
i = len(a) - 1
x = a[-1]
for N in 2020, 30000000:
    while i < N:
        y = x
        if x in d: x = i - d[x]
        else: x = 0
        d[y] = i
        i += 1
    print(y)



#a = [18,8,0,5,4,1,20]
#coord = {j:[i] for i, j in enumerate(a)}
#c = 7
#l = a[-1]
#while c < 3e7:
#    print(c)
#    if len(coord[l]) == 1:
#        l = 0
#        coord[0].append(c)
#        c += 1
#    else:
#        l = coord[l][-1] - coord[l][-2]
#        if l in coord: coord[l].append(c)
#        else: coord[l] = [c]
#        c += 1

#    if len(coord[0]) > 2: coord[0] = coord[0][-2:]
#    if len(coord[l]) > 2: coord[l] = coord[l][-2:]
#    
#    if c == 2020: print (l)
#print(l)

