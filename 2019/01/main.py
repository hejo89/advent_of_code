arr = []
with open("input.txt", "r") as f:
    for l in f: arr.append(int(l.strip()))

def additional_fuel(mass_init, mass_total):
    if mass_init / 3 - 2 <= 0: return mass_total
    mass_total += mass_init / 3 - 2
    return additional_fuel(mass_init / 3 - 2, mass_total)

print sum([additional_fuel(j, 0) for j in arr])
