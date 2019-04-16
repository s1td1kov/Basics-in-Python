a = list(map(int, input().split()))
if len(a) % 2 == 0:
    for i in range(0, len(a), 2):
        (a[i], a[i + 1]) = (a[i + 1], a[i])
else:
    for i in range(0, len(a) - 1, 2):
        (a[i], a[i + 1]) = (a[i + 1], a[i])
print(*a)
