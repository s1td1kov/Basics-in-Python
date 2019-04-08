import math
p, x, y = int(input()), int(input()), int(input())
result = (x * 100 + y) * p / 100 + (x * 100 + y)
newresult = math.floor(result)
rubles = newresult // 100
penny = newresult % 100
print(rubles, penny)
