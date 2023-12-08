f = open("data.txt", 'r')
data = f.readlines()
kortit = {}

for line in data:
    line = line.strip('Card ').strip()
    rivi_nro = int(line.split(':')[0])
    kortit[rivi_nro] = 1
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
    
    for m in range(kortit[rivi_nro]):
        j = 1
        while j <= summa:
            kortit[rivi_nro + j] +=  1
            j += 1
print(sum(kortit.values()))