a = list(map(int, input().split()))
max = a[0]
maxi = 0
for i in range(len(a)):
    if a[i] > max:
        max = a[i]
        maxi = i
print(max, maxi)
