import copy

filename="input/day1input.txt"
file=open(filename,"r")
file=file.readlines()
directions=file[0].strip().replace(" ","").split(",")

cardinals = [(0,-1), (1,0), (0,1), (-1,0)]

facing = 0
loc = (0,0)
doubled = [0,0]
visited=[]
done = 0
for d in directions:
    if d[:1]=='L':
        facing -= 1
        if facing == -1:
            facing = 3
    if d[:1]=='R':
        facing += 1
        if facing == 4:
            facing = 0
    distance = int(d[1:])
    for m in range(distance):
        loc = (loc[0] + cardinals[facing][0], loc[1] + cardinals[facing][1])
        if loc in visited and done == 0:
            doubled = loc
            done = 1
        else:
            visited.append(loc)

distance=abs(loc[0])+abs(loc[1])
print ("Answer for part one: " + str(distance))

distance=abs(doubled[0])+abs(doubled[1])
print ("Answer for part two: " + str(distance))
