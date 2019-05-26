sentence = input()

list_sentence = sentence.split()

k = 0

for word in list_sentence:
    if word.lower() in dict:
        if dict[word.lower()].find(word) != -1:
            continue
        else:
            k += 1

    else:
        l = 0
        for c in word:
            if 'A' <= c <= 'Z':
                l += 1
        if l == 1:
            continue
        else:
            k += 1

print(k)
