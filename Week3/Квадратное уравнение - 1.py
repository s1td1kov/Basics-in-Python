import math
a, b, c = float(input()), float(input()), float(input())
d = b * b - 4 * a * c
if d < 0:
    print()
elif d == 0:
    print((-b + math.sqrt(d)) / (2 * a))
else:
    x1 = (-b - math.sqrt(d)) / (2 * a)
    x2 = (-b + math.sqrt(d)) / (2 * a)
    print(min(x1, x2), max(x1, x2))
    
