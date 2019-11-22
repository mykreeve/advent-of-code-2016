import operator

ranges = []

filename = './input/day20input.txt'
file = open(filename, 'r')
file = file.readlines()

for line in file:
    line = line.replace("\n","").replace("-",",").split(',')
    ranges.append((int(line[0]),int(line[1])))

ranges.sort(key = operator.itemgetter(0))

test_number = 0
good = 0

def in_range(val):
    for r in ranges:
        if val >= r[0] and val <= r[1]:
            return r[1]
    return 0

while test_number < 4294967295:
    if in_range(test_number) == 0:
        if good == 0:
            print ("Answer to part one:", test_number)
        good += 1
        test_number += 1
    else:
        test_number = in_range(test_number) + 1

print ("Answer to part two:", good)