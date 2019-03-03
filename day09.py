filename="input/day9input.txt"
file=open(filename,"r")
file=file.readlines()

string = file[0].strip()

string = list(string)

converted = ""

position = 0
while position < len(string):
    if string[position] == '(':
        pass
    elif string[position] in '123456789':
        charas = string[position]
        position += 1
        while string[position] != 'x':
            charas += string[position]
            position += 1
        charas = int(charas)
        position += 1
        reps = string[position]
        position += 1
        while string[position] != ')':
            reps += string[position]
            position += 1
        reps = int(reps)
        position += 1
        snippet = ""
        for rep in range(charas):
            snippet += string[position]
            position += 1
        for rep in range(reps):
            converted += snippet
    else:
        converted += string[position]
    position += 1

print ("Answer for part one: " + str(len(converted)))

def resolveString(string):
    position = 0
    outputLength = 0
    while position < len(string):
        if string[position] == '(':
            pass
        elif string[position] in '123456789':
            charas = string[position]
            position += 1
            while string[position] != 'x':
                charas += string[position]
                position += 1
            charas = int(charas)
            position += 1
            reps = string[position]
            position += 1
            while string[position] != ')':
                reps += string[position]
                position += 1
            reps = int(reps)
            position += 1
            snippet = ""
            for rep in range(charas):
                snippet += string[position]
                position += 1
            if '(' in snippet:
                outputLength += (reps * resolveString(snippet))
            else:
                outputLength += reps * len(snippet)
        else:
            outputLength += 1
        position += 1
    return outputLength
            
outputLength = resolveString(string)

print ("Answer for part two: " + str(outputLength))