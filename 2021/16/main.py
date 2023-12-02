h = {j.strip().split(" = ")[0]:j.strip().split(" = ")[1] for j in open("hexadecimal")}
a = open("input").read().strip()

b = ""
for l in a: b += h[l]

def foo(c, v=0):
    v += int(c[:3], 2)
    t = c[3:6]
    if int(t, 2) != 4:
        if c[6] == "0": 
            total_length_subpackets = int(c[7:22], 2)
#            while total_length_subpackets:
                
        if c[6] == "1":
            number_of_subpackets    = int(c[7:18], 2)

    else:
        literal = ""
        i = 6
        while c[i] != "0":
            literal += c[i+1:i+5] 
            i += 5
        literal += c[i+1:i+5]
        
#        return int(literal, 2)
    return v
print(foo(b))
