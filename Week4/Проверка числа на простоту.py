import math


def MinDivisor(n):
    divisor, i = 1, 2
    while i <= math.sqrt(n):
        if n % i == 0:
            divisor = i
            break
        i = i + 1
    return divisor


def IsPrime(n):
    if n != 1:
        return MinDivisor(n) == 1
    else:
        return False


n = int(input())
if IsPrime(n):
    print('YES')
else:
    print('NO')
