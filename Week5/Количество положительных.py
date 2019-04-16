a = list(map(int, input().split()))
k = 0
for i in range(len(a)):
    if a[i] > 0:
        k = k + 1
print(k)
