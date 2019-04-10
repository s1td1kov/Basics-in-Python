import math
a, b, c = float(input()), float(input()), float(input())
d = b * b - 4 * a * c
if a == 0:
    if b == 0:
        if c == 0:
            print(3)
        else:
            print(0)
    else:
        if c == 0:
            print(3)
        else:
            print(1, -c / b)
else:
    if d < 0:
        print(0)
    elif d == 0:
        print(1, (-b + math.sqrt(d)) / (2 * a))
    else:
        x1 = (-b - math.sqrt(d)) / (2 * a)
        x2 = (-b + math.sqrt(d)) / (2 * a)
        print(2, min(x1, x2), max(x1, x2))
        
