import hashlib

input_value = "ihaygndm"
# input_value = "abc"
found = []
search_position = 0
generated_hashes = {}
generated_stretched_hashes = {}

def contains_multiple(text, number):
    pos = 0
    while pos < (len(text)-number+1):
        test_string = text[pos]
        count = 0
        for a in range(1,number):
            if text[pos+a] == test_string:
                count += 1
        if count == number-1:
            return test_string;
        pos += 1;
    return "";

def contains_multi_same(text, number, search_string):
    pos = 0
    while pos < (len(text)-number+1):
        if text[pos] == search_string:
            count = 0
            for a in range(1,number):
                if text[pos+a] == search_string:
                    count += 1
            if count == number-1:
                return True
        pos += 1
    return False

def get_hash(value):
    if value not in generated_hashes:
        text_value = (input_value + str(value))
        seed = text_value.encode('utf-8')
        hash_value = hashlib.md5(seed).hexdigest()
        generated_hashes[value] = hash_value
        return hash_value
    else:
        return (generated_hashes[value])

def get_stretched_hash(value):
    if value not in generated_stretched_hashes:
        text_value = (input_value + str(value))
        seed = text_value.encode('utf-8')
        hash_value = hashlib.md5(seed).hexdigest()
        for a in range(2016):
            hash_value = hash_value.encode('utf-8')
            hash_value = hashlib.md5(hash_value).hexdigest()
        generated_stretched_hashes[value] = hash_value
        return hash_value
    else:
        return (generated_stretched_hashes[value])

while len(found) < 64:
    hash_value = get_hash(search_position)
    found_multi = contains_multiple(hash_value, 3)
    if found_multi != "":
        # print ("Hash for " + str(search_position) + " contains three " + found_multi)
        for a in range(1000):
            hash_value2 = get_hash(search_position+a+1)
            if contains_multi_same(hash_value2, 5, found_multi):
                found.append(search_position)
                # print ("Hash for " + str(search_position) + " is a valid key. It is key number: " + str(len(found)))
                # print (hash_value + " has three consecutive " + found_multi + " (seed was " + str(search_position)+ ")")
                # print (hash_value2 + " has five consecutive " + found_multi + " (seed was " + str(search_position+a+1)+ ")")
                break
    search_position += 1
print ("Answer for part 1: " + str(search_position-1))
print ("---")

found = []
search_position = 0

while len(found) < 64:
    hash_value = get_stretched_hash(search_position)
    found_multi = contains_multiple(hash_value, 3)
    if found_multi != "":
        # print ("Stretched Hash for " + str(search_position) + " contains three " + found_multi)
        for a in range(1000):
            hash_value2 = get_stretched_hash(search_position+a+1)
            if contains_multi_same(hash_value2, 5, found_multi):
                found.append(search_position)
                # print ("Stretched Hash for " + str(search_position) + " is a valid key. It is key number: " + str(len(found)))
                # print (hash_value + " has three consecutive " + found_multi + " (seed was " + str(search_position)+ ")")
                # print (hash_value2 + " has five consecutive " + found_multi + " (seed was " + str(search_position+a+1)+ ")")
                break
    search_position += 1
print ("Answer for part 2: " + str(search_position-1))