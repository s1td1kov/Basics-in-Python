a, b, c = int(input()), int(input()), int(input())
if a >= b and a >= c:
    (a, b) = (b, a)
    (b, c) = (c, b)
    if a > b:
        (a, b) = (b, a)
elif b >= a and b >= c:
    (b, c) = (c, b)
    if a > b:
        (a, b) = (b, a)
else:
    if a > b:
        (a, b) = (b, a)
print(a, b, c)
