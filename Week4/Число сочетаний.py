def cnk(n, k):
    if k == 0:
        return 1
    elif k == n:
        return 1
    return cnk(n - 1, k) + cnk(n - 1, k - 1)


n, k = int(input()), int(input())
print(cnk(n, k))
