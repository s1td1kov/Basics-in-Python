n = int(input())
np = list(map(int, input().split()))

for i in range(n):
    np[i] = [np[i], i + 1, 0]
np.sort()

m = int(input())
bu = list(map(int, input().split()))

for i in range(m):
    bu[i] = [bu[i], i + 1]
bu.sort()

start = 0
for i in range(n):
    idx = 0
    minimum = 10e10
    for j in range(start, m):
        tmp = abs(np[i][0] - bu[j][0])
        if tmp < minimum:
            idx = j
            minimum = tmp
            np[i][2] = bu[j][1]
        else:
            break
    start = idx

np.sort(key=lambda idx: idx[1])

for now in np:
    print(now[2], end=' ')
