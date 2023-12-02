import re
import collections

def game(a, red = 0, green = 0, blue = 0, valid_game = True):
    for s in a.strip().split(';'):
        g = collections.defaultdict(int)
        for c in re.findall(r'(\d+)\s*([a-zA-Z]+)', s):
            g[c[1]] = int(c[0])
        red, green, blue = max(red, g['red']), max(green, g['green']), max(blue, g['blue'])
        if g['red'] > 12 or g['green'] > 13 or g['blue'] > 14:
            valid_game = False
    return valid_game, red * green * blue
    
n = 0
m = 0
for idx, l in enumerate(open('input.txt'), 1):
    a, b = game(l)[0], game(l)[1]
    if a: n += idx
    m += b
print(n)
print(m)
