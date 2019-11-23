instructions = []
password = 'abcdefgh'
scrambled = 'fbgdceah'

filename = './input/day21input.txt'
file = open(filename, 'r')
file = file.readlines()

for line in file:
    line = line.replace("\n","")
    line = line.replace("swap letter ","swapl,")
    line = line.replace(" with letter ",",")
    line = line.replace("swap position ","swapp,")
    line = line.replace(" with position ",",")
    line = line.replace("move position ","movep,")
    line = line.replace(" to position ",",")
    line = line.replace("rotate based on position of letter ","rotl,")
    line = line.replace("rotate right ","rotp,")
    line = line.replace("rotate left ","rotp,-")
    line = line.replace(" steps","")
    line = line.replace(" step","")
    line = line.replace("reverse positions ","revp,")
    line = line.replace(" through ",",")
        
    line = line.split(',')
    if line[0] in ('movep', 'revp', 'swapp'):
        instructions.append([line[0], int(line[1]), int(line[2])])
    elif line[0] == 'rotp':
        instructions.append([line[0], int(line[1])])
    else:
        instructions.append(line)

for i in instructions:
    if i[0] == 'swapl':
        pwd = list(password)
        pos1 = password.find(i[1])
        pos2 = password.find(i[2])
        pwd[pos1] = i[2]
        pwd[pos2] = i[1]
        password = ''.join(pwd)
    if i[0] == 'swapp':
        pwd = list(password)
        val1 = pwd[i[1]]
        val2 = pwd[i[2]]
        pwd[i[1]] = val2
        pwd[i[2]] = val1
        password = ''.join(pwd)
    if i[0] == 'rotp':
        pwd = list(password)
        pos = i[1]
        if pos < 0:
            pos = len(pwd) + pos
        pwd = pwd[-pos:] + pwd[:-pos]
        password = ''.join(pwd)
    if i[0] == 'rotl':
        pwd = list(password)
        pos = password.find(i[1])
        if pos >= 4:
            pos += 2
        else:
            pos += 1
        if pos > len(password):
            pos = pos - len(password)
        pwd = pwd[-pos:] + pwd[:-pos]
        password = ''.join(pwd)
    if i[0] == 'revp':
        pwd = list(password)
        revbit = pwd[i[1]:i[2]+1]
        for a in range(i[1], i[2]+1):
            pwd[a] = revbit.pop()
        password = ''.join(pwd)
    if i[0] == 'movep':
        pwd = list(password)
        mov = pwd.pop(i[1])
        pwd.insert(i[2], mov)
        password = ''.join(pwd)

print ("Answer to part one:", password)

password = scrambled
instructions.reverse()
for i in instructions:
    if i[0] == 'swapl':
        pwd = list(password)
        pos1 = password.find(i[1])
        pos2 = password.find(i[2])
        pwd[pos1] = i[2]
        pwd[pos2] = i[1]
        password = ''.join(pwd)
    if i[0] == 'swapp':
        pwd = list(password)
        val1 = pwd[i[1]]
        val2 = pwd[i[2]]
        pwd[i[1]] = val2
        pwd[i[2]] = val1
        password = ''.join(pwd)
    if i[0] == 'rotp':
        pwd = list(password)
        pos = i[1]
        if pos < 0:
            pos = len(pwd) + pos
        pwd = pwd[pos:] + pwd[:pos]
        password = ''.join(pwd)
    if i[0] == 'rotl':
        pwd = list(password)
        for a in range(len(password)):
            pwd = pwd[1:] + pwd[:1]
            pos = ''.join(pwd).find(i[1])
            if pos >= 4:
                pos += 2
            else:
                pos += 1
            if pos > len(password):
                pos = pos - len(password)
            if a+1 == pos:
                break
        password = ''.join(pwd)
    if i[0] == 'revp':
        pwd = list(password)
        revbit = pwd[i[1]:i[2]+1]
        for a in range(i[1], i[2]+1):
            pwd[a] = revbit.pop()
        password = ''.join(pwd)
    if i[0] == 'movep':
        pwd = list(password)
        mov = pwd.pop(i[2])
        pwd.insert(i[1], mov)
        password = ''.join(pwd)
print ("Answer to part two:", password)