inf = open('input.txt', 'r', encoding='utf8')
outf = open('output.txt', 'w', encoding='utf8')
words = {}
for line in inf:
    line = line.split()
    for now in line:
        words[now] = words.get(now, 0) + 1


def makeSort(dict):
    return (-dict[1], dict[0])


words = sorted(words.items(), key=makeSort)

for word in words:
    print(word[0], file=outf)

inf.close()
outf.close()
