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

###PART2

def containing_target(path):
    if 'dac' in path and 'fft' in path:
        return True
    return False

to_visit = [['svr', []]]
count = 0
while len(to_visit) != 0:
    cur, path = to_visit.pop(0)

    if cur == 'out' and containing_target(path):
        count += 1
        continue

    else:
        if cur in d.keys():
            val = d[cur]
            for v in range(len(val)):
                to_visit.insert(v,[val[v], path + [cur]])

print(count)