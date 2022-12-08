import re

input = open('advent.txt', 'r')
overlap = 0
for i in input:
    rivi = i.strip('\n')
    r = re.split(',|-', rivi)

    if int(r[0]) <= int(r[2]) and int(r[1]) >= int(r[2]):
        overlap += 1
    elif int(r[0]) >= int(r[2]) and int(r[0]) <= int(r[3]):
        overlap += 1
print(overlap)