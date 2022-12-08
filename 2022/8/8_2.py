with open('input.txt') as t:
    data = t.readlines()


def visibleTop(kartta, y, x):
    top = []
    i = y -1
    while i >= 0:  
        if kartta[i][x] < kartta[y][x]:
            top.append(kartta[i][x])
        else:
            top.append(kartta[i][x])
            break
        i -= 1  
    return len(top)
def visibleDown(kartta, y, x):
    down = []
    i = y + 1
    while i < len(kartta):  
        if kartta[i][x] < kartta[y][x]:
            down.append(kartta[i][x])
        else:
            down.append(kartta[i][x])
            break
        i += 1
    return len(down)
def visibleLeft(kartta, y, x):
    left = []
    i = x - 1
    while i >= 0:  
        if kartta[y][i] < kartta[y][x]:
            left.append(kartta[i][x])
        else:
            left.append(kartta[i][x])
            break
        i -= 1
    return len(left)
def visibleRight(kartta, y, x):
    right = []    
    i = x+1
    while i < len(kartta[y])-1:  
        if kartta[y][i] < kartta[y][x]:
            right.append(kartta[i][x])
        else:
            right.append(kartta[i][x])
            break
        i += 1
    return len(right)

laskuri = 0
for i in range(len(data)):
    rivi = data[i].strip('\n')
    for j in range(len(rivi)):
        tulos = visibleRight(data,i,j) * visibleLeft(data,i,j) * visibleDown(data,i,j) * visibleTop(data,i,j)
        if tulos > laskuri:
            laskuri = tulos
print(laskuri)


    
