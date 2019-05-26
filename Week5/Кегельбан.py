n, m = [int(s) for s in input().split()]

keglies = ['I'] * n

for _ in range(m):
    left, right = [int(s) for s in input().split()]
    for j in range(left - 1, right):
        keglies[j] = '.'

print(''.join(keglies))
