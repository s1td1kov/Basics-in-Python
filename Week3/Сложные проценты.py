import math
p, x, y, k = int(input()), int(input()), int(input()), int(input())
i = 0
penny = x * 100 + y
while i < k:
    penny += penny * p / 100
    i = i + 1
    penny = math.floor(penny)
rubles = penny // 100
penny = penny % 100
print(rubles, penny)
