import re
n = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
s = 0

pattern = re.compile(r'\d|(?=(' + '|'.join(n.keys()) + '))')

for l in open('input.txt', 'r'):

    d = [n for m in [match.group(0, 1) for match in pattern.finditer(l.strip())] for n in m if n]

    if d[0] in n:
        a = n[d[0]]
    else:
        a = d[0]      

    if d[-1] in n:
        b = n[d[-1]]
    else:
        b = d[-1]
    s += int(a + b)
    
print(s)

