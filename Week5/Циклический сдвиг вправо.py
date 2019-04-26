list = list(map(int, input().split()))
for i in range(len(list) - 1):
    (list[len(list) - i - 1], list[len(list) - i - 2]) = \
        (list[len(list) - i - 2], list[len(list) - i - 1])
print(*list)
