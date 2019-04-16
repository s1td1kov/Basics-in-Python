a = list(map(int, input().split()))
b = list(map(int, input().split()))
k = b[0]
c = b[1]
a.insert(k, c)
print(' '.join(map(str, a)))
