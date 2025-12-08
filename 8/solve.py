import math

input = open("input.txt", 'r')
lines = input.readlines()


#================FUNCTIONS================#

def shortest_connection(l):
    best = float('inf')
    best_i = None
    best_j = None
    for i in l:
        for j in l[l.index(i):]:
            if l.index(i) != l.index(j):
                short = math.sqrt(pow(i[0]-j[0], 2)+pow(i[1]-j[1], 2)+pow(i[2]-j[2], 2))
                if short < best:
                    best = short
                    best_i = i
                    best_j = j
    print(best)
    return (best_i, best_j)

def all_shortest_connection(l):
    d = {}
    for i in l:
        for j in l[l.index(i):]:
            if l.index(i) != l.index(j):
                short = math.sqrt(pow(i[0]-j[0], 2)+pow(i[1]-j[1], 2)+pow(i[2]-j[2], 2))
                d[(i,j)] = short

    sorted_dict = dict(sorted(d.items(), key=lambda item: item[1])) 

    return sorted_dict

#================FUNCTIONS================#

###PART1

l_coord = []
for line in lines:
    coord = line.removesuffix("\n").split(',')
    coord = [int(x) for x in coord]
    l_coord.append(tuple(coord))


res = all_shortest_connection(l_coord)
first_1000 = []

i=0
for k,v in res.items():
    if i < 1000:
        i += 1
        first_1000.append(k)
    else:
        break

l_res = []
visited = []
for i in first_1000:
    if i not in visited:
        cur_circuit = [i[0], i[1]]
        to_visit = [i[0], i[1]]
        visited.append(i)
        while (len(to_visit) != 0):
            cur = to_visit.pop()
            for j in first_1000:
                if i != j and j not in visited:
                    if j[0] == cur:
                        to_visit.append(j[1])
                        if j[1] not in cur_circuit:
                            cur_circuit.append(j[1])
                        visited.append(j)
                    elif j[1] == cur:
                        to_visit.append(j[0])
                        if j[0] not in cur_circuit:
                            cur_circuit.append(j[0])
                        visited.append(j)
        l_res.append(len(cur_circuit))


l_res = sorted(l_res, reverse=True)

mul = math.prod(l_res[:3])
print(mul)


    
