myList = list(map(int, input().split()))
mySet = set()
lenk = 0
for now in myList:
    mySet.add(now)
    if lenk == len(mySet):
        print('YES')
    else:
        print('NO')
    lenk = len(mySet)
