with open('input.txt', 'r', encoding='utf-8') as f:
    mainDict = {}
    for line in f:
        listLine = line.strip().split()
        cust = listLine[0]
        prod = listLine[1]
        num = int(listLine[2])

        if cust in mainDict:
            mainDict[cust][prod] = mainDict[cust].get(prod, 0) + num
        else:
            mainDict[cust] = {}
            mainDict[cust][prod] = num

    for el in sorted(mainDict):
        print(el, ':', sep='')
        for el1 in sorted(mainDict[el]):
            print(el1, mainDict[el][el1])
