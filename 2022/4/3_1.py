import re

input = open('advent.txt', 'r')
parit = 0
for i in input:
    rivi = i.strip('\n')
    r = re.split(',|-', rivi)

    if int(r[0]) <= int(r[2]) and int(r[1]) >= int(r[3]):
       ## if int(r[1]) >= int(r[3]):
        parit += 1
    elif int(r[0]) >= int(r[2]) and int(r[1]) <= int(r[3]):
        parit += 1
print(parit)