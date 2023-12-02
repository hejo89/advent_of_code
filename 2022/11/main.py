#import collections
#import math
#d = {}
#number_of_items_inspected = collections.defaultdict(int)
#with open('input.txt', 'r') as f:
#    for i, l in enumerate(f):
#        if not i % 7:
#            d[i//7] = []
#            continue
#        if i % 7 == 1:
#            d[i//7].append(list(map(int, l.strip().split(':')[1].split(','))))
#        if i % 7 == 2:
#            d[i//7].append(l.strip().split('old ')[1].split(' '))
#        if i % 7 == 3:
#            d[i//7].append(int(l.strip().split('by ')[1]))
#        if i % 7 == 4:
#            d[i//7].append(int(l.strip().split('monkey ')[1]))
#        if i % 7 == 5:
#            d[i//7].append(int(l.strip().split('monkey ')[1]))    


#rounds = 20
#for j in range(rounds):
#    for m in d:
#        number_of_items_inspected[m] += len(d[m][0])
#        while d[m][0]:
#            w        = d[m][0].pop(0)
#            operator = d[m][1][0]
#            operant  = d[m][1][1]
#            if operator == '+':
#                if operant == 'old':
#                    w *= 2

#                else:
#                    w += int(operant)

#            if operator == '*':
#                if operant == 'old':
#                    w *= w

#                else:
#                    w *= int(operant)

#            
##            w //= 3
#            
#            if not w % d[m][2]:
#                d[d[m][3]][0].append(w)

#            else:
#                d[d[m][4]][0].append(w)
##        print(d)
##print(number_of_items_inspected)
##c = sorted(number_of_items_inspected.values())
##r = c[-1] * c[-2]
##print(r)




import collections
import math
d = {}
number_of_items_inspected = collections.defaultdict(int)
with open('input.txt', 'r') as f:
    for i, l in enumerate(f):
        if not i % 7:
            d[i//7] = []
            continue
        if i % 7 == 1:
            d[i//7].append(list(map(int, l.strip().split(':')[1].split(','))))
        if i % 7 == 2:
            d[i//7].append(l.strip().split('old ')[1].split(' '))
        if i % 7 == 3:
            d[i//7].append(int(l.strip().split('by ')[1]))
        if i % 7 == 4:
            d[i//7].append(int(l.strip().split('monkey ')[1]))
        if i % 7 == 5:
            d[i//7].append(int(l.strip().split('monkey ')[1]))    

p = 1
for j in d:
    p *= d[j][2]

for j in range(10**4):

#    if j == 861:
#        for k in d[3][0]:
#            print(math.log(k, 10))
#        break 
    for m in d:
        number_of_items_inspected[m] += len(d[m][0])
#        print(len(d[m][0]))
        while d[m][0]:
            w        = d[m][0].pop(0)
            operator = d[m][1][0]
            operant  = d[m][1][1]
            if operator == '+':
                if operant == 'old':
                    w *= 2
                else:
                    w += int(operant)

            if operator == '*':
                if operant == 'old':
                    w *= w

                else:
                    w *= int(operant)

            
#            w //= 3

            if not w % d[m][2]:
                d[d[m][3]][0].append(w % p)
#                d[d[m][3]][0].append(w % d[m][2])

            else:
#                d[d[m][4]][0].append(w)
                d[d[m][4]][0].append(w % p)


print(number_of_items_inspected)
c = sorted(number_of_items_inspected.values())
r = c[-1] * c[-2]
print(r)


