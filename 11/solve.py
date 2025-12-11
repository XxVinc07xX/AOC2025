input = open("input.txt", 'r')
lines = input.readlines()

d = {}
for line in lines:
    #print(line)
    line = line.removesuffix("\n")
    line = line.split(":")
    line[1] = line[1].lstrip().split(" ")
    d[line[0]] = line[1]

###PART1 

visited = []
to_visit = ['you']

count = 0
while len(to_visit) != 0:
    cur = to_visit.pop(0)
    if cur == 'out':
        count += 1
        continue

    else:
        if cur in d.keys():
            val = d[cur]
            for v in val:
                to_visit.append(v)

print(count)

