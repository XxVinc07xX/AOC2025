input = open("input.txt", 'r')
lines = input.readlines()

###PART1

#get the fresh IDs
index = 0
fresh = []
for line in lines:
    index += 1
    #print(index)
    line = line.removesuffix("\n")
    if line == "":
        break
    s = line.split("-")
    inf = int(s[0])
    sup = int(s[1])
    fresh.append((inf, sup))

count = 0
for i in range(index, len(lines)):
    lines[i] = lines[i].removesuffix("\n")
    lines[i] = int(lines[i])
    for f in fresh:
        if lines[i] >= f[0] and lines[i] <= f[1]:
            count += 1
            break

print(count)



