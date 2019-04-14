def sum():
    n = int(input())
    if n == 0:
        return 0
    else:
        return n + sum()


print(sum())
