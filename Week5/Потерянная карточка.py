n = int(input())
sum = n * (n + 1) // 2
for i in range(n - 1):
    temp = int(input())
    sum -= temp
print(sum)
