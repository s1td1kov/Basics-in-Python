fin = open('input.txt', 'r', encoding='utf8')

sum9, sum10, sum11 = 0, 0, 0
k9, k10, k11 = 0, 0, 0

for line in fin:
    listLine = line.split()
    if listLine[2] == '9':
        sum9 += int(listLine[3])
        k9 += 1
    elif listLine[2] == '10':
        sum10 += int(listLine[3])
        k10 += 1
    else:
        sum11 += int(listLine[3])
        k11 += 1

print(sum9 / k9, sum10 / k10, sum11 / k11)
