def CountSort(myList):
    newList = [0] * 101
    for now in myList:
        newList[now] += 1
    return newList


myList = list(map(int, input().split()))
newList = CountSort(myList)

for now in range(101):
    print((str(now) + ' ') * newList[now], end='')
