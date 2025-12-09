input = open("input.txt", 'r')
lines = input.readlines()

for i in range(len(lines)):
    lines[i] = lines[i].removesuffix("\n")
    lines[i] = lines[i].split(',')

###PART1


best_area = 0
for c1 in range(len(lines)):
    for c2 in range(c1+1, len(lines)):
        #print(lines[c1].removesuffix("\n"), lines[c2].removesuffix("\n"))
        c1_x, c1_y = int(lines[c1][1]), int(lines[c1][0])
        c2_x, c2_y = int(lines[c2][1]), int(lines[c2][0])
        #print(c1_x, c1_y, c2_x, c2_y)
        #print((abs(c2_x-c1_x)+1), (abs(c2_y-c1_y)+1))
        area = (abs(c2_x-c1_x)+1)*(abs(c2_y-c1_y)+1)
        #print(area, c1_x, c1_y, c2_x, c2_y)
        #print(area, best_area)
        if area > best_area:
            best_area = area

print(best_area)

