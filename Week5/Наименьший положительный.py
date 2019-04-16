a = list(map(int, input().split()))
minp = a[0]
for i in range(len(a)):
    if a[i] > 0:
        minp = a[i]
        break
for i in range(len(a)):
    if a[i] > 0 and a[i] < minp:
        minp = a[i]
print(minp)
