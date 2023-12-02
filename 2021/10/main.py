a = open("input").read().split()
brackets = {")":"(", "]":"[", "}":"{", ">":"<"}
s1 = 0
s2 = []
for j in a:
    corrupted = False
    stack = []
    for k in j:
        if not stack and k in brackets.values()               : stack.append(k)
        elif k in brackets.keys() and stack[-1] == brackets[k]: stack.pop()
        elif k in brackets.keys() and stack[-1] != brackets[k]: 

            if k == ")": s1 += 3
            if k == "]": s1 += 57
            if k == "}": s1 += 1197
            if k == ">": s1 += 25137
            
            corrupted = True

            break
            
        else: stack.append(k)

    if not corrupted:
        s = 0
        for k in stack[::-1]:
            s *= 5
            if k == "(": s += 1
            if k == "[": s += 2
            if k == "{": s += 3
            if k == "<": s += 4
            
        s2.append(s)

print(s1)
print(sorted(s2)[len(s2)//2])
