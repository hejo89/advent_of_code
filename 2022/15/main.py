import collections
sb = {}
area = set()
with open('input.txt', 'r') as f:
    for l in f: 
        tmp = l.strip().split()
        x, y = float(tmp[2].split('=')[1].strip(',')), float(tmp[3].split('=')[1].strip(':'))
        a, b = float(tmp[8].split('=')[1].strip(',')), float(tmp[9].split('=')[1])
        sb[(x, y)] = (a, b)



###################################################################################
########################        PART 1        #####################################
###################################################################################
#y = 10
#b_set = set(sb.values())
#s = set()
#for c in sb:
#    d = abs(c[0] - sb[c][0]) + abs(c[1] - sb[c][1])
#    for x in range(int(d) - abs(int(c[1]) - y) + 1):
#        s.add(c[0] + x)
#        s.add(c[0] - x) 

#for b in b_set:
#    if b[1] == y and b[0] in s:
#        s.remove(b[0])

#        
#print(len(s))

###################################################################################
########################        PART 2        #####################################
###################################################################################



#dct = collections.defaultdict(list)
#range_map = {}
#for sensor in sb:
#    print(sensor)
#    beacon = sb[sensor]
#    d = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
#    for x in range(int(d) + 1):
#        print(x)
#        dct[sensor[1] + x].append([sensor[0]-int(d) + x, sensor[0] + int(d) - x])
#        dct[sensor[1] - x].append([sensor[0]-int(d) + x, sensor[0] + int(d) - x])

#    break
#for j in dct:
#    interval = sorted(dct[j])
#    stack = [interval[0]]
#    for i in interval[1:]:
#        if i[0] <= stack[-1][1] + 1:
#            stack[-1][1] = max(i[1], stack[-1][1])
#        else:
#            stack.append(i)
#        

#    range_map[j] = stack

#for j in range_map:
#    print(j, range_map[j])


#            
#for j in s:
#    if j[0] in dct:
#        dct[j[0]] = (min(dct[j[0]][0], j[1][0]), max(dct[j[0]][1], j[1][1]))
#    else:
#        dct[j[0]] = [j[1]]
#        
##for x in sorted(dct.keys()):
##    print(x, dct[x])

##for j in s:
##    if j[0] == 11:
##        print(j)














