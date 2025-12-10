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

###PART2 -> working on test example, not on puzzle input

import copy

def press_button(cur_voltage, to_push, target):

    ret = copy.deepcopy(cur_voltage)

    for btn in to_push:
        ret[btn] += 1

        if ret[btn] > target[btn]:
            #print("here")
            return None

    return ret

count = 0
for line in lines:
    line = line.removesuffix("\n").split(" ")
    wiring = []
    for item in line:

        if item.startswith('('):
            inter = []
            for i in range(1,len(item)-1):
                if item[i].isdigit():
                    inter.append(int(item[i]))
            wiring.append(inter)

        elif item.startswith('{'):
            item = item[1:-1]
            item = item.split(",")
            voltage_target = []
            for i in range(len(item)):
                if item[i].isdigit():
                    voltage_target.append(int(item[i]))

    len_light = len(voltage_target)
    start = [0] * len_light

    visited = []
    to_visit = [[start, 0]]

    while len(to_visit) != 0:

        inter_voltage, nb_btn_pressed = to_visit.pop(0)

        if inter_voltage == voltage_target:
            count += nb_btn_pressed
            break

        for i in range(len(wiring)):
            res = press_button(inter_voltage, wiring[i], target=voltage_target)
            if res:
                if res not in visited:
                    visited.append(res)
                    to_visit.append([res, nb_btn_pressed+1])

print(count)