x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
c1 = (x1 > 0) and (x2 > 0) and (y1 > 0) and (y2 > 0)
c2 = (x1 > 0) and (x2 > 0) and (y1 < 0) and (y2 < 0)
c3 = (x1 < 0) and (x2 < 0) and (y1 > 0) and (y2 > 0)
c4 = (x1 < 0) and (x2 < 0) and (y1 < 0) and (y2 < 0)
if c1 or c2 or c3 or c4:
    print('YES')
else:
    print('NO')
