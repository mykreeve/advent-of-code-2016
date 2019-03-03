import re

filename = './input/day10input.txt'
file = open(filename, 'r')
file = file.readlines()

bots = {}
rules = {}
outputs = {}

for line in file:
    if re.match('.*gives.*', line):
        line = line.replace('bot ','bot,').replace(' gives low to ',',').replace('bot ', 'bot,').replace('output ','output,').replace(' and high to ',',').strip().split(',')
        rules[int(line[1])] = [(line[2], int(line[3])), (line[4], int(line[5]))]
    else:
        line = line.replace('value ','').replace(' goes to bot ',',').strip().split(',')
        if int(line[1]) in bots:
            bots[int(line[1])].append(int(line[0]))
        else:
            bots[int(line[1])] = [int(line[0])]

def doesBotHaveTwo(bots):
    for b in bots:
        if len(bots[b]) == 2:
            return True
    return False

def giveValue(value,rule):
    # print ('Value ' + str(value) + ' is given to ' + rule[0] + ' ' + str(rule[1]))
    if rule[0] == 'bot':
        if rule[1] in bots:
            bots[rule[1]].append(value)
        else:
            bots[rule[1]] = [value]
    elif rule[0] == 'output':
        if rule[1] in outputs:
            outputs[rule[1]].append(value)
        else:
            outputs[rule[1]] = [value]

while doesBotHaveTwo(bots):
    for b in bots:
        if len(bots[b]) == 2:
            if bots[b] == [61,17] or bots[b] == [17,61]:
                print ("Answer to part one: " + str(b))
            # print ("Bot " + str(b) + " has two values; " + str(bots[b]))
            low = (min(bots[b]))
            high = (max(bots[b]))
            bots[b] = []
            giveValue(low, rules[b][0])
            giveValue(high, rules[b][1])
            break
print ("Answer to part two: " + str(outputs[0][0] * outputs[1][0] * outputs[2][0]))