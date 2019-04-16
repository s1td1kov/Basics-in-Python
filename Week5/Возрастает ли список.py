a = list(map(int, input().split()))
temp = 0
for i in range(len(a) - 1):
    if a[i] >= a[i + 1]:
        temp = 1
        break
if temp == 1:
    print('NO')
else:
    print('YES')
