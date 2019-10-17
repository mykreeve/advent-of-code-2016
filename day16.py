import copy

input_value = "10001001100000001"
required_length = 272
part_2_required_length = 35651584
string = copy.deepcopy(input_value)

def increase_dragon(val):
    reversed_string = val[::-1]
    output_value = ""
    for a in range(len(reversed_string)):
        if reversed_string[a]=="1":
            output_value += "0"
        elif reversed_string[a]=="0":
            output_value += "1"
    return val+"0"+output_value

def generate_checksum(strng):
    check = ""
    for a in range(0, len(strng)-1, 2):
        if strng[a] == strng[a+1]:
            check += "1"
        else:
            check += "0"
    return check

while len(string) < required_length:
    string = increase_dragon(string)

string = string[:required_length]

checksum = generate_checksum(string)

while (len(checksum))%2 == 0:
    checksum = generate_checksum(checksum)

print ("Answer to part 1:", checksum)


string = copy.deepcopy(input_value)

while len(string) < part_2_required_length:
    string = increase_dragon(string)

string = string[:part_2_required_length]

checksum = generate_checksum(string)

while (len(checksum))%2 == 0:
    checksum = generate_checksum(checksum)

print ("Answer to part 2:", checksum)