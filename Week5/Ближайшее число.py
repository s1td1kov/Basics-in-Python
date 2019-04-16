n = int(input())
tempList = list(map(int, input().split()))
k = int(input())
min = abs(k - tempList[0])
temp = tempList[0]
for now in tempList:
    if abs(now - k) < min:
        min = abs(now - k)
        temp = now
print(temp)
