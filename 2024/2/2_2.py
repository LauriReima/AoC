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
    if isompi(rowe) or pienempi(rowe):
        safe += 1
    else:
        insafe = 0
        for i in range(len(rowe)):
            new_row = rowe[:i] + rowe[i+1:]
            print(new_row)
            if isompi(new_row) or pienempi(new_row):
                insafe += 1
            if insafe > 0:
                break
        safe += insafe
print(safe)
