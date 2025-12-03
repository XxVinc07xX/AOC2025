input = open("input.txt", 'r')
lines = input.readlines()

#########################FUNCTIONS#########################

'''
sub: the substring to found max
'''
def max_idx(sub):
    l = list(map(int,sub))
    #print(l)
    m = max(l)
    idx = l.index(m)
    return idx



#########################FUNCTIONS#########################


###PART1

sum = 0
for line in lines:
    line = line.removesuffix("\n")
    best = 0
    for i in range(len(line)):
        for j in range(len(line)):
            if i != j and i < j:
                if int(line[i] + line[j]) > best:
                    best = int(line[i] + line[j])

    #print(best)
    sum += best

#print(sum)

###PART2

sum = 0
for line in lines:
    line = line.removesuffix("\n")
    found = 0
    cur_best_idx = None
    cur = ''
    
    #donner l[:-11] : trouver max
    #donner l[max:-10]: trouver max
    #donner l[max:-9]: trouver max 
    #...
    for _ in range(len(line)):
        if cur_best_idx == None:
            sub = line[:-11]
            start_sub_idx = line.index(line[0])
            end_sub_idx = line.index(line[-1])
        else:
            #print(cur_best_idx, found)
            if (-11+found) != 0: 
                sub = line[cur_best_idx+1:-11+found]
            else:
                sub = line[cur_best_idx+1:]
            #print("sub = " +  str(sub))
            start_sub_idx = cur_best_idx+1
            end_sub_idx = len(line)-11+found-1
            #print(start_sub_idx, end_sub_idx)
            #print("sub = " + str(sub))
        #print("sub = " +  str(sub))
        maxi = max_idx(sub)
        cur += sub[maxi]
        found += 1
        #print(start_sub_idx, maxi)
        cur_best_idx = start_sub_idx + maxi
        if found == 12:
            best = int(cur)
            break

    best = int(cur)
    print("best = " + str(best))
    sum += best

print(sum)
