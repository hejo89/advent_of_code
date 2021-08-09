a = [list(j.strip().replace(" ", "")) for j in open("input.txt")]



def F(s):
    if s[-1].isdigit(): return int(s.pop())
    s.pop()
    x = E(s)
    s.pop()
    return x

def T(s):
    x = F(s)
    if s and s[-1] in "+-":
        o = s.pop()
        y = T(s)
        if o == "+": x += y
        else       : x -= y
    return x


def E(s):
    x = T(s)
    if s and s[-1] in "*/":
        o = s.pop()
        y = E(s)
        if o == "*": x *= y
        else       : x /= y

    return x

print(sum(E(j) for j in a))
