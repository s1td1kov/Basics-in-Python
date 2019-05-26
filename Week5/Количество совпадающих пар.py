numbers = list(map(int, input().split()))
n = len(numbers)
k = 0

for i in range(n - 1):
    for j in range(i + 1, n):
        if numbers[i] == numbers[j]:
            k += 1
print(k)
