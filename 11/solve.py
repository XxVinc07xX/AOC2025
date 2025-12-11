from functools import cache
import datetime

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

start = datetime.datetime.now()
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
end = datetime.datetime.now()
print(count)
print(f"time elapsed: {end-start}")

@cache
def memoization(cur):
    if cur == 'out':
        return 1
    res = 0
    next = d[cur]
    for n in next:
        res += memoization(n)
    return res

start = datetime.datetime.now()
count = memoization('you')
end = datetime.datetime.now()
print(count)
print(f"time elapsed: {end-start}")



###PART2

''' working on small example but not on puzzle input

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

'''

@cache #memoization
def parse(cur, dac, fft):
    if cur == 'out':
        return dac & fft
    count = 0
    next = d[cur]
    for n in next:
        count += parse(n, dac | (n == 'dac'), fft | (n == 'fft'))
    return count

count = parse('svr', 0, 0)
print(count)