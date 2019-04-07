num = int(input())
max = num
k = 1
while num != 0:
    num = int(input())
    if max == num:
        k = k + 1
    else:
        if max < num:
            max = num
            k = 1
        else:
            continue
print(k)
