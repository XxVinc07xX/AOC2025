input = open("input.txt", 'r')
lines = input.readlines()

cur = 50
count = 0
for line in lines:
    line = line.removesuffix("\n")
    direction = line[0]
    rotation = int(line[1:])
    #print(direction, rotation)

    if direction == 'L':
        cur = (cur-rotation) % 100
    elif direction == 'R':
        cur = (cur+rotation) % 100
    
    #print(cur)
    
    if cur == 0:
        count += 1

print(count)