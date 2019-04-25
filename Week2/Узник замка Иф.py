a, b, c = int(input()), int(input()), int(input())
d, e = int(input()), int(input())
case1 = d >= a and e >= b or d >= b and e >= a
case2 = d >= a and e >= c or d >= c and e >= a
case3 = d >= b and e >= c or d >= c and e >= b
if case1 or case2 or case3:
    print('YES')
else:
    print('NO')
