with open('input.txt', 'r', encoding='utf-8') as f:
    dict = {}
    for line in f:
        listLine = line.split()

        if listLine[0] == 'DEPOSIT':
            name = listLine[1]
            sum = int(listLine[2])
            if name in dict:
                dict[name] += sum
            else:
                dict[name] = sum

        elif listLine[0] == 'WITHDRAW':
            name = listLine[1]
            sum = int(listLine[2])
            if name in dict:
                dict[name] -= sum
            else:
                dict[name] = -sum

        elif listLine[0] == 'BALANCE':
            name = listLine[1]
            if name in dict:
                print(dict[name])
            else:
                print('ERROR')

        elif listLine[0] == 'TRANSFER':
            first_name = listLine[1]
            second_name = listLine[2]
            sum = int(listLine[3])

            if first_name in dict and second_name in dict:
                dict[first_name] -= sum
                dict[second_name] += sum

            elif first_name not in dict and second_name in dict:
                dict[first_name] = -sum
                dict[second_name] += sum

            elif first_name in dict and second_name not in dict:
                dict[first_name] -= sum
                dict[second_name] = sum

            elif first_name not in dict and second_name not in dict:
                dict[first_name] = -sum
                dict[second_name] = sum

        elif listLine[0] == 'INCOME':
            p = int(listLine[1])
            for dic in dict:
                if dict[dic] > 0:
                    dict[dic] = int(dict[dic] * (1 + (p / 100)))
