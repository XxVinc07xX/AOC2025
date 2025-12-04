input = open("input.txt", "r")
lines = input.readlines()

puzzle = []

for line in lines:
    puzzle.append(line.removesuffix("\n"))

#print(puzzle)

####################FUNCTIONS####################

def count_adj(p, i, j):
    count = 0
    up = (i-1, j)
    if in_map(p, up[0], up[1]) and p[up[0]][up[1]] == '@':
        count += 1
    down = (i+1, j)
    if in_map(p, down[0], down[1]) and p[down[0]][down[1]] == '@':
        count += 1
    right = (i, j+1)
    if in_map(p, right[0], right[1]) and p[right[0]][right[1]] == '@':
        count += 1
    left = (i, j-1)
    if in_map(p, left[0], left[1]) and p[left[0]][left[1]] == '@':
        count += 1
    d_ur = (i-1, j+1)
    if in_map(p, d_ur[0], d_ur[1]) and p[d_ur[0]][d_ur[1]] == '@':
        count += 1
    d_ul = (i-1, j-1)
    if in_map(p, d_ul[0], d_ul[1]) and p[d_ul[0]][d_ul[1]] == '@':
        count += 1
    d_dl = (i+1, j-1)
    if in_map(p, d_dl[0], d_dl[1]) and p[d_dl[0]][d_dl[1]] == '@':
        count += 1
    d_dr = (i+1, j+1)
    if in_map(p, d_dr[0], d_dr[1]) and p[d_dr[0]][d_dr[1]] == '@':
        count += 1
    return count

def in_map(p, i, j):
    if i < len(p) and i >= 0 and j < len(p[i]) and j >= 0:
        return True
    return False


#################################################

###PART1

count = 0
ok = []
for i in range(len(puzzle)):
    for j in range(len(puzzle[i])):
        if puzzle[i][j] == '@':
            res = count_adj(puzzle, i, j)
            #print(res, i, j)
            if res < 4:
                count += 1
                ok.append((i,j))

print(count)