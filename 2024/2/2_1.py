with open('data.txt', 'r') as tiedosto:
    rivit = tiedosto.readlines()

def isompi(list):
    for i in range(len(list)):
        if i < len(list) -1:
            if ((int(list[i+1]) - int(list[i])) < 4) and ((int(list[i+1]) - int(list[i])) > 0):
                continue
            else:
                return False
    return True

def pienempi(list):
    for i in range(len(list)):
        if i < len(list) -1:
            if ((int(list[i]) - int(list[i+1])) < 4) and ((int(list[i]) - int(list[i+1])) > 0):
                continue
            else:
                return False
    return True

safe = 0
for rivi in rivit:
    row = rivi.strip('\n')
    rowe = row.split(' ')
    if int(rowe[0]) > int(rowe[1]):
        if pienempi(rowe):
            safe += 1
    elif int(rowe[0]) < int(rowe[1]):
        if isompi(rowe):
            safe += 1

print(safe)
