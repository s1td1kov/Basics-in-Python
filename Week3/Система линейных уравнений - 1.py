a, b, c = float(input()), float(input()), float(input())
d, e, f = float(input()), float(input()), float(input())
dq = a * d - b * c
dx = (e * d) - (b * f)
dy = a * f - e * c
print(dx / dq, dy / dq)
