input = open("input.txt", 'r')
lines = input.readlines()

###PART1

def str_xor(s1, s2):
    assert(len(s1) == len(s2))
    res = ''
    for i in range(len(s1)):
        res += str(int(s1[i]) ^ int(s2[i]))
    return res

count = 0
for line in lines:
    line = line.removesuffix("\n").split(" ")
    wiring = []
    bin_wiring = []
    for item in line:
        if item.startswith('['):
            schematic = item
            bin_str_target = ''
            for i in range(1, len(item)-1):
                if item[i] == "#":
                    bin_str_target += '1'
                elif item[i] == '.':
                    bin_str_target += '0'
        elif item.startswith('('):
            start = list('0' * len(bin_str_target))
            inter = []
            for i in range(1,len(item)-1):
                if item[i].isdigit():
                    n = int(item[i])
                    start[n] = '1'
            binary = ''.join(start)
            bin_wiring.append(binary)

    
    visited_state = []
    to_visit = [[x,1] for x in bin_wiring]

    while len(to_visit) != 0:
        state, nb_pushed = to_visit.pop(0)

        if state == bin_str_target:
            count += nb_pushed
            break

        for i, buttons in enumerate(bin_wiring):
            res = str_xor(state, buttons)
            if res not in visited_state:
                visited_state.append(res)
                to_visit.append([res, nb_pushed+1])

print(count)


        
