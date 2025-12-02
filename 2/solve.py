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

#===================END FUNCTIONS=======================

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

print(sum)



    