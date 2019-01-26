filename="input/day7input.txt"
file=open(filename,"r")
file=file.readlines()

addresses = []
for line in file:
    line = line.strip().replace("[",",[").replace("]","],").split(",")
    addresses.append(line)

supportTPS = 0
for add in addresses:
    itemResult = False
    done = 0
    for item in add:
        if item[0] != '[' and done == 0:
            pos = 0
            while pos < len(item)-3:
                if item[pos] == item[pos+3] and item[pos+1] == item[pos+2] and item[pos] != item[pos+1]:
                    itemResult = True
                pos += 1
        if item[0] == '[' and done == 0:
            pos = 1
            while pos < len(item)-4:
                if item[pos] == item[pos+3] and item[pos+1] == item[pos+2] and item[pos] != item[pos+1]:
                    itemResult = False
                    done = 1
                pos += 1
    if itemResult == True:
        supportTPS += 1

print ("Answer for part one: " + str(supportTPS))

supportSSL = 0
for add in addresses:
    itemResult = False
    options = []
    for item in add:
        if item[0] != '[':
            pos = 0
            while pos < len(item)-2:
                if item[pos] == item[pos+2] and item[pos] != item[pos+1]:
                    options.append( item[pos+1] + item[pos] + item[pos+1] )
                pos += 1
    for item in add:
        if item[0] == '[':
            for opt in options:
                if opt in item:
                    itemResult = True
    if itemResult == True:
        supportSSL += 1

print ("Answer for part two: " + str(supportSSL))
