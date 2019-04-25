n = int(input())
c1 = 10 < n < 20
c2 = n % 10 == 0
c3 = n % 10 == 5
c4 = n % 10 == 6
c5 = n % 10 == 7
c6 = n % 10 == 8
c7 = n % 10 == 9
c8 = n % 10 == 1
if c1 or c2 or c3 or c4 or c5 or c6 or c7:
    print(n, 'korov')
elif c8:
    print(n, 'korova')
else:
    print(n, 'korovy')
