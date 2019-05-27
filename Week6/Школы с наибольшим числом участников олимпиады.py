with open('input.txt', 'r', encoding='utf-8') as f:
    max = 1
    dict = {}
    for line in f:
        list_line = line.split()
        dict[int(list_line[2])] = dict.get(int(list_line[2]), 0) + 1
    dict_list = sorted(dict.items(), key=lambda x: (x[1], x[0]))
    max_class = dict_list[-1][1]
    for key, value in dict_list:
        if value == max_class:
            print(key, end=' ')
