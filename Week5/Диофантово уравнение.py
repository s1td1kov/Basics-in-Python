a, b, c, d = int(input()), int(input()), int(input()), int(input())
e = int(input())
k = 0
for x in range(0, 1001):
    if x != e and a * x ** 3 + b * x ** 2 + c * x + d == 0:
        k += 1
print(k)
