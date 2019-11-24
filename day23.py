program = []

filename = './input/day23input.txt'
file = open(filename, 'r')
file = file.readlines()

for line in file:
    line = line.replace("\n","").split(" ")
    program.append(line)

letters = ['a','b','c','d']

def tgl_command(valToAmend, pos, program):
    val = 0
    if valToAmend in letters:
        if valToAmend == 'a':
            val = a
        elif valToAmend == 'b':
            val = b
        elif valToAmend == 'c':
            val = c
        elif valToAmend == 'd':
            val = d
    else:
        val = int(valToAmend)
    print(pos, pos+val)
    if pos+val <= len(program)-1:
        print("toggling command:", program[pos+val])
        new_com = []
        if len(program[pos+val]) == 2:
            if program[pos+val][0] == 'inc':
                new_com.append('dec')
            else:
                new_com.append('inc')
            new_com.append(program[pos+val][1])
        elif len(program[pos+val]) == 3:
            if program[pos+val][0] == 'jnz':
                new_com.append('cpy')
            else:
                new_com.append('jnz')
            new_com.append(program[pos+val][1])
            new_com.append(program[pos+val][2])
        program[pos+val] = new_com
    return pos,program

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
        if second in letters:
            if second == 'a':
                mov = a
            elif second == 'b':
                mov = b
            elif second == 'c':
                mov = c
            elif second == 'd':
                mov = d
        else:
            mov = int(second)
        pos = pos + mov
    else:
        pos += 1
    return pos

position = 0
a = 7
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
    elif program[position][0] == 'tgl':
        position, program = tgl_command(program[position][1], position, program)
        position += 1
print('Answer for part one:', a)

program = []

filename = './input/day23input.txt'
file = open(filename, 'r')
file = file.readlines()

for line in file:
    line = line.replace("\n","").split(" ")
    program.append(line)

position = 0
a = 12
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
    elif program[position][0] == 'tgl':
        position, program = tgl_command(program[position][1], position, program)
        position += 1
print('Answer for part two:', a)
