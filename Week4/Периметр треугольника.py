import math


def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def perimeter(x1, y1, x2, y2, x3, y3):
    p1 = distance(x1, y1, x2, y2)
    p2 = distance(x1, y1, x3, y3)
    p3 = distance(x2, y2, x3, y3)
    p = p1 + p2 + p3
    return p


x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
x3, y3 = float(input()), float(input())
print(perimeter(x1, y1, x2, y2, x3, y3))
