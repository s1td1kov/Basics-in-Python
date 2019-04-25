a, b, c, d = float(input()), float(input()), float(input()), float(input())
e, f = float(input()), float(input())

det = a * d - b * c
det_x = e * d - b * f
det_y = a * f - c * e
x_null = a == 0 and c == 0
y_null = b == 0 and d == 0

if det != 0:
    x = det_x / det
    y = det_y / det
    print(2, x, y)
else:
    if det_x == 0 and det_y == 0:
        if x_null and y_null:
            if e != 0 or f != 0:
                print(0)
            else:
                print(5)
        elif x_null:
            if b != 0:
                y = e / b
            else:
                y = f / d
            print(4, y)
        elif y_null:
            if a != 0:
                x = e / a
            else:
                x = f / c
            print(3, x)
        else:
            if b != 0:
                bi = e / b
                k = -a / b
            else:
                bi = f / d
                k = -c / d
            print(1, k, bi)
    else:
        print(0)
