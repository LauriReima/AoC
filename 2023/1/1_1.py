f = open("data.txt", 'r')
data = f.readlines()
numerot = '1234567890'
summa = 0
for line in range(len(data)):
    num = ''
    rivi = data[line].strip()
    for j in range(len(rivi)):
        if rivi[j] in numerot:
            num += rivi[j]
    if len(num) == 1:
        num = num+num
    else:
        num = num[0]+num[-1]
    summa += int(num)
print(summa)