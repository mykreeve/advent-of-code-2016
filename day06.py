filename="input/day6input.txt"
file=open(filename,"r")
file=file.readlines()

messages = []
for line in file:
    messages.append(line.strip())

trans=[]
realTrans=[]
for a in range(len(messages[0])):
    freq={}
    for m in messages:
        if m[a] not in freq:
            freq[m[a]]=1
        else:
            freq[m[a]]+=1
    most = 0
    least = 999
    for k,v in freq.items():
        if v>most:
            most = v
            best = k
        if v<least:
            least = v
            worst = k
    trans.append(best)
    realTrans.append(worst)

print ("Answer to part one: " + "".join(trans))
print ("Answer to part two: " + "".join(realTrans))