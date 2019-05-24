with open('input.txt', 'r', encoding='utf-8') as f:
    dict = {}

    for line in f:
        list = line.split()
        dict[list[0]] = dict.get(list[0], 0) + int(list[1])

    new_dict = sorted(dict.items(), key=lambda x: x[0])
    for key, value in new_dict:
        print(key, value)
