import math

with open('data.txt', 'r') as tiedosto:
    lines = [line.strip() for line in tiedosto.readlines()]

pages = []
pageX = []
pageY = []
rules = []
for i in lines:
    if '|' in i:
        page = [int(num) for num in i.split('|')]
        pageX.append(page[0])
        pageY.append(page[1])
        pages.append(page)
    elif i: 
        rule = [int(num) for num in i.split(',')]
        rules.append(rule)

def find_page(x, y):
    for i, index in enumerate(pageX):
        if index == x:
            if pageY[i] == y:
                return True
    return False

def correct_rules(rules):
    summa = 0
    incorrect_rules = [] 
    for rule in rules:
        rule2 = rule.copy()
        i = 0
        accepted = 0
        while i < len(rule) -1:
            for j in range(i + 1, len(rule)):

                if find_page(rule[i], rule[j]):
                    accepted += 1

            i += 1
        test = 0
        for k in range(len(rule)):
            test += k
        #print(test,accepted)
        if accepted == test:
            keskim = len(rule)/2
            summa += rule[math.floor(keskim)]
        else:
            incorrect_rules.append(rule)
    #print(summa)
    return incorrect_rules

correct_rules(rules)