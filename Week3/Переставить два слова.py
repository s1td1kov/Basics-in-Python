s = input()
pos = s.find(' ')
first_word = s[:pos]
last_word = s[pos + 1:]
print(last_word, first_word)
