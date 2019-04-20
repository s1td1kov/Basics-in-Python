myFile = open('input.txt', 'r', encoding='utf8')
resultFile = open('output.txt', 'w', encoding='utf8')
k = int(myFile.readline())
myList = []
for line in myFile:
    newLine = line.split()
    if int(newLine[-1]) >= 40 and int(newLine[-2]) >= 40 \
            and int(newLine[-3]) >= 40:
        myList.append(newLine)
myFile.close()
myList.sort(key=lambda a: int(a[-1]) + int(a[-2]) + int(a[-3]))
myList.reverse()
konk = []
for i in myList:
    sum = int(i[-1]) + int(i[-2]) + int(i[-3])
    konk.append(sum)
n = len(konk)


def konkurs(n, k, konk):
    if n <= k:
        return 0
    elif konk[0] == konk[k]:
        return 1
    for i in range(k, 0, -1):
        if konk[i - 1] > konk[i]:
            return konk[i - 1]


print(konkurs(n, k, konk), file=resultFile)
myFile.close()
resultFile.close()
