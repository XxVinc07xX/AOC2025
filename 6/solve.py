import math

input = open("input.txt", 'r')
lines = input.readlines()

###PART1

numbers = []
operators = []
for i in range(len(lines)):
    line = lines[i].rstrip().lstrip().removesuffix("\n").split(" ")
    new_line = []
    for j in range(len(line)):
        if line[j] != '':
            new_line.append(line[j])
    if i == len(lines)-1:
        operators = new_line
    else:
        numbers.append(new_line)

assert(len(numbers[0]) == len(numbers[1]) == len(numbers[2]) == len(operators))
count = 0
for i in range(len(numbers[0])):
    op = operators[i]
    cur = []
    for j in range(len(numbers)):
        cur.append(int(numbers[j][i]))
    if op == "+":
        count += sum(cur)
    elif op == "*":
        count += math.prod(cur)

print(count)