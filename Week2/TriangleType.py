a = int(input())
b = int(input())
c = int(input())
if (a + b <= c) or (a + c <= b) or (b + c <= a):
    print('impossible')
else:
    if (a**2 + b**2 == c**2)or(a**2 + c**2 == b**2)or(b**2 + c**2 == a**2):
        print('rectangular')
    elif (a**2 + b**2 > c**2)and(a**2 + c**2 > b**2)and(b**2 + c**2 > a**2):
        print('acute')
    elif (a**2 + b**2 < c**2)or(a**2 + c**2 < b**2)or(b**2 + c**2 < a**2):
        print('obtuse')
