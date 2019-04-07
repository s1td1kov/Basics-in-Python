n = int(input())
f0 = 1
f1 = 1
k = 2
sum = 0
if n == 1:
    print(1)
elif n == 2:
    print(1)
else:
    while k < n:
        sum = f0 + f1
        f0 = f1
        f1 = sum
        k = k + 1
    print(sum)
