dict = {}
n = int(input())
for _ in range(n):
    list_line = input().split()
    for i in range(1, len(list_line)):
        dict[list_line[i]] = list_line[0]
m = int(input())
for _ in range(m):
    capital = input()
    print(dict[capital])
