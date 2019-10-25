import math

max_elves = 3001330

elves = {}
for a in range(1, max_elves+1):
    elves[a] = 1
print ("Elves set up")

def get_right_elf(n):
    for a in range(n+1,max_elves+1):
        if a in elves:
            return a
    for a in range(1,n):
        if a in elves:
            return a

while len(elves) > 1:
    for a in range(1,max_elves+1):
        if a in elves:
            b = get_right_elf(a)
            elves[a] = elves[a] + elves[b]
            elves.pop(b)
for key in elves:
    print("Answer to part 1:",key)

elves = {}
for a in range(1, max_elves+1):
    elves[a] = 1
print ("Elves set up again")

def get_opposite_elf(n):
    ordered = sorted(elves.keys())
    select = ordered.index(n)
    ret = (math.floor(len(elves)/2)+select)%len(elves)
    return ordered[ret]

while len(elves) > 1:
    for a in range(1,max_elves+1):
        if a in elves:
            b = get_opposite_elf(a)
            elves[a] = elves[a] + elves[b]
            elves.pop(b)
            print (a, len(elves))
for key in elves:
    print("Answer to part 2:",key)