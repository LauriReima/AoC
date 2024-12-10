with open('data.txt', 'r') as tiedosto:
    data = tiedosto.read()
allmuls = []
for i, letter in enumerate(data):
    if letter == 'm':
        if data[i+1] == 'u' and data[i+2] == 'l' and data[i+3] == '(':
            allmuls.append(i)
allmuls.append(len(data))
muls = []
for j, index in enumerate(allmuls):
    if index+1 < len(data):
        muls.append(data[index:allmuls[j+1]])
    else:
        muls.append(data[index:len(data)-1])
numbers = []
for mul in muls:
    if ')' in mul:
        if mul.index(')') == 7 or mul.index(')') == 8 or mul.index(')') == 9 or mul.index(')') == 10 or mul.index(')') == 11:
            numbers.append(mul[4:mul.index(')')])
sum = 0
for num in numbers:
    bn = num.split(',')
    if bn[0].isdigit() and bn[1].isdigit():
        sum += (int(bn[0]) * int(bn[1]))
print(sum)

# mul(4,6)  index 7
# mul(4,67) index 8
# mul(4,678) index 9
# mul(45,789) index 10
# mul(456,8910) index 11
