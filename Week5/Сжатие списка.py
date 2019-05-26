list_numbers = list(map(int, input().split()))
new_list = []

for i in range(len(list_numbers)):
    if int(list_numbers[i]) > 0:
        new_list.append(list_numbers[i])

for _ in range(len(list_numbers) - len(new_list)):
    new_list.append(0)

print(*new_list)
