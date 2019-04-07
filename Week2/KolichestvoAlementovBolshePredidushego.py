num = int(input())
temp = num
k = 0
while num != 0:
    num = int(input())
    if num > temp:
        k = k + 1
    temp = num
print(k)
