a = int(input())
b = int(input())
c = int(input())
if b <= a and c <= a:
    print(a)
elif a <= b and c <= b:
    print(b)
elif a <= c and b <= c:
    print(c)
