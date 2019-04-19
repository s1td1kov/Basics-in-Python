n = int(input())
firstList = list(map(int, input().split()))
m = input()
secondList = list(map(int, input().split()))
a = [0] * n

for now in secondList:
    a[now - 1] += 1

for i in range(len(firstList)):
    if a[i] > firstList[i]:
        print('YES')
    else:
        print('NO')
