import math
x = float(input())
y = (x * 10) % 10
if y >= 5:
    print(math.ceil(x))
if y < 5:
    print(int(x))
    
