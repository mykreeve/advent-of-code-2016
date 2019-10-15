program = []

filename = './input/day12input.txt'
file = open(filename, 'r')
file = file.readlines()

for line in file:
    line = line.replace("\n","").split(" ")
    program.append(line)

position = 0
a = 0
b = 0
c = 0
d = 0
letters = ['a','b','c','d']

def cpy_command(fromVal, toVal,a,b,c,d):
    val = 0
    if fromVal in letters:
        if fromVal == 'a':
            val = a
        elif fromVal == 'b':
            val = b
        elif fromVal == 'c':
            val = c
        elif fromVal == 'd':
            val = d
    else:
        val = int(fromVal)
    if toVal == 'a':
        a = val
    elif toVal == 'b':
        b = val
    elif toVal == 'c':
        c = val
    elif toVal == 'd':
        d = val
    return a,b,c,d

def alter_value(toVal, val,a,b,c,d):
    if toVal == 'a':
        a += val
    elif toVal == 'b':
        b += val
    elif toVal == 'c':
        c += val
    elif toVal == 'd':
        d += val
    return a,b,c,d

def jmp_command(first, second, pos):
    val = 0
    if first in letters:
        if first == 'a':
            val = a
        elif first == 'b':
            val = b
        elif first == 'c':
            val = c
        elif first == 'd':
            val = d
    else:
        val = int(first)
    if val != 0:
        pos = pos + int(second)
    else:
        pos += 1
    return pos

position = 0
a = 0
b = 0
c = 0
d = 0
while position < len(program):
    if program[position][0] == 'cpy':
        a,b,c,d = cpy_command(program[position][1], program[position][2],a,b,c,d)
        position += 1
    elif program[position][0] == 'inc':
        a,b,c,d = alter_value(program[position][1], 1,a,b,c,d)
        position += 1
    elif program[position][0] == 'dec':
        a,b,c,d = alter_value(program[position][1], -1,a,b,c,d)
        position += 1
    elif program[position][0] == 'jnz':
        position = jmp_command(program[position][1], program[position][2], position)
print('Values --', a, b, c, d)

position = 0
a = 0
b = 0
c = 1
d = 0
while position < len(program):
    if program[position][0] == 'cpy':
        a,b,c,d = cpy_command(program[position][1], program[position][2],a,b,c,d)
        position += 1
    elif program[position][0] == 'inc':
        a,b,c,d = alter_value(program[position][1], 1,a,b,c,d)
        position += 1
    elif program[position][0] == 'dec':
        a,b,c,d = alter_value(program[position][1], -1,a,b,c,d)
        position += 1
    elif program[position][0] == 'jnz':
        position = jmp_command(program[position][1], program[position][2], position)
print('Values --', a, b, c, d)