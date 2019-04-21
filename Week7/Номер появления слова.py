myFile = open('input.txt')
words = dict()
for line in myFile:
    newline = line.rstrip(line[-1])
    myList = newline.split()
    for i in range(len(myList)):
        words[myList[i]] = words.get(myList[i], 0) + 1
        print(words[myList[i]] - 1, end=' ')
