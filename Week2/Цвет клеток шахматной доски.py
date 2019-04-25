x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
c1 = (x1 + y1) % 2 == 0
c2 = (x2 + y2) % 2 == 0
c3 = (x1 + y1) % 2 == 1
c4 = (x2 + y2) % 2 == 1
if (c1 and c2 or c3 and c4):
    print('YES')
else:
    print('NO')
