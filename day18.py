rows = []
total_rows=40
max_rows=400000

filename = './input/day18input.txt'
file = open(filename, 'r')
file = file.readlines()

for line in file:
    line = line.replace("\n","")
    rows.append(line)

while len(rows) < max_rows:
    next_row = len(rows)
    row = ""
    for a in range(len(rows[next_row-1])):
        test_string = ""
        if (a-1) < 0:
            test_string += "."
        else:
            test_string += rows[next_row-1][a-1]
        test_string += rows[next_row-1][a]
        if (a+1) > len(rows[next_row-1])-1:
            test_string += "."
        else:
            test_string += rows[next_row-1][a+1]
        if test_string in ['^^.','.^^','^..','..^']:
            row += "^"
        else:
            row += "."
    rows.append(row)

safe_count = 0
for r in range(total_rows):
    for c in rows[r]:
        if c == '.':
            safe_count += 1
print ("Answer to part 1:", safe_count)

safe_count = 0
for r in rows:
    for c in r:
        if c == '.':
            safe_count += 1
print ("Answer to part 2:", safe_count)