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

print(sum)

###PART2

'''
found each time the maximum in the sublist starting after current best index and endind with enough element left in case best is last element of the sublist
Example: 111111111119111 => 111111119111; 9 cannot be the first number since there is not enough digit left to form a 12 digit number'''
sum = 0
for line in lines:
    line = line.removesuffix("\n")
    found = 0
    cur_best_idx = None
    cur = ''
    
    for _ in range(len(line)):
        if cur_best_idx == None:
            sub = line[:-11]
            start_sub_idx = line.index(line[0])
            end_sub_idx = line.index(line[-1])
        else:
            if (-11+found) != 0: 
                sub = line[cur_best_idx+1:-11+found]
            else:
                sub = line[cur_best_idx+1:]
            start_sub_idx = cur_best_idx+1
            end_sub_idx = len(line)-11+found-1

        maxi = max_idx(sub)
        cur += sub[maxi]
        found += 1
        cur_best_idx = start_sub_idx + maxi
        if found == 12:
            best = int(cur)
            break

    best = int(cur)
    #print("best = " + str(best))
    sum += best

print(sum)
