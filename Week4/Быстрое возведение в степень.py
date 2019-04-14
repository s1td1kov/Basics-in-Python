def power(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return power(a ** 2, n // 2)
    else:
        return power(a, n - 1) * a


a, n = float(input()), int(input())
print(power(a, n))
