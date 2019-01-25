import hashlib

input="abbhdwsy"
value=1

output = []
while len(output) < 8:
    test=(input+str(value)).encode('utf-8')
    test=hashlib.md5(test).hexdigest()
    if test[:5]=='00000':
        output.append(test[5])
    value += 1

print ("Answer to part one: " + "".join(output))

def output_incomplete():
    for a in output:
        if a == '-':
            return True
    return False

value=1
output = ['-','-','-','-','-','-','-','-']
while output_incomplete():
    test=(input+str(value)).encode('utf-8')
    test=hashlib.md5(test).hexdigest()
    if test[:5]=='00000':
        if test[5] in '01234567':
            if output[int(test[5])]=='-':
                output[int(test[5])] = test[6]
        print ("".join(output))
    value += 1

print ("Answer to part two: " + "".join(output))