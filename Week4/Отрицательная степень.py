def power(a, n):
    if n == 0:
        return 1
    elif n > 0:
        sum = 1
        while n > 0:
            sum *= a
            n = n - 1
        return sum
    else:
        sum = 1
        while n < 0:
            sum *= 1 / a
            n = n + 1
        return sum


a, n = float(input()), int(input())
print(power(a, n))
