a = int(input())
b = int(input())
k = (a - b >= 0)
l = (k + 1) % 2
print(a * k + b * l)
