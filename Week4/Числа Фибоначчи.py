def phib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    return phib(n - 1) + phib(n - 2)


n = int(input())
print(phib(n))
