with open("input.txt") as f:
    image = f.readline()
m = 150, 150
for i in range(0, len(image) / 150):
    zeros = image[i * 150:(i + 1) * 150].count("0")
    if zeros < m[0]: m = zeros, i

print image[m[1] * 150:(m[1] + 1) * 150].count("1") * image[m[1] * 150:(m[1] + 1) * 150].count("2")
print
pixels = []
for i in range(150):
    j = i
    color = image[j]
    while image[j] == "2":
        j += 150
        color = image[j]
    
    if color == "1" :    pixels.append(image[j])
    else            :    pixels.append(" ")

for i in range(6):
    print "".join(pixels[i * 25:(i + 1) * 25])
