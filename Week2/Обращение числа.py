n = int(input())
temp = n
k = 0
while temp != 0:
    temp = temp // 10
    k = k + 1
sum = 0
while n != 0:
    r = n % 10
    n = n // 10
    sum = sum + r * 10**(k - 1)
    k = k - 1
print(sum)
