s = input()
first_pos = s.find('h')
last_pos = s.rfind('h')
first_s = s[:first_pos + 1]
last_s = s[last_pos:]
temps = s[first_pos + 1:last_pos].replace('h', 'H')
print(first_s + temps + last_s)
