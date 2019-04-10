num = int(input())
if num != 0:
    max1 = num
num = int(input())
if num != 0:
    max2 = num
if max1 < max2:
    (max1, max2) = (max2, max1)
while num != 0:
    num = int(input())
    if num > max1:
        max2 = max1
        max1 = num
    else:
        if num > max2:
            max2 = num
print(min(max1, max2))
