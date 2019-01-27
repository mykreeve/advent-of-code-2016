filename="input/day8input.txt"
file=open(filename,"r")
file=file.readlines()

instructions = []
for line in file:
    line = line.strip().replace(" row y=", ",row,").replace(" column x=", ",column,").replace(' by ', ',').replace(" ", ",").replace("x",",").split(",")
    instructions.append(line)

grid = {}
for x in range(50):
    for y in range(6):
        grid[x,y]='.'

def print_grid():
    print("")
    for y in range(6):
        for x in range(50):
            print(grid[x,y], end="")
        print("")
    print("")

def count_grid():
    ret=0
    for y in range(6):
        for x in range(50):
            if grid[x,y]=='#':
                ret += 1
    return ret


for ins in instructions:
    if ins[0]=='rect':
        for x in range(int(ins[1])):
            for y in range(int(ins[2])):
                grid[x,y]='#'
    if ins[0]=='rotate':
        if ins[1]=='row':
            row = []
            rowno = int(ins[2])
            posno = int(ins[3])
            for x in range(50):
                row.append(grid[x,rowno])
            for x in range(50):
                grid[x,rowno]=row[(x-posno)%50]
        elif ins[1]=='column':
            column = []
            colno = int(ins[2])
            posno = int(ins[3])
            for y in range(6):
                column.append(grid[colno,y])
            for y in range(6):
                grid[colno,y]=column[(y-posno)%6]

print("Answer for part one: " + str(count_grid()))
print("")
print ("Answer for part two: ")
print_grid()