import heapq
import hashlib

puzzle_input = "gdjjyniy"
location = (0,0)
time = 0
queue = []
heapq.heappush(queue, (time, location, puzzle_input))

def get_hash(value):
    seed = value.encode('utf-8')
    return hashlib.md5(seed).hexdigest()

def get_door_statuses(value):
    output = []
    hash_value = get_hash(value)[:4]
    for h in hash_value:
        if h in ['b','c','d','e','f']:
            output.append('open')
        else:
            output.append('closed')
    return output

shortest_path = ""
longest_path = 0

while len(queue) > 0:
    consider = heapq.heappop(queue)
    # print (consider[0], consider[1], consider[2])
    if consider[1] == (3,3):
        if shortest_path == "":
            shortest_path = consider[2][len(puzzle_input):]
            print ("Answer to part 1:", consider[2][len(puzzle_input):])
        longest_path = consider[0]
    doors = get_door_statuses(consider[2])
    if consider[1] != (3,3):
        if doors[0] == 'open' and consider[1][1] > 0:
            heapq.heappush(queue, (consider[0]+1, (consider[1][0], consider[1][1]-1), consider[2]+"U"))
        if doors[1] == 'open' and consider[1][1] < 3:
            heapq.heappush(queue, (consider[0]+1, (consider[1][0], consider[1][1]+1), consider[2]+"D"))
        if doors[2] == 'open' and consider[1][0] > 0:
            heapq.heappush(queue, (consider[0]+1, (consider[1][0]-1, consider[1][1]), consider[2]+"L"))
        if doors[3] == 'open' and consider[1][0] < 3:
            heapq.heappush(queue, (consider[0]+1, (consider[1][0]+1, consider[1][1]), consider[2]+"R"))
print ("Answer for part 2:", longest_path)