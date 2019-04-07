n = int(input())
sch = 0
l = 1
while l <= n:
    l = str(l)
    if l == l[::-1]:
        sch = sch + 1
    l = int(l)
    l = l + 1
print(sch)
