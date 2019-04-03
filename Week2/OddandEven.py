a = int(input())
b = int(input())
c = int(input())
c1 = (a % 2 == 0 and b % 2 == 1) or (a % 2 == 1 and b % 2 == 0)
c2 = (b % 2 == 0 and c % 2 == 1) or (b % 2 == 1 and c % 2 == 0)
c3 = (a % 2 == 0 and c % 2 == 1) or (a % 2 == 1 and c % 2 == 0)
if c1 or c2 or c3:
    print('YES')
else:
    print('NO')
