a = list(map(int, input().split()))
k = 0
for i in range(len(a) - 1):
    if i != 0:
        if a[i - 1] < a[i] and a[i] > a[i + 1]:
            k += 1
print(k)
