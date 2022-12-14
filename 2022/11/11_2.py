from math import floor


with open('test.txt') as t:
    data = t.readlines()

monkeys = {}
for i in data:
    row = i.strip('\n').split(' ')
    if row[0] == 'Monkey':
        name = int(row[1].strip(':'))
        monkeys[name] = {}
        monkeys[name]['count'] = 0
    elif len(row) > 1:
        if row[2] == 'Starting':
            monkeys[name]['level'] = [int(x.strip(',')) for x in row[4:]]
        elif row[2] == 'Operation:':
            monkeys[name]['operation'] = [x for x in row[6:]]
        elif row[2] == 'Test:':
            monkeys[name]['test'] = int(row[5])
        elif len(row) == 10 and row[4] == 'If':
            if row[5] == 'true:': 
                monkeys[name]['true'] = int(row[9])           
            elif row[5] == 'false:':
                monkeys[name]['false'] = int(row[9])
        


counter = 0
while counter < 10000:
    for i in range(len(monkeys)):
        worry =0
        monkey = monkeys.get(i)
        j = 0
        while j < len(monkey['level']):  
            if monkey['operation'][0] == '+':
                worry = monkey['level'][j] + int(monkey['operation'][1])
            elif monkey['operation'][1] == 'old':
                worry = monkey['level'][j]**2 
            elif monkey['operation'][0] == '*':
                worry = monkey['level'][j] * int(monkey['operation'][1])
            monkey['count'] += 1
            worry = worry % monkey['test'] + (monkey['test']*7)
            if worry % monkey['test'] == 0:
                monkeys[monkey['true']]['level'].append(worry)    
                monkey['level'].remove(monkey['level'][j])   
                #print(i)
                #monkeys[monkey['true']]['count'] += 1
            elif not worry % monkey['test'] == 0:
                worry = worry%monkey['test']+monkey['test']
                monkeys[monkey['false']]['level'].append(worry)
                monkey['level'].remove(monkey['level'][j])
                #monkeys[monkey['false']]['count'] += 1
                
    counter += 1

max = 0
max2 = 0
for i in monkeys:
    print(monkeys[i])