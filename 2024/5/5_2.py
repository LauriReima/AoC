import math
from mod_5_1 import correct_rules

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

summa = 0
incorrect_rules = correct_rules(rules)
#for rule in incorrect_rules:

cor_rules = []
for inc_rule in incorrect_rules:
    i = 0
    rule = inc_rule.copy()
    while i < len(rule) -1:
        for j in range(i + 1, len(rule)):

            if find_page(rule[i], rule[j]):
                i += 1
            else:
                eka = rule[i]
                toka = rule[j]
                rule[i], rule[j] = toka, eka
    cor_rules.append(rule)        
tsumma = 0
for i in cor_rules:
    keskim = len(i)/2
    tsumma += i[math.floor(keskim)]
print(tsumma)
print(correct_rules(cor_rules))
print(len(incorrect_rules))
print(len(cor_rules))
# 5725 too high