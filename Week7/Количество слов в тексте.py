myFile = open('input.txt', 'r', encoding='utf8')
mySet = set()
for line in myFile:
    string = line.split()
    for now in string:
        mySet.add(now)
print(len(mySet))
