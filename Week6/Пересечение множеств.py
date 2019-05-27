set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))
print(*sorted((set1 & set2)))
