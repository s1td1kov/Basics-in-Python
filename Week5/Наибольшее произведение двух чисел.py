list = list(map(int, input().split()))
first_max = max(list)
first_max_i = 0
first_min = min(list)
first_min_i = 0
for i in range(len(list)):
    if list[i] == first_max:
        first_max_i = i
        break
for i in range(len(list)):
    if list[i] == first_min:
        first_min_i = i
second_max = -10e10
second_max_i = 0
second_min = 10e10
second_min_i = 0
for i in range(len(list)):
    if list[i] > second_max and i != first_max_i:
        second_max = list[i]
        second_max_i = i
for i in range(len(list)):
    if list[i] < second_min and i != first_min_i:
        second_min = list[i]
        second_min_i = i
if first_max * second_max > first_min * second_min:
    print(second_max, first_max)
else:
    print(first_min, second_min)
