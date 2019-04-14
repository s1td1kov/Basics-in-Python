def power(a, n):
    if n == 0:
        return 1
    return power(a, n - 1) * a


a, n = float(input()), int(input())
print(power(a, n))
