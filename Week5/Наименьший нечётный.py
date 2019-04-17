a = list(map(int, input().split()))
Odd = 0
for i in range(len(a)):
    if a[i] % 2 != 0:
        Odd = a[i]
for i in range(len(a)):
    if a[i] % 2 != 0 and Odd > a[i]:
        Odd = a[i]
print(Odd)
