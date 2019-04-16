a = list(map(int, input().split()))
min = a[0]
temp1 = 0
max = a[0]
temp2 = 0
for i in range(len(a)):
    if a[i] < min:
        min = a[i]
        temp1 = i
for i in range(len(a)):
    if max < a[i]:
        max = a[i]
        temp2 = i
(a[temp1], a[temp2]) = (a[temp2], a[temp1])
print(*a)
