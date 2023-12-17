import collections
high_card = {'A': 12, 'K': 11, 'Q': 10, 'J': 9, 'T': 8, '9': 7, '8': 6, '7': 5, '6': 4, '5': 3, '4': 2, '3': 1, '2': 0}

hands = []
with open('input.txt', 'r') as f:
    for l in f:

        r = collections.defaultdict(int)
        d = collections.defaultdict(int)
        for c in l.strip().split()[0]: d[c] += 1
        for j in d: r[d[j]] += 1


        if 5 in r.keys():
            t = 6            
        elif 4 in r.keys():
            t = 5
        elif 3 in r.keys() and 2 in r.keys():
            t = 4
        elif 3 in r.keys():
            t = 3
        elif 2 in r.keys() and r[2] == 2:
            t = 2
        elif 2 in r.keys():
            t = 1
        else:
            t = 0

        hands.append([t, [high_card[c] for c in l.strip().split()[0]], int(l.strip().split()[1])])            
total = 0

for idx, x in enumerate(sorted(hands), 1):
    total += idx * x[-1]
print(total)
