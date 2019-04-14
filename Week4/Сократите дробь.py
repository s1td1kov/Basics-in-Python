def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def ReduceFraction(a, b):
    return a // gcd(a, b), b // gcd(a, b)


a, b = int(input()), int(input())
print(*ReduceFraction(a, b))
