myFile = open('input.txt', 'r', encoding='utf8')
pupils = []

for line in myFile:
    pupils.append(line.split())

list9 = []
list10 = []
list11 = []

for pupil in pupils:
    if int(pupil[2]) == 9:
        list9.append(int(pupil[3]))
    elif int(pupil[2]) == 10:
        list10.append(int(pupil[3]))
    else:
        list11.append(int(pupil[3]))

max9 = max(list9)
max10 = max(list10)
max11 = max(list11)
maximum9 = -10e10
maximum10 = -10e10
maximum11 = -10e10

for now in list9:
    if maximum9 < now and now != max9:
        maximum9 = now
for now in list10:
    if maximum10 < now and now != max10:
        maximum10 = now
for now in list11:
    if maximum11 < now and now != max11:
        maximum11 = now

print(maximum9, maximum10, maximum11)
