s = input()
temp_s = ''
for i in range(len(s)):
    if i % 3 != 0:
        temp_s = temp_s + s[i]
print(temp_s)
