filename="input/day2input.txt"
file=open(filename,"r")
file=file.readlines()

instructions = []
for line in file:
    line = line.strip()
    instructions.append(list(line))

directions={'L':(-1,0), 'U':(0,-1), 'D':(0,1), 'R':(1,0)}

translate={ (1,1):1, (1,2):4, (1,3):7, (2,1):2, (2,2):5, (2,3):8, (3,1):3, (3,2):6, (3,3):9 }

print ("Answer for part one: ", end='')
for i in instructions:
    position = (2,2)
    for pos in i:
        h = position[0]+directions[pos][0]
        if h < 1:
            h = 1
        elif h > 3:
            h = 3
        v = position[1]+directions[pos][1]
        if v < 1:
            v = 1
        elif v > 3:
            v = 3
        position = (h,v)
    print(translate[position], end='')
print("")

new_translate={ (3,1):'1', (2,2):'2', (3,2):'3', (4,2):'4', (1,3):'5', (2,3):'6', (3,3):'7', (4,3):'8', (5,3):'9', (2,4):'A', (3,4):'B', (4,4):'C', (3,5):'D'}

print ("Answer for part two: ", end='')
for i in instructions:
    position = (1,3)
    for pos in i:
        h = position[0]+directions[pos][0]
        v = position[1]+directions[pos][1]
        if (h,v) not in new_translate:
            pass
        else:
            position = (h,v)
    print(new_translate[position], end='')
print("")