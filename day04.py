import re

filename="input/day4input.txt"
file=open(filename,"r")
file=file.readlines()

keys = []
for line in file:
    line = line.strip().replace("[","").replace("]","")
    line = re.split('([0-9]*)',line)
    keys.append(line)

checked=[]
score=0
for k in keys:
    freq={}
    for c in k[0]:
        if c not in freq:
            freq[c] = 1
        else:
            freq[c] += 1
    checksum = []
    n = len(k[0])
    while n>0:
        for a in list('abcdefghijklmnopqrstuvwxyz'):
            if a in freq and freq[a]==n:
                checksum.append(a)
        n -= 1
    test = "".join(checksum)[:5]
    if test == k[2]:
        score += int(k[1])
        checked.append([k[0][:-1],int(k[1])])

print ("Answer for part one: " + str(score))

alpha = list('abcdefghijklmnopqrstuvwxyz')

for k in checked:
    translate = []
    forward = k[1]%26
    for c in k[0]:
        if c=='-':
            translate.append('-')
        else:
            for n,a in enumerate(alpha):
                if a==c:
                    value = n
            value += forward
            if value > 25:
                value -= 26
            translate.append(alpha[value])
    if "north" in "".join(translate):
        print("Answer for part two: " + str(k[1]))