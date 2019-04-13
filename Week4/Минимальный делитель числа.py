import math


def MinDivisor(n):
    divisor, i = 1, 2
    while i <= math.sqrt(n):
        if n % i == 0:
            divisor = i
            break
        i = i + 1
    return divisor


n = int(input())
if MinDivisor(n) == 1:
    print(n)
else:
    print(MinDivisor(n))
