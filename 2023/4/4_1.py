f = open("data.txt", 'r')
data = f.readlines()
total = 0
for line in data:
    line = line.strip('Card ').strip()
    rivi_nro = int(line.split(':')[0])
    voittavat = line.split(' |')[0].split(': ')[1].split(' ')
    arvotut = line.split('| ')[1].split(' ')
    win = []
    num = []
    summa = 0
    
    for i in voittavat:
        if i.isdigit():
            win.append(int(i))
    for i in arvotut:
        if i.isdigit():
            num.append(int(i))
    for winner in win:
        if winner in num:
            summa += 1
    if summa > 2:
        summa = 2**(summa-1)
    total += summa
print(total)