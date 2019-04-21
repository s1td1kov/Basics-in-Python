n = int(input())
allLang = set()
oneLang = set()
m = int(input())
temp1 = set()
for i in range(m):
    s = input()
    temp1.add(s)
allLang = temp1.copy()
oneLang = temp1.copy()
for i in range(1, n):
    m = int(input())
    for i in range(m):
        s = input()
        temp1.add(s)
    allLang |= temp1
    oneLang &= temp1
    temp1 = set()
print(len(oneLang))
for now in oneLang:
    print(now)
print(len(allLang))
for now in allLang:
    print(now)
