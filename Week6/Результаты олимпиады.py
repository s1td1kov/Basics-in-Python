n = int(input())

newList = []

for i in range(n):
    temp = input()
    now = temp.split()
    newList.append(now)

newList.sort(key=lambda x: -int(x[1]))

for now in newList:
    print(now[0])
