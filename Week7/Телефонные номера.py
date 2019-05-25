with open('input.txt', 'r', encoding='utf-8') as f:
    list = f.readlines()

    def new_string(line):
        temp = line.replace('(', '')
        temp = temp.replace(')', '')
        temp = temp.replace('+', '')
        temp = temp.replace('-', '')
        line = temp
        if len(line) == 7:
            line = '8495' + line
        elif len(line) != 7 and line[0] == '7':
            line = '8' + line[1:]
        return line

    first_line = list[0][:-1]
    second_line = list[1][:-1]
    third_line = list[2][:-1]
    fourth_line = list[3][:-1]

    first_line = new_string(first_line)
    second_line = new_string(second_line)
    third_line = new_string(third_line)
    fourth_line = new_string(fourth_line)

    if(first_line == second_line):
        print('YES')
    else:
        print('NO')
    if(first_line == third_line):
        print('YES')
    else:
        print('NO')
    if(first_line == fourth_line):
        print('YES')
    else:
        print('NO')
