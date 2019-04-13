def IsPointInSquare(x, y):
    iff1 = y - x - 1 <= 0
    iff2 = y + x - 1 <= 0
    iff3 = y + x + 1 >= 0
    iff4 = y - x + 1 >= 0
    return iff1 and iff2 and iff3 and iff4


x, y = float(input()), float(input())
if IsPointInSquare(x, y):
    print('YES')
else:
    print('NO')
