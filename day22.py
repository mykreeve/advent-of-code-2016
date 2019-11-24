nodes = {}

filename = './input/day22input.txt'
file = open(filename, 'r')
file = file.readlines()

maxx = 0
maxy = 0

for line in file:
    line = line.replace('  ',' ').replace('  ',' ').replace('  ',' ')
    line = line.replace('/dev/grid/node-x','')
    line = line.replace('-y',',')
    line = line.replace(' ',',')
    line = line.replace('T','')
    line = line.replace('%','')
    line = line.replace('\n','')
    line = line.split(',')
    if line[0] not in ('root@ebhq-gridcenter#', 'Filesystem'):
        if int(line[0]) > maxx:
            maxx = int(line[0])
        if int(line[1]) > maxy:
            maxy = int(line[1])
        nodes[(int(line[0]), int(line[1]))] = {'size':int(line[2]), 'used':int(line[3]), 'avail':int(line[4]), 'use':int(line[5])}

viables = []

for x in range(maxx+1):
    for y in range(maxy+1):
        for a in range(maxx+1):
            for b in range(maxy+1):
                if nodes[x,y]['used'] > 0 and (x,y) != (a,b):
                    if nodes[x,y]['used'] <= nodes[a,b]['avail']:
                        print(len(viables)+1, nodes[x,y], nodes[a,b])
                        viables.append([(x,y),(a,b)])
print("Answer for part one:", len(viables))


for y in range(maxy+1):
    for x in range(maxx+1):
        if x == maxx and y == 0:
            print('G', end='')
        elif nodes[x,y]['used'] == 0:
            print('_',end='')
        elif nodes[x,y]['size'] >= 100:
            print('#', end='')
        else:
            print('.', end='')
    print('\n', end='')

# I didn't do any code to solve part two
# I just counted how many moves it would take
# to move from the '_' to the 'G' position
# and then added (31*5) to account for each 
# loop to move 'G' to the top left.