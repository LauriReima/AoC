with open('input.txt') as t:
    data = t.readlines()

cycle = 0
sprite = 1
crtCol = 0
crt = {0:[],1:[],2:[],3:[],4:[],5:[],6:[]}

for i in data:
    row = i.strip('\n').split(' ')
    inst = row[0]
    if cycle < sprite - 1 or cycle > sprite +1:
        crt[crtCol].append(cycle)
    if inst == 'noop':
        if cycle == 39:
            cycle = 0
            crtCol += 1
        else:
            cycle += 1
        if cycle < sprite - 1 or cycle > sprite +1:
                crt[crtCol].append(cycle)
    else:
        for i in range(2):
            if i == 0:
                if cycle == 39:
                    cycle = 0
                    crtCol += 1
                else:
                    cycle += 1
                if cycle < sprite - 1 or cycle > sprite +1:
                        crt[crtCol].append(cycle)
            else:
                if cycle == 39:
                    cycle = 0
                    crtCol += 1
                else:
                    cycle += 1 
                sprite += int(row[1])
                if cycle < sprite - 1 or cycle > sprite +1:
                    crt[crtCol].append(cycle)
for i in range(6):
    for j in range(40):
        if j in crt[i]:
            print('.',end='')
        else:
            print('#',end='')
    print()