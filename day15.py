discs = []

filename = './input/day15input.txt'
file = open(filename, 'r')
file = file.readlines()

for line in file:
    line = line.replace("\n","").replace("Disc #","").replace(" has ",",")
    line = line.replace(" positions; at time=0, it is at position ",",").replace(".","")
    line = line.split(",")
    discs.append((int(line[0]), int(line[1]), int(line[2])))

time = 0
while True:
    discs_passed = 0
    for disc in discs:
        time_to_disc = time+disc[0]
        position_of_disc = (disc[2]+time_to_disc)%disc[1]
        if position_of_disc != 0:
            break
        else:
            discs_passed += 1
    if discs_passed == len(discs):
        print ("Answer to part 1:", time)
        break
    time += 1

time = 0
discs.append((7,11,0))
while True:
    discs_passed = 0
    for disc in discs:
        time_to_disc = time+disc[0]
        position_of_disc = (disc[2]+time_to_disc)%disc[1]
        if position_of_disc != 0:
            break
        else:
            discs_passed += 1
    if discs_passed == len(discs):
        print ("Answer to part 2:", time)
        break
    time += 1