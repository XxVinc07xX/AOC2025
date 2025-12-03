input = open("input.txt", 'r')
lines = input.readlines()

for l in lines:
    l = l.removesuffix("\n")

sum = 0
for line in lines:
    line = line.removesuffix("\n")
    best = 0
    for i in range(len(line)):
        for j in range(len(line)):
            if i != j and i < j:
                if int(line[i] + line[j]) > best:
                    best = int(line[i] + line[j])

    #print(best)
    sum += best

print(sum)
