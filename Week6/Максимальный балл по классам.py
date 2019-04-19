fin = open('input.txt', 'r', encoding='utf8')
newList = []
max9 = []
max10 = []
max11 = []

for line in fin:
    lineList = line.split()
    newList.append(lineList)

for now in newList:
    if now[2] == '9':
        max9.append(now[3])
    elif now[2] == '10':
        max10.append(now[3])
    else:
        max11.append(now[3])

print(max(max9), max(max10), max(max11))
