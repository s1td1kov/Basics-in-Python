def IsPointInFirst(x, y):
    inCircle = (x + 1) ** 2 + (y - 1) ** 2 <= 4
    aboveFirstLine = x + y >= 0
    aboveSecondLine = y - 2 * x - 2 >= 0
    return inCircle and aboveFirstLine and aboveSecondLine


def IsPointInSecond(x, y):
    outCircle = (x + 1) ** 2 + (y - 1) ** 2 >= 4
    underFirstLine = x + y <= 0
    underSecondLine = y - 2 * x - 2 <= 0
    return outCircle and underFirstLine and underSecondLine


def IsPointInArea(x, y):
    return IsPointInFirst(x, y) or IsPointInSecond(x, y)


x, y = float(input()), float(input())
if IsPointInArea(x, y):
    print('YES')
else:
    print('NO')
