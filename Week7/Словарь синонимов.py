n = int(input())
dict = {}
for i in range(n):
    s = input()
    s1, s2 = s.split()
    dict[s1] = s2
    dict[s2] = s1
s = input()
print(dict[s])
