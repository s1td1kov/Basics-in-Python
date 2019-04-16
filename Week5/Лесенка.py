n = int(input())
sum = 0
for i in range(n + 1):
    sum = sum * 10 + i
    if sum != 0:
        print(sum)
