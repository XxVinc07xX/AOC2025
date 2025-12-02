input = open("input.txt", 'r')
lines = input.read()

#===================FUNCTIONS===========================

'''
check if first half of nb == second half
e.g. 3939 => return true
e.g. 111 => return false
e.g. 5469 => return false
'''
def check_half(nb):
    string_nb = str(nb)
    if len(string_nb)%2 != 0:
        return False
    first, second = string_nb[:len(string_nb)//2], string_nb[len(string_nb)//2:]
    if first == second:
        return True
    return False

#print(check_half(5251))
    
def split_equal(str_nb, n):
    l = []
    jump = len(str_nb)//n
    #print(jump)
    start = 0
    for _ in range(0,n):
        l.append(str_nb[start:start+jump])
        start += jump
    return l 

def check_l(l):
    res = len(set(l)) == 1
    return res

def check_all(nb):
    l = []
    string_nb = str(nb)
    for i in range(2, len(string_nb)+1):
        if len(string_nb)%i != 0:
            continue
        l = split_equal(string_nb, i)
        if check_l(l):
            print(l)
            return True
        #return False
    
#print(check_all(12))

#print(split_equal('11111111', 7))
print(check_l(split_equal('565656', 3)))


#===================END FUNCTIONS=======================

#PART1

l = lines.split(",")
ranges = []
sum = 0

for item in l:
    item = item.removesuffix("\n").removeprefix("\n")
    item = item.split('-')
    tpl = (int(item[0]), int(item[1]))
    ranges.append(tpl)

#print(ranges)
for r in ranges:
    for i in range(r[0], r[1]+1):
        val = check_half(i)
        if val:
            sum += i

#print(sum)


#PART2
sum2 = 0
for r in ranges:
    for i in range(r[0], r[1]+1):
        val = check_all(i)
        if val:
            #print(i)
            sum2 += i

print(sum2)





    