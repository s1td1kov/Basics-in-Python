n = int(input())
mySet = set()
for i in range(1, n + 1):
    mySet.add(i)
while True:
    numbers = input()
    if numbers != 'HELP':
        numbers = set(map(int, numbers.split()))
        s = input()
        if s == 'YES':
            mySet &= numbers
        else:
            mySet -= numbers
    else:
        print(*sorted(list(mySet)))
        break
