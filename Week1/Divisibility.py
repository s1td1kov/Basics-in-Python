a = int(input())
b = int(input())
k = (a % b == 0)
print('YES' * k + 'NO' * (1 - k))
