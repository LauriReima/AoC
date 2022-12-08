f = open("advent.txt", 'r')
x = f.readlines()
sum = 0
list = []
for i in x:  
    if i != '\n':
        sum += int(i)
    else:
        list.append(sum)
        sum = 0
    #print(i.strip('\n'))
a = 0
b = 0
c = 0
for j in range(len(list)):
    if list[j] > c and list[j] > b and list[j] > a:
        c = b
        b = a
        a = list[j]
    elif list[j] > c and list[j] > b:
        c = b
        b = list[j]
    elif list[j] > c:
        c = list[j]
print(a+b+c)

