s = input()
if s.find('f') == -1:
    print()
else:
    first_pos = s.find('f')
    pos = first_pos
    temp = 1
    while pos != -1:
        pos = s.find('f', pos + 1)
        temp = temp + 1
    if temp - 1 == 1:
        print(first_pos)
    else:
        print(first_pos, s.rfind('f'))
