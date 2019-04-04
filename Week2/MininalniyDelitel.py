n = int(input())
i = 1
minDel = 1
while i <= n:
    if i != 1 and n % i == 0:
        minDel = i
        break
    i = i + 1
print(minDel)
