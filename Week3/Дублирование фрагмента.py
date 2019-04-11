s = input()
first_pos = s.find('h')
last_pos = s.rfind('h')
temps = s[first_pos + 1:last_pos]
temps = temps + temps
first_s = s[:first_pos + 1]
last_s = s[last_pos:]
print(first_s + temps + last_s)
