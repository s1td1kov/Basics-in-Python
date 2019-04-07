num = int(input())
max1 = 1
max2 = 1
while num != 0:
    temp = num
    num = int(input())
    if temp == num:
        max1 += 1
    else:
        if max2 < max1:
            max2 = max1
        max1 = 1
if max1 < max2:
    print(max2)
else:
    print(max1)
