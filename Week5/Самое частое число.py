list_numbers = list(map(int, input().split()))
dict = {}

for number in list_numbers:
    dict[number] = dict.get(number, 0) + 1

new_dict = sorted(dict.items(), key=lambda x: (x[1], x[0]))
print(new_dict[-1][0])
