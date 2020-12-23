s1 = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"])
s2 = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
validation_rules = {"byr": set(map(str, range(1920, 2003))), "iyr": set(map(str, range(2010, 2021))), "eyr": set(map(str, range(2020, 2031))), "hgt": {"cm": set(map(str, range(150, 194))), "in": set(map(str, range(59, 77)))}, "ecl": set(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])}
print(validation_rules)
c = 0
arr = [{}]

with open("input.txt", "r") as f:
    for l in f:
        if l.strip() == "":
            s = set(arr[-1].keys())
            valid_id = False
            if s == s1 or s == s2:
                valid_id = True
                for j in s:
                    tmp = arr[-1][j]
                    if   j == "cid": continue 
                    elif j == "hcl":
                        if len(tmp) != 7 or tmp[0] != "#": valid_id = False
                        for l in tmp[1:]:
                            if l not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']: valid_id = False
                    elif j == "pid":
                        if len(tmp) != 9: valid_id = False
                        for l in tmp:
                            if l not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']: valid_id = False
                    elif j == "hgt":
                        if tmp[-2:] not in ["cm", "in"]: valid_id = False; break
                        if tmp[-2:] == "cm":
                            if tmp[:-2] not in validation_rules[j]["cm"]: valid_id = False
                        if tmp[-2:] == "in":
                            if tmp[:-2] not in validation_rules[j]["in"]: valid_id = False
                    elif arr[-1][j] not in validation_rules[j]: valid_id = False

                if valid_id: c += 1
            arr.append({})
        else: 
            for j in l.strip().split():
                a, b = j.split(":")
                arr[-1][a] = b

print(c)
