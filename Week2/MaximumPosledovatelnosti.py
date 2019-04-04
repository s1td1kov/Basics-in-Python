num = int(input())
maxNum = num
while num != 0:
    num = int(input())
    if num != 0 and maxNum < num:
        maxNum = num
print(maxNum)
