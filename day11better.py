import heapq
import copy
import itertools

queue = []
done = []

filename = './input/day11binput.txt'
file = open(filename, 'r')
file = file.readlines()

condition = {1:['E'], 2:[], 3:[], 4:[]}
setup_floor = 1

for line in file:
    line = line.replace("The ", "").replace(" floor contains a ","").replace(" a ","")
    line = line.replace(" floor contains nothing relevant.","")
    line = line.replace("first","").replace("second","").replace("third","")
    line = line.replace("fourth","").replace(".","").replace("-compatible","")
    line = line.replace(" generator","G").replace(" microchip", "M")
    line = line.replace(", and", ",").replace(" and", ",")
    line = line.replace("polonium","P").replace("thulium","T").replace("ruthenium","R")
    line = line.replace("cobalt","C").replace("promethium","M").replace("\n","")
    line = line.replace("hydrogen","H").replace("dilithium","D").replace("lithium","L")
    line = line.replace("elerium","E")
    line = line.split(",")
    for item in line:
        if item != "":
            condition[setup_floor].append(item)
    setup_floor += 1

print (condition)
done.append(condition)

def find_options(condition, time):
    found = 0
    found_add = 0
    elevator = find_item(condition, 'E')
    options_to_move = []
    working = copy.deepcopy(condition[elevator])
    working.remove('E')
    options_to_move.extend(itertools.permutations(working, 2))
    options_to_move.extend(itertools.permutations(working, 1))
    for option in options_to_move:
        options_to_move_to = []
        if elevator > 1:
            options_to_move_to.append(elevator-1)
        if elevator < 4:
            options_to_move_to.append(elevator+1)
        for option_floor in options_to_move_to:
            new_condition = copy.deepcopy(condition)
            # print ('---before moves---')
            # print (new_condition, option)
            for thing in option:
                # print ('---moving---' + thing + " from " + str(elevator) + " to " + str(option_floor))
                # print (thing, new_condition[elevator])
                new_condition[elevator].remove(thing)
                new_condition[option_floor].append(thing)
            new_condition[option_floor].append('E')
            new_condition[elevator].remove('E')
            if (evaluate_condition(new_condition)):
                found += 1
                nc = {}
                converted = {}
                for a in range(1,5):
                    x = new_condition[a]
                    x.sort()
                    nc[a] = x

                    converted[a] = {'pair':0, 'solog':0, 'solom': 0, 'elevator':0}
                    for l in new_condition[a]:
                        if l != 'E':
                            alt = ''
                            if l[1] == 'G':
                                if find_item(new_condition, l[0]+'M') == a:
                                    converted[a]['pair'] += 1
                                else:
                                    converted[a]['solog'] += 1
                            else:
                                if find_item(new_condition, l[0]+'G') == a:
                                    converted[a]['pair'] += 1
                                else:
                                    converted[a]['solom'] += 1
                        else:
                            converted[a]['elevator'] += 1
                    converted[a]['pair'] = (converted[a]['pair']/2)

                if converted not in done:
                    found_add += 1
                    done.append(converted)
                    heapq.heappush (queue, (time+1, str(nc), nc))

def find_item(condition, missing):
    for floor in condition:
        for item in condition[floor]:
            if item == missing:
                return floor

def evaluate_condition(condition):
    for floor in condition:
        for item in condition[floor]:
            if item != 'E' and item[1] == 'M':
                if find_item(condition,item[0]+'G') != floor:
                    # print("Potential problem: " + item[0] + " microchip is alone on " + str(floor))
                    for other_item in condition[floor]:
                        if other_item != 'E' and other_item[0] != item[0] and other_item[1] == 'G':
                            # print ("Bigger problem: It is with " + other_item[0] + " generator")
                            return False
    return True


time = 0
curtime = 0

find_options(condition, time)

while (len(queue) > 0):
    next_option = heapq.heappop(queue)
    condition = next_option[2]
    time = next_option[0]
    if time != curtime:
        curtime = time
        print("time:", time, ", queue:", str(len(queue)), ", done:", str(len(done)))
    if condition[1] == [] and condition[2] == [] and condition[3] == []:
        break;
    find_options(condition, time)

print ("final time: ", time)