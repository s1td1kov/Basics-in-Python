distances = list(map(int, input().split()))
prices = list(map(int, input().split()))
distances.sort(reverse=True)
prices.sort()
sum = 0
for i in range(len(distances)):
    sum += distances[i] * prices[i]
print(sum)
