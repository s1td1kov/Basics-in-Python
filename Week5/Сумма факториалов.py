n = int(input())
sum = 0
fac = 1
for i in range(n + 1):
    if i != 0:
        sum += fac
        fac *= (i + 1)
print(sum)
