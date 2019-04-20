firstSet = set(map(int, input().split()))
secondSet = set(map(int, input().split()))
print(*sorted(list(firstSet & secondSet)))
