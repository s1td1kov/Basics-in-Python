a, b = int(input()), int(input())
for i in range(a, b + 1):
    tempS = str(i)
    revS = tempS[::-1]
    if tempS == revS:
        print(tempS)
