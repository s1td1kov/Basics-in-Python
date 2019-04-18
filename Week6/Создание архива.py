a = list(map(int, input().split()))
S = a[0]
n = a[1]
b = []
for i in range(n):
    temp = int(input())
    b.append(temp)
b.sort()
sum = 0
k = 0
for now in b:
    sum += now
    if sum <= S:
        k += 1
    else:
        break
print(k)
