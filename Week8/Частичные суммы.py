from itertools import accumulate

print(*accumulate(map(int, input().split()), lambda x, y: x + y))
