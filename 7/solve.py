input = open("input.txt", 'r')
lines = input.readlines()

def in_map(m, i, j):
    if i < len(m) and i >= 0 and j < len(m[0]) and j >= 0:
        return True
    return False

start_idx = lines[0].index('S')
start = (0, start_idx)

for i in range(len(lines)):
    if lines[i][-1] == '\n':
        lines[i] = list(lines[i][:-1])
    else:
        lines[i] = list(lines[i])

###PART1

count = 0
for i in range(1,len(lines)):
    for j in range(len(lines[i])):
        if lines[i-1][j] == 'S' or lines[i-1][j] == '|':
            if lines[i][j] == '^':
                count += 1
                if in_map(lines, i, j-1):
                    if lines[i][j-1] == '.':
                        lines[i][j-1] = '|'
                if in_map(lines, i, j+1):
                    if lines[i][j+1] == '.':
                        lines[i][j+1] = '|'
            else:
                lines[i][j] = '|'

print(count)
