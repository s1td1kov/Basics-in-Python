from collections import OrderedDict

numbers = list(map(int, input().split()))
dict = {}

for number in numbers:
    dict[number] = dict.get(number, 0) + 1

dict = OrderedDict(dict)

for number in numbers:
    if dict[number] == 1:
        print(number, end=' ')
