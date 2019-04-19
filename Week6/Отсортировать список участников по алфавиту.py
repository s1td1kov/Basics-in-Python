fin = open('input.txt', 'r', encoding='utf8')

a = []

for line in fin:
    lineList = line.split()
    a.append(lineList)

a.sort(key=lambda x: x[0])

for now in a:
    print(now[0], now[1], now[3])
