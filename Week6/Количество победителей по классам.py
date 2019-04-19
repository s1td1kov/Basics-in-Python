fin = open('input.txt', 'r', encoding='utf8')

newList = []

for line in fin:
    now = line.split()
    newList.append(now)

list9 = []
list10 = []
list11 = []

for i in range(len(newList)):
    if newList[i][2] == '9':
        list9.append(newList[i][3])
    elif newList[i][2] == '10':
        list10.append(newList[i][3])
    else:
        list11.append(newList[i][3])

max9 = max(list9)
max10 = max(list10)
max11 = max(list11)

print(list9.count(max9), list10.count(max10), list11.count(max11))
