inf = open('input.txt', 'r', encoding='utf8')
resultFile = open('output.txt', 'w', encoding='utf8')
text = inf.read().splitlines()
candidates = {}
voices = len(text)

for line in text:
    candidates[line] = candidates.get(line, 0) + 1

candidates = sorted(candidates.items(), key=lambda x: x[1], reverse=True)
if candidates[0][1] > voices / 2:
    print(candidates[0][0], file=resultFile)
else:
    print(candidates[0][0], candidates[1][0], sep='\n', file=resultFile)
