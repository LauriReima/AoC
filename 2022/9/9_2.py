
with open('input.txt') as t:
    data = t.readlines()

def sign(x):
    if x > 0:
        x = 1
    elif x < 0:
        x = -1
    else:
        x = 0
    return x

def move(dir):
    if dir == 'R':
        mato[0] = (mato[0][0], mato[0][1]+1)
    elif dir == 'L':
        mato[0] = (mato[0][0], mato[0][1]-1)
    elif dir == 'U':
        mato[0] = (mato[0][0]-1, mato[0][1])
    elif dir == 'D':
        mato[0] = (mato[0][0]+1, mato[0][1])
    for i in range(1,10):
        firrow = mato[i-1][0]
        fircol = mato[i-1][1]
        secrow = mato[i][0]
        seccol = mato[i][1]
        calcrow = firrow - secrow
        calccol = fircol - seccol
        if calcrow < -1 or calcrow > 1 or calccol < -1 or calccol > 1:
            row = sign(calcrow)
            col = sign(calccol)
            mato[i] = (secrow + row, seccol + col)
    return mato
 
mato = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]

coordinates = set()
for i in data:
    row = i.split(' ')
    direction = row[0]
    amount = int(row[1])
    r = mato[0][0]
    c = mato[0][1]
    while amount > 0:
        move(direction)          
        amount -= 1
        coordinates.add(mato[-1])
print(len(coordinates))
    