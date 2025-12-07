import copy
from functools import lru_cache

input = open("input.txt", 'r')
lines = input.readlines()

lines_pt2 = copy.deepcopy(lines)

lines_pt3 = copy.deepcopy(lines)

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


###PART2

'''

##inefficient, DFN does not work for input puzzle
for i in range(len(lines_pt3)):
    if lines_pt3[i][-1] == '\n':
        lines_pt3[i] = list(lines_pt3[i][:-1])
    else:
        lines_pt3[i] = list(lines_pt3[i])


end = []
to_visit = [(1, start_idx)]

while (len(to_visit) != 0):
    print(len(to_visit))
    cur = to_visit.pop(0)
    cur_x, cur_y = cur[0], cur[1]
    if cur[0] == len(lines_pt3)-1:
        lines_pt3[cur_x][cur_y] = '|'
        end.append(cur)
    else:
        if lines_pt3[cur_x][cur_y] == '.' or lines_pt3[cur_x][cur_y] == '|':
            lines_pt3[cur_x][cur_y] = '|'
            to_visit.append((cur_x+1, cur_y))
        elif lines_pt3[cur_x][cur_y] == '^':
            if in_map(lines_pt3, cur_x, cur_y-1):
                lines_pt3[cur_x][cur_y-1] = '|'
                to_visit.append((cur_x, cur_y-1))
            if in_map(lines_pt3, cur_x, cur_y+1):
                lines_pt3[cur_x][cur_y+1] = '|'
                to_visit.append((cur_x, cur_y+1))

print(len(end))
'''

@lru_cache
def count_path(x, y):
    if not in_map(lines, x, y):
        return 0
    if x == len(lines)-1:
        return 1
    
    if lines[x][y] == '.' or lines[x][y] == '|':
        return count_path(x+1, y)
    
    if lines[x][y] == '^':
        return count_path(x, y-1) + count_path(x, y+1)
    
    return 0

result = count_path(1, start_idx)
print(result)