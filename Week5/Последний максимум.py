a = list(map(int, input().split()))
k = 0
max = 0
for i in range(len(a)):
    if a[i] >= max:
        max = a[i]
        k = i
print(max, k)
