import heapq

favourite_number = 1352
target=(31,39)
queue = []
visited = []
grid = {}
distance = {(1,1): 0}

def find_max_2_factor(x):
    temp = 1
    while x > temp:
        temp = temp*2
    return int(temp/2)

for x in range(100):
    for y in range(100):
        value = (x*x)+(3*x)+(2*x*y)+y+(y*y)+favourite_number
        factor = find_max_2_factor(value)
        count = 0
        while factor >= 0.9:
            if value >= factor:
                count += 1
                value = value - factor
            factor = factor/2
        if count%2 == 0:
            grid[(x,y)]="."
        else:
            grid[(x,y)]="#"

position = (1,1)
time = 0

def add_to_queue(position, time):
    position_options = [
        (position[0]+1,position[1]),
        (position[0]-1,position[1]),
        (position[0],position[1]+1),
        (position[0],position[1]-1)
    ]
    for pos in position_options:
        if pos in grid and pos not in visited and grid[pos] == '.':
            heapq.heappush(queue, (time+1, pos))
            distance[pos] = time+1


while position != target:
    visited.append(position)
    add_to_queue(position, time)
    time,position = heapq.heappop(queue)

print ("Part one answer:", time)

part2count = 0
for x in range(100):
    for y in range(100):
        if (x,y) in distance and distance[(x,y)] <= 50:
            part2count += 1
print ("Part two answer:", part2count)