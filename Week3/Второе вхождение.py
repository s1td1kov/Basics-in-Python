s = input()
first_pos = s.find('f')
if first_pos == -1:
    print(-2)
else:
    temp = 1
    pos = first_pos
    while pos != -1:
        pos = s.find('f', pos + 1)
        temp += 1
    if temp - 1 == 1:
        print(-1)
    else:
        print(s.find('f', first_pos + 1))
