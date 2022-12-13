with open('input.txt') as t:
    data = t.readlines()

cycle = 0
X = 1
signal = 0
for i in data:
    row = i.strip('\n').split(' ')
    inst = row[0]
    
    if inst == 'noop':
        cycle += 1
        if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
            signal += (cycle*X)
    else:
        for i in range(2):
            if i == 0:
                cycle += 1
                if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
                    signal += (cycle*X)
            else:
                cycle += 1
                if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
                    signal += (cycle*X)
                X += int(row[1])
print(signal)
