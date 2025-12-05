import copy

input = open("input.txt", 'r')
lines = input.readlines()

###PART1

#get the fresh IDs
index = 0
fresh = []
for line in lines:
    index += 1
    #print(index)
    line = line.removesuffix("\n")
    if line == "":
        break
    s = line.split("-")
    inf = int(s[0])
    sup = int(s[1])
    fresh.append([inf, sup])

count = 0
for i in range(index, len(lines)):
    lines[i] = lines[i].removesuffix("\n")
    lines[i] = int(lines[i])
    for f in fresh:
        if lines[i] >= f[0] and lines[i] <= f[1]:
            count += 1
            break

print(count)

###PART2

'''
Idea:
1)parse list
2) if current element is the same at the end of the list (no overlapping) => increment count with right number of element and indicate to not take it in account anymore
   if current element is changed => start again the loop with the changed element
3) until all element have been taken into account
'''
start_nb = len(fresh)
count = 0
to_ignore = []
while(len(to_ignore) != start_nb):
    for i in range(len(fresh)):
        if i not in to_ignore:
            start = copy.deepcopy(fresh[i])
            cur = fresh[i]
            for j in range(len(fresh)):
                if i != j:
                    if j not in to_ignore:
                        if fresh[j][0] >= cur[0] and fresh[j][1] <= cur[1]:
                            to_ignore.append(j)
                        elif fresh[j][0] <= cur[0] and fresh[j][1] >= cur[1]:
                            to_ignore.append(i)
                            cur = fresh[j]
                        elif fresh[j][0] <= cur[1] and fresh[j][0] >= cur[0]:
                            cur[1] =  fresh[j][1]
                            to_ignore.append(j)
                            #print(cur)
                        elif fresh[j][0] <= cur[0] and fresh[j][1] >= cur[0]:
                            cur[0] = fresh[j][0]
                            to_ignore.append(j)
            if cur == start:
                to_ignore.append(i)
                count += cur[1] - cur[0] + 1
            else:
                fresh[i] = cur


print(count)


