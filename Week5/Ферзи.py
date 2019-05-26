table = []

for _ in range(8):
    x, y = [int(s) for s in input().split()]
    tuple = (x, y)
    table.append(tuple)

k = False

for i in range(7):
    for j in range(i + 1, 8):
        if table[i][0] == table[j][0] or table[i][1] == table[j][1]:
            k = True
        elif abs(table[i][0] - table[j][0]) == abs(table[i][1] - table[j][1]):
            k = True

if k:
    print('YES')
else:
    print('NO')
