a = [list(j.strip().replace(" ", "")) for j in open("input.txt")]
def f(s):
    t = s.pop()
    if t.isdigit():
        x = int(t)
    elif t == ")":
        x = f(s)
        s.pop()  # open parentheses
    while s and s[-1] in "+*":
        o = s.pop()
        if o == "+": return x + f(s)
        if o == "*": return x * f(s)

    return x



print sum(f(j) for j in a)

