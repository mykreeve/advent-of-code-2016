filename="input/day3input.txt"
file=open(filename,"r")
file=file.readlines()

triangles = []
for line in file:
    [a,b,c] = line.strip().replace("  ", " ").replace(" ",",").replace(",,",",").split(",")
    [a,b,c] = [int(a), int(b), int(c)]
    line = [a,b,c]
    line.sort()
    triangles.append(line)

possible = 0
for t in triangles:
    if (t[0] + t[1]) > t[2]:
        possible += 1

print ("Answer for part one: " + str(possible))

triangles = []
for line in file:
    [a,b,c] = line.strip().replace("  ", " ").replace(" ",",").replace(",,",",").split(",")
    [a,b,c] = [int(a), int(b), int(c)]
    line = [a,b,c]
    triangles.append(line)

new_triangles=[]
tpos=0
while tpos < len(triangles):
    new_triangles.append([ triangles[tpos][0], triangles[tpos+1][0], triangles[tpos+2][0] ])
    new_triangles.append([ triangles[tpos][1], triangles[tpos+1][1], triangles[tpos+2][1] ])
    new_triangles.append([ triangles[tpos][2], triangles[tpos+1][2], triangles[tpos+2][2] ])
    tpos += 3

possible = 0
for t in new_triangles:
    t.sort()
    if (t[0] + t[1]) > t[2]:
        possible += 1

print ("Answer for part two: " + str(possible))