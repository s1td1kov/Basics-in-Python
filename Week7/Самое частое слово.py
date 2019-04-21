myFile = open('input.txt')
firstDict = {}
for line in myFile:
    lineList = line.split()
    for i in range(len(lineList)):
        firstDict[lineList[i]] = firstDict.get(lineList[i], 0) + 1

newList = []
for word in firstDict:
    newList.append(firstDict[word])

maximum = max(newList)
maxList = []
for word in firstDict:
    if firstDict[word] == maximum:
        maxList.append(word)
maxList.sort()
print(maxList[0])
