with open('input.txt') as t:
    data = t.readlines()

def pienempi(lista, arvo):
    for i in lista:
        if i >= arvo:
            return False
    return True

def isVisible(kartta, y, x):
    top = []
    down = []
    left = []
    right = []
    for i in range(len(kartta)):
        if i < y:
            top.append(kartta[i][x])
        elif i > y:
            down.append(kartta[i][x])
    for j in range(len(kartta[y])):
        if j < x:
            left.append(kartta[y][j])
        elif j > x:
            right.append(kartta[y][j])
    if pienempi(top, kartta[y][x]) or pienempi(down, kartta[y][x]) or pienempi(left, kartta[y][x]) or pienempi(right, kartta[y][x]):
        return True
    else:
        return False



laskuri = 0
for i in range(len(data)):
    rivi = data[i].strip('\n')
    for j in range(len(rivi)):
        if i == 0 or i == len(data)-1:
            laskuri += 1
        elif j == 0 or j == len(rivi)-1:
            laskuri += 1
        else:
            if isVisible(data,i,j) == True:
                laskuri += 1
print(laskuri)


    
