from math import sqrt

x = []
now = int(input())
x.append(now)
while now != 0:
    now = int(input())
    x.append(now)
x = x[:-1]
sumx = sum(x) / len(x)
sum = 0
for i in range(len(x)):
    sum += (x[i] - sumx)**2
print(sqrt(sum / (len(x) - 1)))
