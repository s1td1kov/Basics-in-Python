n = int(input())
x = float(input())
i = 0
sum = 0
while i <= n:
    temp = float(input())
    sum = sum * x + temp
    i = i + 1
print(sum)
